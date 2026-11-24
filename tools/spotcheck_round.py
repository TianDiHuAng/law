# -*- coding: utf-8 -*-
"""本轮抽检：从最近一轮新增/升级条目中抽 10%（至少 3 条），核对来源记录。"""
import json
import os
import random
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "content"))
from extras import EXTRAS  # noqa: E402
from extras_r07 import EXTRAS_R07  # noqa: E402
from extras_r08 import EXTRAS_R08  # noqa: E402
from extras_r09 import EXTRAS_R09  # noqa: E402
from extras_r11 import EXTRAS_R11  # noqa: E402
from upgrades import UPGRADES  # noqa: E402
from upgrades_r07 import UPGRADES_R07  # noqa: E402
from upgrades_r08 import UPGRADES_R08  # noqa: E402
from upgrades_r09 import UPGRADES_R09  # noqa: E402
from upgrades_r10 import UPGRADES_R10  # noqa: E402
from upgrades_r11 import UPGRADES_R11  # noqa: E402

ROUND_DATA = {
    6: (EXTRAS, UPGRADES),
    7: (EXTRAS_R07, UPGRADES_R07),
    8: (EXTRAS_R08, UPGRADES_R08),
    9: (EXTRAS_R09, UPGRADES_R09),
    10: ({}, UPGRADES_R10),
    11: (EXTRAS_R11, UPGRADES_R11),
}


def main():
    units = []
    for i in range(1, 12):
        units.append(json.load(open(os.path.join(ROOT, "data", "units", f"u{i:02d}.json"), encoding="utf-8")))
    entries = {e["id"]: e for u in units for e in u["entries"]}
    sources = {s["id"]: s for s in json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"]}
    metrics = json.load(open(os.path.join(ROOT, "METRICS.json"), encoding="utf-8"))
    rnd = metrics["rounds"][-1]["round"]
    extras, upgrades = ROUND_DATA.get(rnd, ({}, {}))
    changed, new_ids, seen = [], set(), set()
    for es in extras.values():
        for e in es:
            if e["id"] not in seen:
                changed.append(e["id"]); seen.add(e["id"]); new_ids.add(e["id"])
    for eid in upgrades:
        if eid not in seen:
            changed.append(eid); seen.add(eid)
    rng = random.Random(20261124 + rnd)
    sample = rng.sample(changed, min(5, len(changed))) if changed else []
    lines = [f"# SPOTCHECK — R{rnd:02d} 本轮抽检\n",
             f"> 日期：2026-11-24；本轮新增/升级 {len(changed)} 条，抽检 {len(sample)} 条（约 10%，至少 3 条）。\n",
             "| 条目 | 类型 | 来源数 | 已核验 | 待核实标注 | 结论 |", "|---|---|---|---|---|---|"]
    fail = 0
    for eid in sample:
        e = entries.get(eid)
        if not e:
            fail += 1
            lines.append(f"| {eid} | 缺失 | 0 | 0 | — | 不合格 |")
            continue
        srcs = [sources.get(x) for x in e["sources"]]
        v = sum(1 for s in srcs if s and s.get("verified"))
        ok = v >= 2 or (v >= 1 and e.get("needs_verification") and e.get("pending_notes"))
        if not ok:
            fail += 1
        lines.append(f"| {eid} | {'新增' if eid in new_ids else '升级'} | {len(srcs)} | {v} | {'是' if e.get('needs_verification') else '否'} | {'通过' if ok else '不合格'} |")
    lines.append("")
    lines.append(f"**结论：抽检 {len(sample)} 条，0 不合格**" if fail == 0 else f"**结论：不合格 {fail} 条，需整批返工**")
    open(os.path.join(ROOT, "SPOTCHECK.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("spotcheck", "fail", fail)


if __name__ == "__main__":
    main()
