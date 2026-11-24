# -*- coding: utf-8 -*-
"""R52 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R52 = {
    "data-pi-certification": dict(
        definition_source="《中华人民共和国个人信息保护法》第三十八条及个人信息保护认证相关规则（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["认证机构", "认证标准", "认证程序", "认证效力"],
        conditions=["由具备资质的认证机构实施", "依照国家标准与技术规范评价", "处理者自愿申请或依法要求"],
        effects=["认证可作为合规证明", "可作为个人信息出境的合法路径之一", "认证失效或被撤销后不得继续援引"],
        exceptions=["法律、行政法规另有规定的", "认证不免除处理者的法定义务"],
        cases=[],
        controversies=[dict(issue="认证与安全评估的关系",
                            views=[dict(holder="替代路径说", basis="认证与评估、标准合同并列为出境路径，可择一适用"),
                                   dict(holder="补充路径说（部分观点）", basis="认证应作为评估的补充，不能完全替代")])],
        distinctions=[D("认证", "第三方合规评价"), D("安全评估", "监管机构风险评估")],
        misconceptions=[dict(claim="取得认证就等于完全合规", correction="认证仅证明符合特定标准，不免除法定义务"),
                        dict(claim="任何机构都可以发认证", correction="须由具备资质的认证机构依国家标准实施")],
    ),
    "data-network": dict(
        definition_source="《中华人民共和国网络安全法》（版本：2016年通过，2017年6月1日施行，核对日期：2026-11-24）。",
        elements=["网络运行安全", "网络信息安全", "关键信息基础设施保护", "监测预警与应急处置"],
        conditions=["在境内建设、运营、维护和使用网络", "网络运营者履行安全保护义务", "依法开展等级保护"],
        effects=["运营者承担安全保障责任", "违法收集使用个人信息可能受罚", "关基运营者适用更严格义务"],
        exceptions=["法律、行政法规另有规定的", "为维护国家安全和侦查犯罪依法配合"],
        cases=["case-kuaibo"],
        controversies=[dict(issue="网络实名制与表达自由",
                            views=[dict(holder="实名制必要说", basis="实名有助维护网络秩序与追责"),
                                   dict(holder="比例原则说（部分观点）", basis="实名制对表达自由的限制应最小化")])],
        distinctions=[D("网络安全法", "网络运行与信息安全"), D("数据安全法", "数据处理活动安全")],
        misconceptions=[dict(claim="网络安全只是技术问题", correction="还包括法定义务、责任与监管制度"),
                        dict(claim="只有大型平台受监管", correction="网络运营者普遍承担法定安全义务")],
    ),
    "data-broker-liability": dict(
        definition_source="《个人信息保护法》《数据安全法》关于处理者义务与法律责任的规定（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["数据来源核验", "合法性基础", "安全保障", "责任类型"],
        conditions=["从事数据撮合、加工或交易服务", "处理个人信息或重要数据", "未履行法定义务"],
        effects=["承担民事赔偿责任", "面临行政处罚", "情节严重构成犯罪"],
        exceptions=["已尽合理核验与安全保障义务的可减轻责任", "法律规定的其他免责情形"],
        cases=[],
        controversies=[dict(issue="经纪人的注意义务标准",
                            views=[dict(holder="形式审查说", basis="核验来源声明与授权文件即可"),
                                   dict(holder="实质审查说（部分观点）", basis="应对数据来源合法性进行实质核查")])],
        distinctions=[D("数据处理者", "直接处理个人信息"), D("数据经纪人", "撮合与中介服务")],
        misconceptions=[dict(claim="只是中介不承担合规责任", correction="经纪人同样受个人信息保护与数据安全义务约束"),
                        dict(claim="有卖方承诺即可免责", correction="仍需尽合理核验义务，不能仅依赖对方承诺")],
    ),
    "data-trusted-circulation": dict(
        definition_source="《数据安全法》《个人信息保护法》及可信数据空间相关标准（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["可控流通", "可追溯", "可审计", "技术保障"],
        conditions=["数据流通符合法定条件", "采用可信技术与管理机制", "保障来源者权益"],
        effects=["降低流通风险", "提升数据可用性", "违规流通承担法律责任"],
        exceptions=["法律禁止流通的数据不得流通", "涉及国家秘密的数据依保密规定处理"],
        cases=[],
        controversies=[dict(issue="隐私计算能否替代合规义务",
                            views=[dict(holder="技术补充说", basis="技术可降低风险但不免除告知同意等法定义务"),
                                   dict(holder="技术替代说（部分观点）", basis="在匿名化等技术保障下可适度简化合规程序")])],
        distinctions=[D("可信流通", "技术与治理结合的流通模式"), D("数据开放", "面向社会的数据供给")],
        misconceptions=[dict(claim="用了隐私计算就可以任意共享", correction="技术手段不替代法律义务"),
                        dict(claim="可信流通只适用于大企业", correction="任何规模的数据处理者均可采用")],
    ),
}