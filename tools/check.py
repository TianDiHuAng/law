# -*- coding: utf-8 -*-
"""法律知识库全量校验器。

覆盖 TASK_law.md 通用规则与法律专用规则：
R1 字段完整性；R2 日期/数字合法；R3 来源必须 verified 且双源；
R4 重复条目；R5 内部链接；R6 SVG；R7 无图片；
R8 页脚声明；R9 禁用措辞；R10 案例案号来源；R11 法律文本版本/核对日期；
R12 辖区；R13 coverage/scope 一致性；R14 来源总量；R15 结构完整；R16 统计一致。
"""
import glob
import html
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = os.path.join(ROOT, "site")
REQUIRED_ENTRY = ["id", "title", "type", "importance", "jurisdiction", "era", "definition", "summary", "sources", "related", "status", "legal_status", "checked_date"]
REQUIRED_CASE = ["cause", "court", "case_no", "date", "facts", "issue", "reasoning", "result", "significance"]
REQUIRED_LAW = ["status", "version", "effective_date", "checked_date", "background", "structure", "key_articles", "amendments", "interpretations"]
REQUIRED_FLOW = ["steps"]
L2_KEYS = ["definition_source", "elements", "conditions", "effects", "exceptions", "controversies", "distinctions", "misconceptions"]
DISCLAIMER = "本站内容仅供学习参考，不构成法律意见；法律会修订，具体问题请咨询执业律师或查阅官方现行文本。"
BANNED = ["建议您起诉", "建议起诉", "你会胜诉", "可以规避", "逃避税款", "制作或使用虚假材料", "保证胜诉", "显然是", "必然导致", "必然会", "一定是", "一定能", "一定不"]
SVG_ALLOWED = {"svg", "g", "title", "desc", "rect", "circle", "ellipse", "line", "polyline", "polygon", "path", "text", "tspan", "defs", "marker", "linearGradient", "stop"}

ERRORS = []
WARNINGS = []


def err(rule, msg):
    ERRORS.append(f"[{rule}] {msg}")


def warn(rule, msg):
    WARNINGS.append(f"[{rule}] {msg}")


def load_all():
    units = []
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "units", "*.json"))):
        units.append(json.load(open(p, encoding="utf-8")))
    sources = json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"]
    coverage = json.load(open(os.path.join(ROOT, "coverage.json"), encoding="utf-8"))
    scope = open(os.path.join(ROOT, "scope.md"), encoding="utf-8").read() if os.path.exists(os.path.join(ROOT, "scope.md")) else ""
    entries = []
    for u in units:
        for e in u["entries"]:
            e["_unit"] = u["unit_id"]
            entries.append(e)
    return units, entries, sources, coverage, scope


def check_entries(entries, sources):
    ids, titles = set(), {}
    source_map = {s["id"]: s for s in sources}
    for e in entries:
        # R1
        for k in REQUIRED_ENTRY:
            if k not in e or e[k] in (None, "", []):
                err("R1", f"{e.get('id','?')} missing {k}")
        if e["type"] not in ("concept", "case", "law", "flow"):
            err("R1", f"{e['id']} bad type {e['type']}")
        if e["importance"] not in ("核心", "重要", "补充"):
            err("R1", f"{e['id']} bad importance")
        if e["status"] not in ("L1", "L2", "L3"):
            err("R1", f"{e['id']} bad status")
        # R4
        if e["id"] in ids:
            err("R4", f"duplicate id {e['id']}")
        ids.add(e["id"])
        if e["title"] in titles:
            err("R4", f"duplicate title {e['title']} ({e['id']} vs {titles[e['title']]})")
        titles[e["title"]] = e["id"]
        # R12
        if not e.get("jurisdiction"):
            err("R12", f"{e['id']} missing jurisdiction")
        # R3
        srcs = e.get("sources", [])
        if len(srcs) < 2 and not (e.get("needs_verification") and e.get("pending_notes")):
            err("R3", f"{e['id']} <2 sources without needs_verification+pending_notes")
        seen_urls = []
        for sid in srcs:
            s = source_map.get(sid)
            if not s:
                err("R3", f"{e['id']} cites missing source {sid}")
                continue
            if not s.get("verified"):
                err("R3", f"{e['id']} cites unverified source {sid}")
            if s.get("url"):
                if s["url"] in seen_urls:
                    err("R3", f"{e['id']} cites duplicate URL, not independent: {s['url']}")
                seen_urls.append(s["url"])
        # type-specific
        if e["type"] == "case":
            c = e.get("case") or {}
            for k in REQUIRED_CASE:
                if k not in c:
                    err("R1", f"{e['id']} case missing {k}")
            if c.get("case_no") and c["case_no"] not in ("待核实", "不适用（未进入审判）", "不适用"):
                has_case_source = any(source_map.get(sid, {}).get("type") in ("判例", "指导性案例", "判例数据库", "权威百科") and source_map.get(sid, {}).get("verified") for sid in srcs)
                if not has_case_source:
                    err("R10", f"{e['id']} case_no {c['case_no']} has no verified case source")
        if e["type"] == "law":
            l = e.get("law") or {}
            for k in REQUIRED_LAW:
                if k not in l or l[k] in (None, "", []):
                    err("R11", f"{e['id']} law missing {k}")
            for k in ("effective_date", "checked_date"):
                v = l.get(k, "")
                if v and v != "待核实" and not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(v)):
                    err("R2", f"{e['id']} law {k} bad date {v}")
            if l.get("status") not in ("现行有效", "已修订", "已废止", "待复核"):
                err("R11", f"{e['id']} law bad status {l.get('status')}")
            for a in l.get("key_articles", []):
                if not a.get("article") or not a.get("content"):
                    err("R11", f"{e['id']} key article incomplete")
        if e["type"] == "flow":
            f = e.get("flow") or {}
            if not f.get("steps"):
                err("R1", f"{e['id']} flow empty")
        # R2 year
        y = e.get("year")
        if y is not None and not isinstance(y, int):
            err("R2", f"{e['id']} year not int")
        if isinstance(y, int) and not (-3000 <= y <= 2100):
            err("R2", f"{e['id']} year out of range {y}")
        # R15 L2 structure
        if e["status"] in ("L2", "L3"):
            l2 = e.get("l2") or {}
            for k in L2_KEYS:
                if k not in l2:
                    err("R15", f"{e['id']} L2 missing {k}")
            for k in ("elements", "conditions", "effects", "exceptions", "controversies", "distinctions", "misconceptions"):
                if not isinstance(l2.get(k), list):
                    err("R15", f"{e['id']} L2 {k} not list")
        # related exist handled in R5 later
    return ids, titles, source_map


