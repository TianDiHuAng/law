# -*- coding: utf-8 -*-
"""R50 体检轮附加升级：2 条条目。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R50 = {
    "data-export-assessment": dict(
        definition_source="《数据出境安全评估办法》及《个人信息保护法》第三十八条（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["申报主体", "申报情形", "申报材料", "评估结果"],
        conditions=["关键信息基础设施运营者向境外提供个人信息或重要数据", "处理个人信息达到规定数量", "国家网信部门规定的其他情形"],
        effects=["评估通过后方可出境", "评估结果有效期内可多次出境", "情形变化应重新申报"],
        exceptions=["未达到申报门槛的可依标准合同或认证出境", "法律、行政法规规定的其他路径"],
        cases=[],
        controversies=[dict(issue="评估门槛与中小企业负担",
                            views=[dict(holder="风险分级说", basis="按数据数量与敏感程度设定门槛，避免一刀切"),
                                   dict(holder="统一评估说（部分观点）", basis="出境风险难以量化，宜统一评估标准")])],
        distinctions=[D("安全评估", "事前风险评估"), D("标准合同", "以合同条款约束出境")],
        misconceptions=[dict(claim="所有个人信息出境都要评估", correction="依数量与类型适用评估、标准合同或认证等不同路径"),
                        dict(claim="评估通过后永久有效", correction="评估结果有有效期，情形变化需重新申报")],
    ),
    "data-cross-border-whitelist": dict(
        definition_source="《个人信息保护法》及数据跨境流动相关监管政策（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["白名单认定", "充分性评估", "适用条件", "动态调整"],
        conditions=["接收方所在国家或地区被认定为具备相当保护水平", "符合监管规定的适用条件"],
        effects=["在白名单内可简化出境合规程序", "仍须履行告知与同意义务", "名单调整后适用规则随之变化"],
        exceptions=["涉及重要数据与关基数据的出境仍须评估", "名单外的仍按一般路径处理"],
        cases=[],
        controversies=[dict(issue="白名单与负面清单的取舍",
                            views=[dict(holder="白名单说", basis="以充分性认定为前提，安全可控"),
                                   dict(holder="负面清单说（部分观点）", basis="以负面清单管理更便利数据流动")])],
        distinctions=[D("白名单", "事前认定可便利出境"), D("安全评估", "逐案风险评估")],
        misconceptions=[dict(claim="进入白名单即可自由出境", correction="仍须满足告知同意与其他法定义务"),
                        dict(claim="中国已建立完整白名单制度", correction="相关制度仍在探索与完善中")],
    ),
}