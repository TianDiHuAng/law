# -*- coding: utf-8 -*-
"""把 content/uNN.py 汇总为 data/units/*.json、scope.md、coverage.json。"""
import importlib
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import date

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
from extras_r31 import EXTRAS_R31  # noqa: E402
from extras_r32 import EXTRAS_R32  # noqa: E402
from extras_r33 import EXTRAS_R33  # noqa: E402
from extras_r34 import EXTRAS_R34  # noqa: E402
from extras_r36 import EXTRAS_R36  # noqa: E402
from extras_r37 import EXTRAS_R37  # noqa: E402
from extras_r38 import EXTRAS_R38  # noqa: E402
from extras_r39 import EXTRAS_R39  # noqa: E402
from extras_r41 import EXTRAS_R41  # noqa: E402
from extras_r42 import EXTRAS_R42  # noqa: E402
from extras_r43 import EXTRAS_R43  # noqa: E402
from extras_r44 import EXTRAS_R44  # noqa: E402
from extras_r46 import EXTRAS_R46  # noqa: E402
from extras_r47 import EXTRAS_R47  # noqa: E402
from extras_r48 import EXTRAS_R48  # noqa: E402
from extras_r49 import EXTRAS_R49  # noqa: E402
from extras_r51 import EXTRAS_R51  # noqa: E402
from extras_r52 import EXTRAS_R52  # noqa: E402
from extras_r53 import EXTRAS_R53  # noqa: E402
from extras_r54 import EXTRAS_R54  # noqa: E402
from extras_r56 import EXTRAS_R56  # noqa: E402
from extras_r57 import EXTRAS_R57  # noqa: E402
from extras_r58 import EXTRAS_R58  # noqa: E402
from upgrades import UPGRADES  # noqa: E402
from upgrades_r07 import UPGRADES_R07  # noqa: E402
from upgrades_r08 import UPGRADES_R08  # noqa: E402
from upgrades_r09 import UPGRADES_R09  # noqa: E402
from upgrades_r10 import UPGRADES_R10  # noqa: E402
from upgrades_r11 import UPGRADES_R11  # noqa: E402
from upgrades_r12 import UPGRADES_R12  # noqa: E402
from upgrades_r13 import UPGRADES_R13  # noqa: E402
from upgrades_r14 import UPGRADES_R14  # noqa: E402
from upgrades_r15 import UPGRADES_R15  # noqa: E402
from upgrades_r16 import UPGRADES_R16  # noqa: E402
from upgrades_r17 import UPGRADES_R17  # noqa: E402
from upgrades_r18 import UPGRADES_R18  # noqa: E402
from upgrades_r19 import UPGRADES_R19  # noqa: E402
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
from upgrades_r31 import UPGRADES_R31  # noqa: E402
from upgrades_r32 import UPGRADES_R32  # noqa: E402
from upgrades_r33 import UPGRADES_R33  # noqa: E402
from upgrades_r34 import UPGRADES_R34  # noqa: E402
from upgrades_r35 import UPGRADES_R35  # noqa: E402
from upgrades_r36 import UPGRADES_R36  # noqa: E402
from upgrades_r37 import UPGRADES_R37  # noqa: E402
from upgrades_r38 import UPGRADES_R38  # noqa: E402
from upgrades_r39 import UPGRADES_R39  # noqa: E402
from upgrades_r40 import UPGRADES_R40  # noqa: E402
from upgrades_r41 import UPGRADES_R41  # noqa: E402
from upgrades_r42 import UPGRADES_R42  # noqa: E402
from upgrades_r43 import UPGRADES_R43  # noqa: E402
from upgrades_r44 import UPGRADES_R44  # noqa: E402
from upgrades_r45 import UPGRADES_R45  # noqa: E402
from upgrades_r46 import UPGRADES_R46  # noqa: E402
from upgrades_r47 import UPGRADES_R47  # noqa: E402
from upgrades_r48 import UPGRADES_R48  # noqa: E402
from upgrades_r49 import UPGRADES_R49  # noqa: E402
from upgrades_r50 import UPGRADES_R50  # noqa: E402
from upgrades_r51 import UPGRADES_R51  # noqa: E402
from upgrades_r52 import UPGRADES_R52  # noqa: E402
from upgrades_r53 import UPGRADES_R53  # noqa: E402
from upgrades_r54 import UPGRADES_R54  # noqa: E402
from upgrades_r55 import UPGRADES_R55  # noqa: E402
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