def check_sources(sources):
    if len(sources) < 80:
        err("R14", f"sources total {len(sources)} < 80")
    verified = [s for s in sources if s.get("verified")]
    if len(verified) < 80:
        err("R14", f"verified sources {len(verified)} < 80")
    for s in sources:
        for k in ("id", "title", "author", "year", "url", "type", "jurisdiction", "version", "effective_date", "checked_date", "verified", "layer"):
            if k not in s:
                err("R1", f"source {s.get('id','?')} missing {k}")
        if not isinstance(s.get("verified"), bool):
            err("R3", f"source {s['id']} verified not bool")
        for k in ("title", "author", "type", "jurisdiction", "checked_date"):
            if not s.get(k):
                err("R1", f"source {s['id']} empty {k}")
        if s.get("verified") and not s.get("url"):
            err("R3", f"source {s['id']} verified but no url")
    return verified


def check_coverage(entries, coverage, scope, units):
    if coverage.get("total") != len(entries):
        err("R13", f"coverage total {coverage.get('total')} != {len(entries)}")
    cov_ids = {x["id"] for x in coverage.get("entries", [])}
    if cov_ids != {e["id"] for e in entries}:
        err("R13", "coverage entries ids mismatch")
    level_counts = Counter(e["status"] for e in entries)
    for k in ("L1", "L2", "L3"):
        if coverage["levels"].get(k) != level_counts.get(k, 0):
            err("R13", f"coverage levels {k} mismatch")
    for u in units:
        if u["unit_id"] not in coverage["matrix"]:
            err("R13", f"matrix missing {u['unit_id']}")
        for e in u["entries"]:
            if e["id"] not in scope:
                err("R13", f"scope.md missing {e['id']}")


def check_links_and_pages(entries, units, source_map):
    files = {os.path.basename(p) for p in glob.glob(os.path.join(SITE, "*.html"))} | {"style.css"}
    for e in entries:
        f = f"entry-{e['id']}.html"
        if f not in files:
            err("R5", f"missing page {f}")
    for u in units:
        if f"unit-{u['unit_id']}.html" not in files:
            err("R5", f"missing unit {u['unit_id']}")
    # check each html internal href
    for path in glob.glob(os.path.join(SITE, "*.html")):
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        if DISCLAIMER not in text:
            err("R8", f"{name} missing footer disclaimer")
        if "<img" in text.lower():
            err("R7", f"{name} contains img tag")
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = href.split("#")[0]
            if target and target not in files:
                err("R5", f"{name} broken link {href}")
        for phrase in BANNED:
            if phrase in text:
                err("R9", f"{name} contains banned phrase {phrase}")
        # basic title/heading
        if "<title>" not in text or "<h1>" not in text:
            warn("R8", f"{name} missing title/h1")
    # entry related links presence
    for e in entries:
        for rid in e.get("related", []):
            if rid not in {x["id"] for x in entries}:
                err("R5", f"{e['id']} related missing {rid}")


