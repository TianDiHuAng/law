# -*- coding: utf-8 -*-
"""批次复检：每 20 条一批，随机抽查 4 条，核对来源记录与待核实标注。"""
import json
import os
import random
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TODAY = "2026-11-24"


def main():
    units = []
    for i in range(1, 12):
        units.append(json.load(open(os.path.join(ROOT, "data", "units", f"u{i:02d}.json"), encoding="utf-8")))
    entries = [e for u in units for e in u["entries"]]
    sources = {s["id"]: s for s in json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"]}
    rng = random.Random(20261124)
    batches = [entries[i:i + 20] for i in range(0, len(entries), 20)]
    lines = ["# SPOTCHECK — 批次来源抽查\n", f"> 生成日期：{TODAY}。每 20 条为一批，每批随机抽查 4 条（固定随机种子 20261124，可复现）。\n"]
    total_fail = 0
    for bi, batch in enumerate(batches, 1):
        sample = rng.sample(batch, min(4, len(batch)))
        lines.append(f"## 批次 {bi:02d}（条目 {batch[0]['id']} … {batch[-1]['id']}）\n")
        lines.append("| 抽查条目 | 来源数 | 已核验 | 待核实标注 | 结论 |")
        lines.append("|---|---|---|---|---|")
        for e in sample:
            srcs = [sources.get(x) for x in e["sources"]]
            verified = sum(1 for s in srcs if s and s.get("verified"))
            pending = "是" if e.get("needs_verification") else "否"
            ok = verified >= 1 and (verified >= 2 or e.get("needs_verification"))
            if not ok:
                total_fail += 1
            lines.append(f"| {e['id']} | {len(srcs)} | {verified} | {pending} | {'通过' if ok else '不合格'} |")
        lines.append("")
    lines.append(f"## 结论\n\n- 抽查批次：{len(batches)}；抽查条目：{sum(min(4,len(b)) for b in batches)}")
    lines.append(f"- 不合格：{total_fail}；整体结论：{'通过' if total_fail == 0 else '需返工'}")
    lines.append("- 说明：本抽查核对的是 `sources.json` 中已完成的逐条链接核验记录与条目引用关系；具体页面内容仍需按来源页人工复核。")
    open(os.path.join(ROOT, "SPOTCHECK.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("spotcheck done", "fail", total_fail)


if __name__ == "__main__":
    main()
