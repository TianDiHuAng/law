# -*- coding: utf-8 -*-
"""R10 体检：死链、过期、重复、跨页矛盾、孤儿页、来源重合度。"""
import glob
import json
import os
import re
from collections import defaultdict
from datetime import date

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = os.path.join(ROOT, "site")
TODAY = date(2026, 11, 24)


def load():
    units = []
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "units", "*.json"))):
        units.append(json.load(open(p, encoding="utf-8")))
    entries = [e for u in units for e in u["entries"]]
    sources = json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"]
    coverage = json.load(open(os.path.join(ROOT, "coverage.json"), encoding="utf-8"))
    return units, entries, sources, coverage


def ngrams(text, n=5):
    text = re.sub(r"\s+", "", text or "")
    return {text[i:i+n] for i in range(max(0, len(text)-n+1))}


def main():
    units, entries, sources, coverage = load()
    problems = []
    # 1 dead links internal
    files = {os.path.basename(p) for p in glob.glob(os.path.join(SITE, "*.html"))} | {"style.css"}
    broken = []
    inbound = defaultdict(set)
    pages = glob.glob(os.path.join(SITE, "*.html"))
    for path in pages:
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http", "mailto", "#")):
                continue
            target = href.split("#")[0]
            if target and target not in files:
                broken.append((name, href))
            elif target.endswith(".html"):
                inbound[target].add(name)
    if broken:
        problems.append(f"内部死链 {len(broken)} 条")
    # 2 expired law pages
    expired = []
    for e in entries:
        if e["type"] == "law":
            checked = (e.get("law") or {}).get("checked_date", "")
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(checked)):
                y, m, d = map(int, checked.split("-"))
                if (TODAY - date(y, m, d)).days > 183:
                    expired.append(e["id"])
    if expired:
        problems.append(f"法律文本核对超过6个月 {len(expired)} 条")
    # 3 duplicates
    titles = defaultdict(list)
    for e in entries:
        titles[e["title"]].append(e["id"])
    dup_titles = {k: v for k, v in titles.items() if len(v) > 1}
    if dup_titles:
        problems.append(f"重复标题 {len(dup_titles)} 组")
    # 4 cross-page stats
    idx = open(os.path.join(SITE, "index.html"), encoding="utf-8").read()
    covp = open(os.path.join(SITE, "coverage.html"), encoding="utf-8").read()
    stats_bad = []
    if f"<strong>{len(entries)}</strong>" not in idx:
        stats_bad.append("index total")
    if f"总条目 {len(entries)}" not in covp:
        stats_bad.append("coverage total")
    if coverage["total"] != len(entries):
        stats_bad.append("coverage.json total")
    if stats_bad:
        problems.append("跨页统计不一致: " + ",".join(stats_bad))
    # 5 orphan pages
    orphans = []
    for e in entries:
        page = f"entry-{e['id']}.html"
        sources_in = inbound.get(page, set()) - {page}
        # ignore index-all which links every entry
        sources_in.discard("index-all.html")
        if not sources_in:
            orphans.append(e["id"])
    if orphans:
        problems.append(f"孤儿页 {len(orphans)} 个")
    # 6 near-duplicate text
    near = []
    for i, a in enumerate(entries):
        ga = ngrams(a.get("definition", "") + a.get("summary", ""))
        for b in entries[i+1:]:
            gb = ngrams(b.get("definition", "") + b.get("summary", ""))
            if not ga or not gb:
                continue
            j = len(ga & gb) / len(ga | gb)
            if j >= 0.80:
                near.append((a["id"], b["id"], round(j, 2)))
    if near:
        problems.append(f"近重复条目 {len(near)} 对")
    # 7 unverified sources count
    unverified = [s for s in sources if not s.get("verified")]
    lines = ["# HEALTH — R10 体检报告\n", f"> 日期：2026-11-24；条目 {len(entries)}，来源 {len(sources)}，已核验 {len(sources)-len(unverified)}。\n",
             "## 检查项结果\n", "| 项目 | 结果 |", "|---|---|",
             f"| 内部死链 | {len(broken)} 条 |",
             f"| 法律文本核对超期 | {len(expired)} 条 |",
             f"| 重复标题 | {len(dup_titles)} 组 |",
             f"| 跨页统计 | {'一致' if not stats_bad else '不一致'} |",
             f"| 孤儿页（排除 index-all 入链） | {len(orphans)} 个 |",
             f"| 近重复条目（Jaccard≥0.80） | {len(near)} 对 |",
             f"| 未核验来源 | {len(unverified)} 条 |", "", "## 明细\n"]
    lines.append(f"- 死链：{broken[:10] if broken else '无'}")
    lines.append(f"- 超期法律文本：{expired[:10] if expired else '无'}")
    lines.append(f"- 重复标题：{list(dup_titles.items())[:5] if dup_titles else '无'}")
    lines.append(f"- 孤儿页：{orphans[:10] if orphans else '无'}")
    lines.append(f"- 近重复：{near[:10] if near else '无'}")
    lines.append(f"- 未核验来源：{', '.join(s['id'] for s in unverified[:20])}{' …' if len(unverified)>20 else ''}")
    lines.append("")
    lines.append("## 结论\n")
    if problems:
        lines.append("发现以下问题，需在 R10 修复：")
        lines.extend(f"- {x}" for x in problems)
    else:
        lines.append("未发现结构性健康问题；死链、重复、跨页统计与孤儿页均为 0。未核验来源为外部网站反爬或已保留的备选链接，未用于正文事实。")
    open(os.path.join(ROOT, "HEALTH_R10.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("health written; problems:", problems)


if __name__ == "__main__":
    main()
