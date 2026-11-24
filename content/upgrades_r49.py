# -*- coding: utf-8 -*-
"""R49 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R49 = {
    "data-security-standards": dict(
        definition_source="《中华人民共和国数据安全法》及数据安全国家标准体系（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["基础标准", "技术标准", "管理标准", "评估认证标准"],
        conditions=["标准由标准化技术委员会组织制定", "企业自愿采用或依监管要求适用"],
        effects=["为数据处理者提供合规实施指引", "支撑分类分级、安全评估与认证", "标准与法律冲突时以法律为准"],
        exceptions=["标准属推荐性规范，不直接创设法律责任", "强制性国家标准须依法执行"],
        cases=[],
        controversies=[dict(issue="推荐性标准的实际约束力",
                            views=[dict(holder="软法说", basis="推荐性标准不具强制力，仅提供实施参考"),
                                   dict(holder="事实约束说（部分观点）", basis="监管与司法常以标准判断是否尽到义务，具有事实约束力")])],
        distinctions=[D("法律规范", "具强制约束力"), D("技术标准", "提供技术要求与实施指引")],
        misconceptions=[dict(claim="符合标准就等于合法", correction="标准不能替代法律，仍需满足法律规定的实质义务"),
                        dict(claim="标准只针对技术人员", correction="管理类标准同样约束企业治理与合规流程")],
    ),
    "data-mlps": dict(
        definition_source="《中华人民共和国网络安全法》第二十一条及网络安全等级保护相关国家标准（版本：2016年通过，核对日期：2026-11-24）。",
        elements=["定级", "备案", "安全建设整改", "等级测评", "监督检查"],
        conditions=["网络运营者依网络重要程度定级", "依法向公安机关备案", "按等级落实安全保护措施"],
        effects=["运营者承担等级保护义务", "未履行义务可能被处罚", "关键信息基础设施在等保基础上重点保护"],
        exceptions=["法律、行政法规另有规定的", "涉密网络依保密规定管理"],
        cases=[],
        controversies=[dict(issue="等级保护与关键信息基础设施保护的关系",
                            views=[dict(holder="递进说（现行制度）", basis="关基保护在等保基础上叠加更严格义务"),
                                   dict(holder="并行说（部分观点）", basis="两套制度应整合，避免重复合规")])],
        distinctions=[D("等级保护", "普遍适用的安全义务"), D("关键信息基础设施保护", "重点保护制度")],
        misconceptions=[dict(claim="等保只是技术测评", correction="涵盖管理、技术与运营全流程义务"),
                        dict(claim="小企业不需要做等保", correction="只要运营网络即可能负有定级备案义务")],
    ),
    "data-cybersecurity-review": dict(
        definition_source="《网络安全审查办法》及《网络安全法》《数据安全法》相关规定（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["审查对象", "申报义务", "审查内容", "审查决定"],
        conditions=["关键信息基础设施运营者采购网络产品和服务影响国家安全的", "数据处理者开展数据处理活动影响国家安全的"],
        effects=["审查期间应配合提供材料", "审查不通过不得采购或继续处理", "违反规定可能承担法律责任"],
        exceptions=["不涉及国家安全影响的一般采购无需申报", "法律、行政法规规定的其他情形"],
        cases=[],
        controversies=[dict(issue="网络安全审查与外商投资审查的关系",
                            views=[dict(holder="分工说", basis="网络安全审查侧重网络与数据安全，外资审查侧重投资准入"),
                                   dict(holder="整合说（部分观点）", basis="二者审查要素重叠，宜建立协同机制")])],
        distinctions=[D("网络安全审查", "评估产品服务与数据处理的国家安全风险"), D("数据出境安全评估", "评估数据出境风险")],
        misconceptions=[dict(claim="所有网络产品采购都要审查", correction="仅影响国家安全的特定情形需要申报"),
                        dict(claim="审查通过即永久有效", correction="情形变化时可能重新触发审查")],
    ),
    "data-public-data-open": dict(
        definition_source="《中华人民共和国数据安全法》第五章政务数据安全与开放（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["开放主体", "开放目录", "开放方式", "安全审查"],
        conditions=["政务数据依法开放", "不属于不予开放情形", "依法进行脱敏与安全审查"],
        effects=["社会主体可依法获取政务数据", "开放主体承担安全责任", "违规开放可能承担法律责任"],
        exceptions=["涉及国家秘密、商业秘密与个人信息的依法不予开放或脱敏", "法律、行政法规规定的其他情形"],
        cases=[],
        controversies=[dict(issue="政务数据开放与个人信息保护的平衡",
                            views=[dict(holder="开放优先说", basis="政务数据开放促进创新与监督，应在脱敏前提下扩大开放"),
                                   dict(holder="保护优先说（部分观点）", basis="应严格限制涉及个人信息的数据开放范围")])],
        distinctions=[D("政府信息公开", "公开政府信息"), D("政务数据开放", "开放可机读的数据集")],
        misconceptions=[dict(claim="所有政务数据都应开放", correction="涉及秘密、隐私与安全的数据依法不予开放"),
                        dict(claim="开放数据可以随意再利用", correction="再利用仍须遵守许可条件与法律规定")],
    ),
}