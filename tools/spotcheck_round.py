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
from extras_r27 import EXTRAS_R27  # noqa: E402
from extras_r28 import EXTRAS_R28  # noqa: E402
from extras_r29 import EXTRAS_R29  # noqa: E402
from upgrades_r20 import UPGRADES_R20  # noqa: E402
from upgrades_r21 import UPGRADES_R21  # noqa: E402
from upgrades_r22 import UPGRADES_R22  # noqa: E402
from upgrades_r23 import UPGRADES_R23  # noqa: E402
from upgrades_r24 import UPGRADES_R24  # noqa: E402
from upgrades_r25 import UPGRADES_R25  # noqa: E402
from upgrades_r26 import UPGRADES_R26  # noqa: E402
from upgrades_r27 import UPGRADES_R27  # noqa: E402
from upgrades_r28 import UPGRADES_R28  # noqa: E402
from upgrades_r29 import UPGRADES_R29  # noqa: E402
from upgrades_r30 import UPGRADES_R30  # noqa: E402
from extras_r31 import EXTRAS_R31  # noqa: E402
from extras_r32 import EXTRAS_R32  # noqa: E402
from extras_r33 import EXTRAS_R33  # noqa: E402
from extras_r34 import EXTRAS_R34  # noqa: E402
from upgrades_r31 import UPGRADES_R31  # noqa: E402
from upgrades_r32 import UPGRADES_R32  # noqa: E402
from upgrades_r33 import UPGRADES_R33  # noqa: E402
from upgrades_r34 import UPGRADES_R34  # noqa: E402
from upgrades_r35 import UPGRADES_R35  # noqa: E402
from extras_r36 import EXTRAS_R36  # noqa: E402
from extras_r37 import EXTRAS_R37  # noqa: E402
from extras_r38 import EXTRAS_R38  # noqa: E402
from extras_r39 import EXTRAS_R39  # noqa: E402
from upgrades_r36 import UPGRADES_R36  # noqa: E402
from upgrades_r37 import UPGRADES_R37  # noqa: E402
from upgrades_r38 import UPGRADES_R38  # noqa: E402
from upgrades_r39 import UPGRADES_R39  # noqa: E402
from upgrades_r40 import UPGRADES_R40  # noqa: E402
from extras_r41 import EXTRAS_R41  # noqa: E402
from extras_r42 import EXTRAS_R42  # noqa: E402
from extras_r43 import EXTRAS_R43  # noqa: E402
from extras_r44 import EXTRAS_R44  # noqa: E402
from upgrades_r41 import UPGRADES_R41  # noqa: E402
from upgrades_r42 import UPGRADES_R42  # noqa: E402
from upgrades_r43 import UPGRADES_R43  # noqa: E402
from upgrades_r44 import UPGRADES_R44  # noqa: E402
from upgrades_r45 import UPGRADES_R45  # noqa: E402
from extras_r46 import EXTRAS_R46  # noqa: E402
from extras_r47 import EXTRAS_R47  # noqa: E402
from extras_r48 import EXTRAS_R48  # noqa: E402
from extras_r49 import EXTRAS_R49  # noqa: E402
from upgrades_r46 import UPGRADES_R46  # noqa: E402
from upgrades_r47 import UPGRADES_R47  # noqa: E402
from upgrades_r48 import UPGRADES_R48  # noqa: E402
from upgrades_r49 import UPGRADES_R49  # noqa: E402
from upgrades_r50 import UPGRADES_R50  # noqa: E402
from extras_r51 import EXTRAS_R51  # noqa: E402
from upgrades_r51 import UPGRADES_R51  # noqa: E402
from extras_r52 import EXTRAS_R52  # noqa: E402
from extras_r53 import EXTRAS_R53  # noqa: E402
from extras_r54 import EXTRAS_R54  # noqa: E402
from upgrades_r52 import UPGRADES_R52  # noqa: E402
from upgrades_r53 import UPGRADES_R53  # noqa: E402
from upgrades_r54 import UPGRADES_R54  # noqa: E402
from upgrades_r55 import UPGRADES_R55  # noqa: E402
from extras_r56 import EXTRAS_R56  # noqa: E402
from extras_r57 import EXTRAS_R57  # noqa: E402
from extras_r58 import EXTRAS_R58  # noqa: E402
from upgrades_r56 import UPGRADES_R56  # noqa: E402
from upgrades_r57 import UPGRADES_R57  # noqa: E402
from upgrades_r58 import UPGRADES_R58  # noqa: E402
from upgrades_r59 import UPGRADES_R59  # noqa: E402
from upgrades_r60 import UPGRADES_R60  # noqa: E402
from upgrades_r61 import UPGRADES_R61  # noqa: E402
from upgrades_r62 import UPGRADES_R62  # noqa: E402
from upgrades_r63 import UPGRADES_R63  # noqa: E402
from upgrades_r64 import UPGRADES_R64  # noqa: E402
from upgrades_r65 import UPGRADES_R65  # noqa: E402
from upgrades_r66 import UPGRADES_R66  # noqa: E402
from upgrades_r67 import UPGRADES_R67  # noqa: E402
from upgrades_r68 import UPGRADES_R68  # noqa: E402
from upgrades_r69 import UPGRADES_R69  # noqa: E402
from upgrades_r70 import UPGRADES_R70  # noqa: E402
from upgrades_r71 import UPGRADES_R71  # noqa: E402
from upgrades_r72 import UPGRADES_R72  # noqa: E402
from upgrades_r73 import UPGRADES_R73  # noqa: E402
from upgrades_r74 import UPGRADES_R74  # noqa: E402
from upgrades_r75 import UPGRADES_R75  # noqa: E402
from upgrades_r76 import UPGRADES_R76  # noqa: E402
from upgrades_r77 import L3_UPGRADES_R77  # noqa: E402
from upgrades_r78 import L3_UPGRADES_R78  # noqa: E402
from upgrades_r79 import L3_UPGRADES_R79  # noqa: E402
from upgrades_r80 import L3_UPGRADES_R80  # noqa: E402
from upgrades_r81 import L3_UPGRADES_R81  # noqa: E402
from upgrades_r82 import L3_UPGRADES_R82  # noqa: E402
from upgrades_r83 import L3_UPGRADES_R83  # noqa: E402
from upgrades_r84 import L3_UPGRADES_R84  # noqa: E402
from upgrades_r85 import L3_UPGRADES_R85  # noqa: E402
from upgrades_r86 import L3_UPGRADES_R86  # noqa: E402
from upgrades_r87 import L3_UPGRADES_R87  # noqa: E402
from upgrades_r88 import L3_UPGRADES_R88  # noqa: E402
from upgrades_r89 import L3_UPGRADES_R89  # noqa: E402
from upgrades_r90 import L3_UPGRADES_R90  # noqa: E402
from upgrades_r91 import L3_UPGRADES_R91  # noqa: E402
from upgrades_r92 import L3_UPGRADES_R92  # noqa: E402
from upgrades_r93 import L3_UPGRADES_R93  # noqa: E402
from upgrades_r94 import L3_UPGRADES_R94  # noqa: E402
from upgrades_r95 import L3_UPGRADES_R95  # noqa: E402
from upgrades_r96 import L3_UPGRADES_R96  # noqa: E402
from upgrades_r97 import L3_UPGRADES_R97  # noqa: E402
from upgrades_r98 import L3_UPGRADES_R98  # noqa: E402
from upgrades_r99 import L3_UPGRADES_R99  # noqa: E402
from upgrades_r100 import L3_UPGRADES_R100  # noqa: E402
from upgrades_r101 import L3_UPGRADES_R101  # noqa: E402
from upgrades_r102 import L3_UPGRADES_R102  # noqa: E402
from upgrades_r103 import L3_UPGRADES_R103  # noqa: E402
from upgrades_r104 import L3_UPGRADES_R104  # noqa: E402
from upgrades_r105 import L3_UPGRADES_R105  # noqa: E402
from upgrades_r106 import L3_UPGRADES_R106  # noqa: E402
from upgrades_r107 import L3_UPGRADES_R107  # noqa: E402
from upgrades_r108 import L3_UPGRADES_R108  # noqa: E402
from upgrades_r109 import L3_UPGRADES_R109  # noqa: E402
from upgrades_r110 import L3_UPGRADES_R110  # noqa: E402
from upgrades_r111 import L3_UPGRADES_R111  # noqa: E402
from upgrades_r112 import L3_UPGRADES_R112  # noqa: E402
from upgrades_r113 import L3_UPGRADES_R113  # noqa: E402
from upgrades_r114 import L3_UPGRADES_R114  # noqa: E402
from upgrades_r115 import L3_UPGRADES_R115  # noqa: E402
from upgrades_r116 import L3_UPGRADES_R116  # noqa: E402
from upgrades_r117 import L3_UPGRADES_R117  # noqa: E402
from upgrades_r118 import L3_UPGRADES_R118  # noqa: E402
from upgrades_r119 import L3_UPGRADES_R119  # noqa: E402
from upgrades_r120 import L3_UPGRADES_R120  # noqa: E402
from upgrades_r121 import L3_UPGRADES_R121  # noqa: E402
from upgrades_r122 import L3_UPGRADES_R122  # noqa: E402
from upgrades_r123 import L3_UPGRADES_R123  # noqa: E402
from upgrades_r124 import L3_UPGRADES_R124  # noqa: E402
from upgrades_r125 import L3_UPGRADES_R125  # noqa: E402
from upgrades_r126 import L3_UPGRADES_R126  # noqa: E402
from upgrades_r127 import L3_UPGRADES_R127  # noqa: E402
from upgrades_r128 import L3_UPGRADES_R128  # noqa: E402
from upgrades_r129 import L3_UPGRADES_R129  # noqa: E402
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
    27: (EXTRAS_R27, UPGRADES_R27),
    28: (EXTRAS_R28, UPGRADES_R28),
    29: (EXTRAS_R29, UPGRADES_R29),
    30: ({}, UPGRADES_R30),
    31: (EXTRAS_R31, UPGRADES_R31),
    32: (EXTRAS_R32, UPGRADES_R32),
    33: (EXTRAS_R33, UPGRADES_R33),
    34: (EXTRAS_R34, UPGRADES_R34),
    35: ({}, UPGRADES_R35),
    36: (EXTRAS_R36, UPGRADES_R36),
    37: (EXTRAS_R37, UPGRADES_R37),
    38: (EXTRAS_R38, UPGRADES_R38),
    39: (EXTRAS_R39, UPGRADES_R39),
    40: ({}, UPGRADES_R40),
    41: (EXTRAS_R41, UPGRADES_R41),
    42: (EXTRAS_R42, UPGRADES_R42),
    43: (EXTRAS_R43, UPGRADES_R43),
    44: (EXTRAS_R44, UPGRADES_R44),
    45: ({}, UPGRADES_R45),
    46: (EXTRAS_R46, UPGRADES_R46),
    47: (EXTRAS_R47, UPGRADES_R47),
    48: (EXTRAS_R48, UPGRADES_R48),
    49: (EXTRAS_R49, UPGRADES_R49),
    50: ({}, UPGRADES_R50),
    51: (EXTRAS_R51, UPGRADES_R51),
    52: (EXTRAS_R52, UPGRADES_R52),
    53: (EXTRAS_R53, UPGRADES_R53),
    54: (EXTRAS_R54, UPGRADES_R54),
    55: ({}, UPGRADES_R55),
    56: (EXTRAS_R56, UPGRADES_R56),
    57: (EXTRAS_R57, UPGRADES_R57),
    58: (EXTRAS_R58, UPGRADES_R58),
    59: ({}, UPGRADES_R59),
    60: ({}, UPGRADES_R60),
    61: ({}, UPGRADES_R61),
    62: ({}, UPGRADES_R62),
    63: ({}, UPGRADES_R63),
    64: ({}, UPGRADES_R64),
    65: ({}, UPGRADES_R65),
    66: ({}, UPGRADES_R66),
    67: ({}, UPGRADES_R67),
    68: ({}, UPGRADES_R68),
    69: ({}, UPGRADES_R69),
    70: ({}, UPGRADES_R70),
    71: ({}, UPGRADES_R71),
    72: ({}, UPGRADES_R72),
    73: ({}, UPGRADES_R73),
    74: ({}, UPGRADES_R74),
    75: ({}, UPGRADES_R75),
    76: ({}, UPGRADES_R76),
    77: ({}, {}),
    78: ({}, {}),
    79: ({}, {}),
    80: ({}, {}),
    81: ({}, {}),
    82: ({}, {}),
    83: ({}, {}),
    84: ({}, {}),
    85: ({}, {}),
    86: ({}, {}),
    87: ({}, {}),
    88: ({}, {}),
    89: ({}, {}),
    90: ({}, {}),
    91: ({}, {}),
    92: ({}, {}),
    93: ({}, {}),
    94: ({}, {}),
    95: ({}, {}),
    96: ({}, {}),
    97: ({}, {}),
    98: ({}, {}),
    99: ({}, {}),
    100: ({}, {}),
    101: ({}, {}),
    102: ({}, {}),
    103: ({}, {}),
    104: ({}, {}),
    105: ({}, {}),
    106: ({}, {}),
    107: ({}, {}),
    108: ({}, {}),
    109: ({}, {}),
    110: ({}, {}),
    111: ({}, {}),
    112: ({}, {}),
    113: ({}, {}),
    114: ({}, {}),
    115: ({}, {}),
    116: ({}, {}),
    117: ({}, {}),
    118: ({}, {}),
    119: ({}, {}),
    120: ({}, {}),
    121: ({}, {}),
    122: ({}, {}),
    123: ({}, {}),
    124: ({}, {}),
    125: ({}, {}),
    126: ({}, {}),
    127: ({}, {}),
    128: ({}, {}),
    129: ({}, {}),
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
