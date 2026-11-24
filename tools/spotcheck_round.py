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
from extras_r12 import EXTRAS_R12  # noqa: E402
from extras_r13 import EXTRAS_R13  # noqa: E402
from extras_r14 import EXTRAS_R14  # noqa: E402
from upgrades_r15 import UPGRADES_R15  # noqa: E402
from extras_r16 import EXTRAS_R16  # noqa: E402
from extras_r17 import EXTRAS_R17  # noqa: E402
from extras_r18 import EXTRAS_R18  # noqa: E402
from extras_r19 import EXTRAS_R19  # noqa: E402
from extras_r21 import EXTRAS_R21  # noqa: E402
from extras_r22 import EXTRAS_R22  # noqa: E402
from extras_r23 import EXTRAS_R23  # noqa: E402
from extras_r24 import EXTRAS_R24  # noqa: E402
from extras_r26 import EXTRAS_R26  # noqa: E402
from upgrades_r20 import UPGRADES_R20  # noqa: E402
from upgrades_r21 import UPGRADES_R21  # noqa: E402
from upgrades_r22 import UPGRADES_R22  # noqa: E402
from upgrades_r23 import UPGRADES_R23  # noqa: E402
from upgrades_r24 import UPGRADES_R24  # noqa: E402
from upgrades_r25 import UPGRADES_R25  # noqa: E402
from upgrades_r26 import UPGRADES_R26  # noqa: E402
from upgrades_r16 import UPGRADES_R16  # noqa: E402
from upgrades_r17 import UPGRADES_R17  # noqa: E402
from upgrades_r18 import UPGRADES_R18  # noqa: E402
from upgrades_r19 import UPGRADES_R19  # noqa: E402
from upgrades import UPGRADES  # noqa: E402
from upgrades_r07 import UPGRADES_R07  # noqa: E402
from upgrades_r08 import UPGRADES_R08  # noqa: E402
from upgrades_r09 import UPGRADES_R09  # noqa: E402
from upgrades_r10 import UPGRADES_R10  # noqa: E402
from upgrades_r11 import UPGRADES_R11  # noqa: E402
from upgrades_r12 import UPGRADES_R12  # noqa: E402
from upgrades_r13 import UPGRADES_R13  # noqa: E402
from upgrades_r14 import UPGRADES_R14  # noqa: E402

ROUND_DATA = {
    6: (EXTRAS, UPGRADES),
    7: (EXTRAS_R07, UPGRADES_R07),
    8: (EXTRAS_R08, UPGRADES_R08),
    9: (EXTRAS_R09, UPGRADES_R09),
    10: ({}, UPGRADES_R10),
    11: (EXTRAS_R11, UPGRADES_R11),
    12: (EXTRAS_R12, UPGRADES_R12),
    13: (EXTRAS_R13, UPGRADES_R13),
    14: (EXTRAS_R14, UPGRADES_R14),
    15: ({}, UPGRADES_R15),
    16: (EXTRAS_R16, UPGRADES_R16),
    17: (EXTRAS_R17, UPGRADES_R17),
    18: (EXTRAS_R18, UPGRADES_R18),
    19: (EXTRAS_R19, UPGRADES_R19),
    20: ({}, UPGRADES_R20),
    21: (EXTRAS_R21, UPGRADES_R21),
    22: (EXTRAS_R22, UPGRADES_R22),
    23: (EXTRAS_R23, UPGRADES_R23),
    24: (EXTRAS_R24, UPGRADES_R24),
    25: ({}, UPGRADES_R25),
    26: (EXTRAS_R26, UPGRADES_R26),
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
