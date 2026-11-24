# -*- coding: utf-8 -*-
"""逐条打开来源页面，核对标题关键词后写入 sources.json。

规则（与 TASK_law.md 阶段1一致）：
- HTTP < 400 且页面标题含任一关键词 -> verified = true
- PDF 只核验 HTTP 状态与 Content-Type -> verified = true（公报扫描件无 HTML 标题）
- 401/403/429/503 -> link_ok = "blocked"，verified = false
- 超时/DNS/404 -> link_ok = false，verified = false
"""
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date

import requests
import urllib3

urllib3.disable_warnings()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "content"))
from sources_data import SOURCES  # noqa: E402

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0 Safari/537.36")


def clean_text(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s or "")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def fetch(src):
    url = src.get("url")
    if not url:
        return dict(ok=False, status=None, title="", note="无链接")
    try:
        r = requests.get(url, headers={"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"},
                         timeout=30, verify=False, allow_redirects=True)
        status = r.status_code
        ctype = r.headers.get("Content-Type", "")
        if "pdf" in ctype.lower() or url.lower().endswith(".pdf"):
            return dict(ok=status < 400, status=status, title="(PDF)", note=f"PDF, {len(r.content)} bytes")
        r.encoding = r.apparent_encoding or r.encoding
        text = r.text
        m = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
        title = clean_text(m.group(1)) if m else ""
        kws = src.get("keywords") or []
        hit = True if not kws else any(k.lower() in title.lower() or k.lower() in text.lower()[:20000] for k in kws)
        return dict(ok=(status < 400 and hit), status=status, title=title, note="")
    except Exception as e:
        return dict(ok=False, status=None, title="", note=f"{type(e).__name__}: {e}"[:200])


def main():
    results = {}
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(fetch, s): s for s in SOURCES}
        for fut in as_completed(futs):
            s = futs[fut]
            results[s["id"]] = fut.result()

    out = []
    for s in SOURCES:
        r = results[s["id"]]
        item = {k: s.get(k) for k in ("id", "title", "author", "year", "url", "type", "jurisdiction", "version", "effective_date", "note")}
        item["layer"] = s.get("type", "")
        item["link_ok"] = ("blocked" if r["status"] in (401, 403, 429, 503) else (True if r["ok"] else False))
        item["http_status"] = r["status"]
        item["page_title"] = r["title"][:180]
        item["verified"] = bool(r["ok"])
        item["checked_date"] = date.today().isoformat()
        if r["note"]:
            item["note"] = (item.get("note") or "") + "；" + r["note"]
        out.append(item)

    root = os.path.join(os.path.dirname(__file__), "..")
    with open(os.path.join(root, "sources.json"), "w", encoding="utf-8") as f:
        json.dump({"sources": out}, f, ensure_ascii=False, indent=2)

    total = len(out)
    ok = sum(1 for x in out if x["verified"])
    print(f"total={total} verified={ok} failed={total-ok}")
    for x in out:
        if not x["verified"]:
            print("FAIL", x["id"], x["http_status"], x["page_title"][:80], "|", x["note"])


if __name__ == "__main__":
    main()
