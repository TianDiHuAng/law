# -*- coding: utf-8 -*-
"""R60 体检轮附加升级：2 个经典案例。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R60 = {
    "case-qiyuling": dict(
        definition_source="山东省高级人民法院二审（2001年）；最高人民法院相关批复（案号与批复原文待核实，核对日期：2026-11-24）。",
        elements=["受教育权性质", "姓名权侵权手段", "民事责任承担", "宪法基本权利第三人效力"],
        conditions=["存在冒名顶替致他人受教育权受损的事实", "以侵犯姓名权为手段", "受害人提起民事诉讼"],
        effects=["侵权人承担民事责任", "引发宪法司法化的学理讨论", "相关批复后经清理废止"],
        exceptions=["宪法基本权利一般不直接作为民事裁判依据", "基本权利实现主要依赖立法与宪法监督机制"],
        cases=["case-luzhou"],
        controversies=[dict(issue="宪法基本权利能否在民事案件中直接适用",
                            views=[dict(holder="间接效力说（主流）", basis="基本权利通过民法概括条款间接影响私法关系"),
                                   dict(holder="直接适用说（该案批复思路）", basis="法院可直接援引宪法基本权利裁判民事案件")])],
        distinctions=[D("受教育权", "宪法基本权利"), D("姓名权", "具体人格权")],
        misconceptions=[dict(claim="宪法不能影响民事裁判", correction="宪法可通过概括条款产生间接效力"),
                        dict(claim="本案批复仍现行有效", correction="相关批复已被清理废止，宪法实施依现行制度")],
    ),
    "case-luzhou": dict(
        definition_source="四川省泸州市中级人民法院二审（2001年，案号待核实，核对日期：2026-11-24）。",
        elements=["遗嘱自由", "公序良俗", "遗赠效力", "道德评价与法律效力"],
        conditions=["遗嘱形式上有效", "遗嘱内容涉及婚外同居关系", "受遗赠人主张受赠"],
        effects=["法院以违背公序良俗认定遗嘱无效", "引发遗嘱自由与伦理秩序关系的讨论", "影响后续公序良俗条款的适用"],
        exceptions=["遗嘱自由受法律保护，公序良俗的限制应审慎适用", "纯粹道德评价不当然否定法律行为效力"],
        cases=["case-qiyuling"],
        controversies=[dict(issue="违背道德风尚的遗赠是否一律无效",
                            views=[dict(holder="公序良俗限制说（该案立场）", basis="遗嘱将财产赠与婚外同居者违背公序良俗，应认定无效"),
                                   dict(holder="遗嘱自由优先说（部分学者）", basis="应尊重遗嘱自由，区分道德评价与法律效力")])],
        distinctions=[D("遗嘱继承", "依遗嘱指定继承人"), D("遗赠", "将财产赠与法定继承人以外的人")],
        misconceptions=[dict(claim="遗嘱只要形式合法就有效", correction="内容违背公序良俗或强制性规定的遗嘱无效"),
                        dict(claim="道德不端必然导致遗嘱无效", correction="须结合公序良俗的具体内涵审慎判断")],
    ),
}