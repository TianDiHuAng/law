# -*- coding: utf-8 -*-
"""R45 体检轮附加升级：2 条条目。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R45 = {
    "intl-law-of-sea": dict(
        definition_source="《联合国海洋法公约》（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["内水", "领海", "毗连区", "专属经济区", "大陆架", "公海", "国际海底区域"],
        conditions=["沿海国依公约主张相应海域权利", "海域划界须依公平原则与相关情况协议解决"],
        effects=["沿海国在相应海域享有主权、主权权利或管辖权", "他国享有航行、飞越与铺设电缆等权利", "争端可通过公约第十五部分解决"],
        exceptions=["用于国际航行的海峡适用过境通行制", "群岛水域制度适用于群岛国"],
        cases=[],
        controversies=[dict(issue="专属经济区内的军事活动",
                            views=[dict(holder="自由使用说", basis="专属经济区不属于领海，他国享有航行飞越自由"),
                                   dict(holder="沿海国安全关切说（部分观点）", basis="军事测量等活动应顾及沿海国安全利益")])],
        distinctions=[D("领海", "沿海国主权及于水域与上空"), D("专属经济区", "沿海国享有资源主权权利")],
        misconceptions=[dict(claim="领海是无限制的主权水域", correction="外国船舶享有无害通过权"),
                        dict(claim="公海无人管辖", correction="公海受船旗国管辖并受公约一般义务约束")],
    ),
    "intl-international-criminal": dict(
        definition_source="《罗马规约》及国际刑事法庭实践（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["灭绝种族罪", "危害人类罪", "战争罪", "侵略罪", "个人刑事责任"],
        conditions=["行为符合犯罪构成要件", "具有故意与明知", "不属于职务行为豁免范围"],
        effects=["个人承担刑事责任", "指挥官与上级可能承担指挥责任", "国家承担合作与惩治义务"],
        exceptions=["官方身份不免除刑事责任", "上级命令不当然免除责任（明显违法时）"],
        cases=[],
        controversies=[dict(issue="侵略罪的管辖启动条件",
                            views=[dict(holder="安理会前置说（规约安排）", basis="侵略罪管辖在特定情形下需安理会认定"),
                                   dict(holder="缔约国大会授权说（部分观点）", basis="应允许缔约国大会在安理会不作为时授权调查")])],
        distinctions=[D("国际刑法", "个人刑事责任"), D("国家责任", "国家违反国际义务的责任")],
        misconceptions=[dict(claim="国家元首可以豁免国际刑事责任", correction="官方身份不免除国际刑事法院的管辖权"),
                        dict(claim="国际刑法只适用于战争时期", correction="危害人类罪可发生在平时")],
    ),
}