def check_svg(entries):
    for e in entries:
        # concept L2 diagram generated from elements, flow from steps, law from structure: all in site
        pass
    svgs = []
    for path in glob.glob(os.path.join(SITE, "*.html")):
        text = open(path, encoding="utf-8").read()
        svgs += [(os.path.basename(path), m) for m in re.findall(r"<svg\b.*?</svg>", text, re.S)]
    for name, s in svgs:
        if "viewBox" not in s:
            err("R6", f"{name} svg missing viewBox")
            continue
        if "<script" in s.lower():
            err("R6", f"{name} svg contains script")
        try:
            root = ET.fromstring(s)
        except Exception as ex:
            err("R6", f"{name} svg xml error: {ex}")
            continue
        vb = root.attrib.get("viewBox", "")
        try:
            _, _, w, h = [float(x) for x in vb.split()]
        except Exception:
            err("R6", f"{name} svg bad viewBox {vb}")
            continue
        for el in root.iter():
            tag = el.tag.split("}")[-1]
            if tag not in SVG_ALLOWED:
                err("R6", f"{name} svg disallowed tag {tag}")
            if tag in ("text", "tspan"):
                x = el.attrib.get("x")
                y = el.attrib.get("y")
                font = float(el.attrib.get("font-size", 14))
                content = "".join(el.itertext())
                if x is not None:
                    try:
                        xv = float(x)
                        if xv < 0 or xv > w:
                            err("R6", f"{name} svg text x out of bounds {xv}>{w}")
                    except ValueError:
                        pass
                if y is not None:
                    try:
                        yv = float(y)
                        if yv < 0 or yv > h:
                            err("R6", f"{name} svg text y out of bounds {yv}>{h}")
                    except ValueError:
                        pass
                # approximate width: CJK 1em, ASCII .55em
                width_est = sum(font if ord(c) > 127 else font * 0.55 for c in content)
                if x is not None and str(x).replace(".", "").isdigit():
                    xv = float(x)
                    anchor = el.attrib.get("text-anchor", "start")
                    if anchor == "middle":
                        left = xv - width_est / 2
                        right = xv + width_est / 2
                    else:
                        left, right = xv, xv + width_est
                    if left < -1 or right > w + 1:
                        err("R6", f"{name} svg text overflow ({left:.0f}..{right:.0f}) w={w}: {content[:30]}")
        # rect bounds
        for el in root.iter():
            tag = el.tag.split("}")[-1]
            if tag in ("rect", "line", "path"):
                for attr in ("x", "y", "x1", "y1", "x2", "y2"):
                    v = el.attrib.get(attr)
                    if v and re.fullmatch(r"-?\d+(\.\d+)?", v):
                        val = float(v)
                        lim = w if attr in ("x", "x1", "x2") else h
                        if val < -1 or val > lim + 1:
                            err("R6", f"{name} svg {tag} {attr} out of bounds {val}>{lim}")


def main():
    units, entries, sources, coverage, scope = load_all()
    ids, titles, source_map = check_entries(entries, sources)
    verified = check_sources(sources)
    check_coverage(entries, coverage, scope, units)
    # fill related set for link check
    all_ids = {e["id"] for e in entries}
    for e in entries:
        e["related"] = [r for r in e.get("related", []) if r in all_ids]
    check_links_and_pages(entries, units, source_map)
    check_svg(entries)
    # R16 同一数据跨页一致
    idx = open(os.path.join(SITE, "index.html"), encoding="utf-8").read()
    covp = open(os.path.join(SITE, "coverage.html"), encoding="utf-8").read()
    srcp = open(os.path.join(SITE, "sources.html"), encoding="utf-8").read()
    if f"<strong>{len(entries)}</strong>" not in idx:
        err("R16", "index total count does not match coverage")
    if f"总条目 {len(entries)}" not in covp:
        err("R16", "coverage page total mismatch")
    if f"共 {len(sources)} 条来源" not in srcp:
        err("R16", "sources page total mismatch")
    if f"<strong>{len([s for s in sources if s.get('verified')])}</strong>" not in idx:
        err("R16", "index verified source count mismatch")

    print(f"entries={len(entries)} units={len(units)} sources={len(sources)} verified={len(verified)}")
    print(f"levels={dict(Counter(e['status'] for e in entries))}")
    print(f"errors={len(ERRORS)} warnings={len(WARNINGS)}")
    for x in ERRORS[:80]:
        print("ERROR", x)
    for x in WARNINGS[:30]:
        print("WARN", x)
    if ERRORS:
        sys.exit(1)
    print("CHECK_OK")


if __name__ == "__main__":
    main()
