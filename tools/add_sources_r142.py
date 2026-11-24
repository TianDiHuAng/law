# -*- coding: utf-8 -*-
"""R142 体检：登记本轮实际打开核对的官方来源。"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PATH = os.path.join(ROOT, "sources.json")
TODAY = "2026-11-24"

NEW = [
    {
        "id": "src-spc-ji-list",
        "title": "最高人民法院·司法解释栏目（含2025—2026年新发布司法解释目录）",
        "author": "最高人民法院",
        "year": 2026,
        "url": "https://www.court.gov.cn/fabu/gengduo/16.html",
        "type": "司法解释",
        "jurisdiction": "中国",
        "version": "栏目页（核对至2026-11-24，共401篇）",
        "effective_date": "待核实",
        "note": "用于体检轮核对是否有新的司法解释发布；仅作为目录性依据，具体条文以各司法解释正文为准。",
        "layer": "司法解释",
        "link_ok": True,
        "http_status": 200,
        "page_title": "司法解释 - 中华人民共和国最高人民法院",
        "verified": True,
        "checked_date": TODAY,
    },
    {
        "id": "src-spc-fs-2026-15",
        "title": "最高人民法院关于适用《中华人民共和国生态环境法典》时间效力的若干规定（法释〔2026〕15号）",
        "author": "最高人民法院",
        "year": 2026,
        "url": "https://www.court.gov.cn/fabu/xiangqing/508001.html",
        "type": "司法解释",
        "jurisdiction": "中国",
        "version": "法释〔2026〕15号（2026年7月27日审判委员会第1980次会议通过）",
        "effective_date": "2026-08-15",
        "note": "载明生态环境法典于2026-08-15施行；据此将环境法相关条目标为待复核。",
        "layer": "司法解释",
        "link_ok": True,
        "http_status": 200,
        "page_title": "最高人民法院关于适用《中华人民共和国生态环境法典》时间效力的若干规定",
        "verified": True,
        "checked_date": TODAY,
    },
]


def main():
    data = json.load(open(PATH, encoding="utf-8"))
    have = {s["id"] for s in data["sources"]}
    added = []
    for s in NEW:
        if s["id"] not in have:
            data["sources"].append(s)
            added.append(s["id"])
    json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("added:", added, "total:", len(data["sources"]))


if __name__ == "__main__":
    main()