TODAY = "2026-11-24"
OUTLINE_A = "教育部《普通高等学校法学类本科专业教学质量国家标准》（2018）"
OUTLINE_B = "司法部《2025年国家统一法律职业资格考试大纲》"
OUTLINE_C = "《中国大百科全书（第三版）·法学》"
OUTLINE_D = "国家法律法规数据库法律分类"

OUTLINE_BY_TYPE = {
    "concept": [OUTLINE_A, OUTLINE_C],
    "case": [OUTLINE_B, OUTLINE_D],
    "law": [OUTLINE_A, OUTLINE_D],
    "flow": [OUTLINE_B, OUTLINE_D],
}

TYPE_LABEL = {"concept": "概念制度", "case": "案例", "law": "文本导读", "flow": "流程"}


def main():
    sources = json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"]
    verified = {s["id"] for s in sources if s.get("verified")}
    source_map = {s["id"]: s for s in sources}

    units = []
    for i in range(1, 12):
        mod = importlib.import_module(f"u{i:02d}")
        units.append(mod.U)

    # 挂载本轮新增条目与升级内容
    for unit in units:
        unit["entries"].extend(EXTRAS.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R07.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R08.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R09.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R11.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R12.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R13.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R14.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R16.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R17.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R18.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R19.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R21.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R22.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R23.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R24.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R26.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R27.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R28.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R29.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R31.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R32.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R33.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R34.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R36.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R37.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R38.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R39.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R41.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R42.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R43.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R44.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R46.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R47.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R48.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R49.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R51.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R52.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R53.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R54.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R56.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R57.get(unit["unit_id"], []))
        unit["entries"].extend(EXTRAS_R58.get(unit["unit_id"], []))
    for unit in units:
        for e in unit["entries"]:
            if e["id"] in UPGRADES:
                e["l2"] = UPGRADES[e["id"]]
            if e["id"] in UPGRADES_R07:
                e["l2"] = UPGRADES_R07[e["id"]]
            if e["id"] in UPGRADES_R08:
                e["l2"] = UPGRADES_R08[e["id"]]
            if e["id"] in UPGRADES_R09:
                e["l2"] = UPGRADES_R09[e["id"]]
            if e["id"] in UPGRADES_R10:
                e["l2"] = UPGRADES_R10[e["id"]]
            if e["id"] in UPGRADES_R11:
                e["l2"] = UPGRADES_R11[e["id"]]
            if e["id"] in UPGRADES_R12:
                e["l2"] = UPGRADES_R12[e["id"]]
            if e["id"] in UPGRADES_R13:
                e["l2"] = UPGRADES_R13[e["id"]]
            if e["id"] in UPGRADES_R14:
                e["l2"] = UPGRADES_R14[e["id"]]
            if e["id"] in UPGRADES_R15:
                e["l2"] = UPGRADES_R15[e["id"]]
            if e["id"] in UPGRADES_R16:
                e["l2"] = UPGRADES_R16[e["id"]]
            if e["id"] in UPGRADES_R17:
                e["l2"] = UPGRADES_R17[e["id"]]
            if e["id"] in UPGRADES_R18:
                e["l2"] = UPGRADES_R18[e["id"]]
            if e["id"] in UPGRADES_R19:
                e["l2"] = UPGRADES_R19[e["id"]]
            if e["id"] in UPGRADES_R20:
                e["l2"] = UPGRADES_R20[e["id"]]
            if e["id"] in UPGRADES_R21:
                e["l2"] = UPGRADES_R21[e["id"]]
            if e["id"] in UPGRADES_R22:
                e["l2"] = UPGRADES_R22[e["id"]]
            if e["id"] in UPGRADES_R23:
                e["l2"] = UPGRADES_R23[e["id"]]
            if e["id"] in UPGRADES_R24:
                e["l2"] = UPGRADES_R24[e["id"]]
            if e["id"] in UPGRADES_R25:
                e["l2"] = UPGRADES_R25[e["id"]]
            if e["id"] in UPGRADES_R26:
                e["l2"] = UPGRADES_R26[e["id"]]
            if e["id"] in UPGRADES_R27:
                e["l2"] = UPGRADES_R27[e["id"]]
            if e["id"] in UPGRADES_R28:
                e["l2"] = UPGRADES_R28[e["id"]]
            if e["id"] in UPGRADES_R29:
                e["l2"] = UPGRADES_R29[e["id"]]
            if e["id"] in UPGRADES_R30:
                e["l2"] = UPGRADES_R30[e["id"]]
            if e["id"] in UPGRADES_R31:
                e["l2"] = UPGRADES_R31[e["id"]]
            if e["id"] in UPGRADES_R32:
                e["l2"] = UPGRADES_R32[e["id"]]
            if e["id"] in UPGRADES_R33:
                e["l2"] = UPGRADES_R33[e["id"]]
            if e["id"] in UPGRADES_R34:
                e["l2"] = UPGRADES_R34[e["id"]]
            if e["id"] in UPGRADES_R35:
                e["l2"] = UPGRADES_R35[e["id"]]
            if e["id"] in UPGRADES_R36:
                e["l2"] = UPGRADES_R36[e["id"]]
            if e["id"] in UPGRADES_R37:
                e["l2"] = UPGRADES_R37[e["id"]]
            if e["id"] in UPGRADES_R38:
                e["l2"] = UPGRADES_R38[e["id"]]
            if e["id"] in UPGRADES_R39:
                e["l2"] = UPGRADES_R39[e["id"]]
            if e["id"] in UPGRADES_R40:
                e["l2"] = UPGRADES_R40[e["id"]]
            if e["id"] in UPGRADES_R41:
                e["l2"] = UPGRADES_R41[e["id"]]
            if e["id"] in UPGRADES_R42:
                e["l2"] = UPGRADES_R42[e["id"]]
            if e["id"] in UPGRADES_R43:
                e["l2"] = UPGRADES_R43[e["id"]]
            if e["id"] in UPGRADES_R44:
                e["l2"] = UPGRADES_R44[e["id"]]
            if e["id"] in UPGRADES_R45:
                e["l2"] = UPGRADES_R45[e["id"]]
            if e["id"] in UPGRADES_R46:
                e["l2"] = UPGRADES_R46[e["id"]]
            if e["id"] in UPGRADES_R47:
                e["l2"] = UPGRADES_R47[e["id"]]
            if e["id"] in UPGRADES_R48:
                e["l2"] = UPGRADES_R48[e["id"]]
            if e["id"] in UPGRADES_R49:
                e["l2"] = UPGRADES_R49[e["id"]]
            if e["id"] in UPGRADES_R50:
                e["l2"] = UPGRADES_R50[e["id"]]
            if e["id"] in UPGRADES_R51:
                e["l2"] = UPGRADES_R51[e["id"]]
            if e["id"] in UPGRADES_R52:
                e["l2"] = UPGRADES_R52[e["id"]]
            if e["id"] in UPGRADES_R53:
                e["l2"] = UPGRADES_R53[e["id"]]
            if e["id"] in UPGRADES_R54:
                e["l2"] = UPGRADES_R54[e["id"]]
            if e["id"] in UPGRADES_R55:
                e["l2"] = UPGRADES_R55[e["id"]]
            if e["id"] in UPGRADES_R56:
                e["l2"] = UPGRADES_R56[e["id"]]
            if e["id"] in UPGRADES_R57:
                e["l2"] = UPGRADES_R57[e["id"]]
            if e["id"] in UPGRADES_R58:
                e["l2"] = UPGRADES_R58[e["id"]]
            if e["id"] in UPGRADES_R59:
                e["l2"] = UPGRADES_R59[e["id"]]
            if e["id"] in UPGRADES_R60:
                e["l2"] = UPGRADES_R60[e["id"]]
            if e["id"] in UPGRADES_R61:
                e["l2"] = UPGRADES_R61[e["id"]]
            if e["id"] in UPGRADES_R62:
                e["l2"] = UPGRADES_R62[e["id"]]
            if e["id"] in UPGRADES_R63:
                e["l2"] = UPGRADES_R63[e["id"]]
            if e["id"] in UPGRADES_R64:
                e["l2"] = UPGRADES_R64[e["id"]]
            if e["id"] in UPGRADES_R65:
                e["l2"] = UPGRADES_R65[e["id"]]
            if e["id"] in UPGRADES_R66:
                e["l2"] = UPGRADES_R66[e["id"]]
            if e["id"] in UPGRADES_R67:
                e["l2"] = UPGRADES_R67[e["id"]]
            if e["id"] in UPGRADES_R68:
                e["l2"] = UPGRADES_R68[e["id"]]
            if e["id"] in UPGRADES_R69:
                e["l2"] = UPGRADES_R69[e["id"]]
            if e["id"] in UPGRADES_R70:
                e["l2"] = UPGRADES_R70[e["id"]]
            if e["id"] in UPGRADES_R71:
                e["l2"] = UPGRADES_R71[e["id"]]
            if e["id"] in UPGRADES_R72:
                e["l2"] = UPGRADES_R72[e["id"]]
            if e["id"] in UPGRADES_R73:
                e["l2"] = UPGRADES_R73[e["id"]]
            if e["id"] in UPGRADES_R74:
                e["l2"] = UPGRADES_R74[e["id"]]
            if e["id"] in UPGRADES_R75:
                e["l2"] = UPGRADES_R75[e["id"]]
            if e["id"] in UPGRADES_R76:
                e["l2"] = UPGRADES_R76[e["id"]]
            if e["id"] in L3_UPGRADES_R77:
                e["l3"] = L3_UPGRADES_R77[e["id"]]
            if e["id"] in L3_UPGRADES_R78:
                e["l3"] = L3_UPGRADES_R78[e["id"]]
            if e["id"] in L3_UPGRADES_R79:
                e["l3"] = L3_UPGRADES_R79[e["id"]]
            if e["id"] in L3_UPGRADES_R80:
                e["l3"] = L3_UPGRADES_R80[e["id"]]
            if e["id"] in L3_UPGRADES_R81:
                e["l3"] = L3_UPGRADES_R81[e["id"]]
            if e["id"] in L3_UPGRADES_R82:
                e["l3"] = L3_UPGRADES_R82[e["id"]]
            if e["id"] in L3_UPGRADES_R83:
                e["l3"] = L3_UPGRADES_R83[e["id"]]
            if e["id"] in L3_UPGRADES_R84:
                e["l3"] = L3_UPGRADES_R84[e["id"]]
            if e["id"] in L3_UPGRADES_R85:
                e["l3"] = L3_UPGRADES_R85[e["id"]]
            if e["id"] in L3_UPGRADES_R86:
                e["l3"] = L3_UPGRADES_R86[e["id"]]
            if e["id"] in L3_UPGRADES_R87:
                e["l3"] = L3_UPGRADES_R87[e["id"]]
            if e["id"] in L3_UPGRADES_R88:
                e["l3"] = L3_UPGRADES_R88[e["id"]]
            if e["id"] in L3_UPGRADES_R89:
                e["l3"] = L3_UPGRADES_R89[e["id"]]
            if e["id"] in L3_UPGRADES_R90:
                e["l3"] = L3_UPGRADES_R90[e["id"]]
            if e["id"] in L3_UPGRADES_R91:
                e["l3"] = L3_UPGRADES_R91[e["id"]]
            if e["id"] in L3_UPGRADES_R92:
                e["l3"] = L3_UPGRADES_R92[e["id"]]
            if e["id"] in L3_UPGRADES_R93:
                e["l3"] = L3_UPGRADES_R93[e["id"]]
            if e["id"] in L3_UPGRADES_R94:
                e["l3"] = L3_UPGRADES_R94[e["id"]]
            if e["id"] in L3_UPGRADES_R95:
                e["l3"] = L3_UPGRADES_R95[e["id"]]
            if e["id"] in L3_UPGRADES_R96:
                e["l3"] = L3_UPGRADES_R96[e["id"]]
            if e["id"] in L3_UPGRADES_R97:
                e["l3"] = L3_UPGRADES_R97[e["id"]]
            if e["id"] in L3_UPGRADES_R98:
                e["l3"] = L3_UPGRADES_R98[e["id"]]
            if e["id"] in L3_UPGRADES_R99:
                e["l3"] = L3_UPGRADES_R99[e["id"]]
            if e["id"] in L3_UPGRADES_R100:
                e["l3"] = L3_UPGRADES_R100[e["id"]]
            if e["id"] in L3_UPGRADES_R101:
                e["l3"] = L3_UPGRADES_R101[e["id"]]
            if e["id"] in L3_UPGRADES_R102:
                e["l3"] = L3_UPGRADES_R102[e["id"]]

    ids, titles = {}, {}
    entries_all = []
    errors = []
    for unit in units:
        for e in unit["entries"]:
            if e["id"] in ids:
                errors.append(f"duplicate id {e['id']}")
            ids[e["id"]] = e
            if e["title"] in titles:
                errors.append(f"duplicate title {e['title']}")
            titles[e["title"]] = e
            e["unit_id"] = unit["unit_id"]
            e["unit_title"] = unit["title"]
            e["outline_sources"] = OUTLINE_BY_TYPE[e["type"]]
            e["status"] = "L3" if e.get("l3") else ("L2" if e.get("l2") else "L1")
            if e["type"] == "law" and e.get("law"):
                e["legal_status"] = e["law"].get("status", "待复核")
                e["checked_date"] = e["law"].get("checked_date", TODAY)
            else:
                e["legal_status"] = "制度/案例条目（以现行法为背景）"
                e["checked_date"] = TODAY
            for sid in e["sources"]:
                if sid not in verified:
                    errors.append(f"{e['id']} cites unverified/missing source {sid}")
            if len(e["sources"]) < 2 and not e.get("needs_verification"):
                errors.append(f"{e['id']} has <2 sources but no verification flag")
            if e["type"] == "case" and not e.get("case"):
                errors.append(f"{e['id']} case entry missing case dict")
            if e["type"] == "law" and not e.get("law"):
                errors.append(f"{e['id']} law entry missing law dict")
            if e["type"] == "flow" and not e.get("flow"):
                errors.append(f"{e['id']} flow entry missing flow dict")
            entries_all.append(e)

    # related 自动补齐
    by_unit = defaultdict(list)
    for e in entries_all:
        by_unit[e["unit_id"]].append(e)
    for unit_id, es in by_unit.items():
        for e in es:
            rel = [r for r in e["related"] if r in ids and r != e["id"]]
            if len(rel) < 2:
                for other in es:
                    if other["id"] != e["id"] and other["id"] not in rel:
                        rel.append(other["id"])
                    if len(rel) >= 3:
                        break
            e["related"] = rel[:4]
    for e in entries_all:
        for r in e["related"]:
            if r not in ids:
                errors.append(f"{e['id']} related missing {r}")

    if errors:
        print("BUILD ERRORS:")
        for x in errors:
            print(" -", x)
        sys.exit(1)

    os.makedirs(os.path.join(ROOT, "data", "units"), exist_ok=True)
    for unit in units:
        with open(os.path.join(ROOT, "data", "units", f"{unit['unit_id']}.json"), "w", encoding="utf-8") as f:
            json.dump(unit, f, ensure_ascii=False, indent=2)

    # coverage
    level_counts = Counter(e["status"] for e in entries_all)
    matrix = {}
    core_l2 = {}
    for unit in units:
        uid = unit["unit_id"]
        es = [e for e in entries_all if e["unit_id"] == uid]
        m = defaultdict(Counter)
        for e in es:
            m[e["jurisdiction"]][TYPE_LABEL[e["type"]]] += 1
            m[e["jurisdiction"]]["合计"] += 1
        cross = {}
        for e in es:
            cross.setdefault(e["jurisdiction"], Counter())[TYPE_LABEL[e["type"]]] += 1
        matrix[uid] = {
            "title": unit["title"],
            "by_jurisdiction": {k: dict(v) for k, v in m.items()},
            "by_type": dict(Counter(TYPE_LABEL[e["type"]] for e in es)),
            "cross": {k: dict(v) for k, v in cross.items()},
            "total": len(es),
        }
        core_items = [e for e in es if e["importance"] == "核心" and e["type"] != "flow"]
        core_l2[uid] = (all(e["status"] in ("L2", "L3") for e in core_items) if core_items else None)

    coverage = {
        "generated": TODAY,
        "total": len(entries_all),
        "levels": {k: level_counts.get(k, 0) for k in ("L1", "L2", "L3")},
        "core_l2_coverage": core_l2,
        "matrix": matrix,
        "entries": [
            {
                "id": e["id"], "title": e["title"], "unit": e["unit_id"], "type": TYPE_LABEL[e["type"]],
                "importance": e["importance"], "level": e["status"], "status": "done",
                "source_count": len(e["sources"]),
                "verified_source_count": sum(1 for s in e["sources"] if s in verified),
                "unverified_count": (1 if e.get("needs_verification") else 0),
                "pending_notes": e.get("pending_notes", ""),
                "last_updated": TODAY,
            }
            for e in entries_all
        ],
    }
    with open(os.path.join(ROOT, "coverage.json"), "w", encoding="utf-8") as f:
        json.dump(coverage, f, ensure_ascii=False, indent=2)

    # scope.md
    lines = []
    lines.append("# scope.md — 入选清单与范围说明\n")
    lines.append("> 本清单由四份权威大纲/目录取并集后，按法学知识体系整理。每条标注层级与大纲来源；"
                 "层级是编辑投入优先级，不代表法律效力等级。\n")
    lines.append("## 一、对照的大纲与目录\n")
    lines.append("| 代号 | 大纲/目录 | 用途 | 链接 |")
    lines.append("|---|---|---|---|")
    lines.append(f"| A | {OUTLINE_A} | 本科法学专业核心课程与知识领域 | [来源](https://fxjyzx.cupl.edu.cn/info/1042/1437.htm) |")
    lines.append(f"| B | {OUTLINE_B} | 法律职业资格考试部门法范围 | [来源](https://www.moj.gov.cn/pub/sfbgw/gwxw/xwyw/202505/t20250515_519393.html) |")
    lines.append(f"| C | {OUTLINE_C} | 法学学科分支与概念体系 | [来源](https://www.zgbk.com/) |")
    lines.append(f"| D | {OUTLINE_D} | 现行法律分类与法规名称 | [来源](https://flk.npc.gov.cn/) |")
    lines.append("\n> 说明：表中的 A/B/C/D 表示该条目所属知识领域在对应大纲/目录中有对应分类，不表示逐字同名条目；层级为编辑投入优先级。本清单不是任何单一教材的目录复制，而是按四份来源的共同知识领域取并集后整理；教材、百科与评注有版权，未逐字复制其结构。\n")
    lines.append("\n## 二、层级说明\n")
    lines.append("- **核心**：法学体系的主干制度或基础范畴，优先升 L2，个别升 L3。")
    lines.append("- **重要**：理解主干所必需的制度、程序或案例，保持 L1，条件成熟再升级。")
    lines.append("- **补充**：拓展性、比较法或边缘制度，保持 L1。")
    lines.append("\n## 三、单元与条目\n")
    for unit in units:
        es = [e for e in entries_all if e["unit_id"] == unit["unit_id"]]
        lines.append(f"### {unit['unit_id'].upper()} {unit['title']}（{len(es)} 条）\n")
        lines.append(f"{unit['subtitle']}\n")
        lines.append("| id | 条目 | 类型 | 层级 | 大纲来源 | 辖区 |")
        lines.append("|---|---|---|---|---|---|")
        for e in es:
            srcs = "、".join(["A" if OUTLINE_A in e["outline_sources"] else "",
                              "B" if OUTLINE_B in e["outline_sources"] else "",
                              "C" if OUTLINE_C in e["outline_sources"] else "",
                              "D" if OUTLINE_D in e["outline_sources"] else ""]).replace("、、", "、").strip("、")
            lines.append(f"| {e['id']} | {e['title']} | {TYPE_LABEL[e['type']]} | {e['importance']} | {srcs} | {e['jurisdiction']} |")
        lines.append("")
    lines.append("## 四、范围边界\n")
    lines.append("- 以中国大陆现行法为主，比较法与国际法单列；每个条目均标注辖区。")
    lines.append("- 不收录纯政治学、纯管理学内容；不针对具体个案提供结论或操作建议。")
    lines.append("- 教材、评注、案例汇编仅作参考，不复制其结构或大段文字；所有图示为自制 SVG。")
    lines.append("\n## 五、覆盖统计\n")
    lines.append(f"- 总条目：{len(entries_all)}")
    lines.append(f"- L1：{level_counts.get('L1', 0)}；L2：{level_counts.get('L2', 0)}；L3：{level_counts.get('L3', 0)}")
    lines.append(f"- 核心条目全部达到 L2 及以上的单元：{sum(1 for v in core_l2.values() if v)}/{len(core_l2)}")
    with open(os.path.join(ROOT, "scope.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"build ok: {len(entries_all)} entries, levels={dict(level_counts)}")
    print("units:", {u['unit_id']: len([e for e in entries_all if e['unit_id']==u['unit_id']]) for u in units})


if __name__ == "__main__":
    main()
