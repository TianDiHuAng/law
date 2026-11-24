# -*- coding: utf-8 -*-
"""R48 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R48 = {
    "data-pi-audit": dict(
        definition_source="《中华人民共和国个人信息保护法》第五十四条（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["审计主体", "审计周期", "审计内容", "审计记录"],
        conditions=["处理者定期开展合规审计", "审计覆盖处理规则、告知同意、权利响应、安全保障等"],
        effects=["发现合规风险应及时整改", "应留存审计记录", "审计结果可作为合规证明"],
        exceptions=["法律、行政法规另有规定的", "处理活动规模极小的可简化处理"],
        cases=[],
        controversies=[dict(issue="审计主体是否必须为外部机构",
                            views=[dict(holder="内外结合说（现行制度）", basis="可自行审计，也可委托专业机构"),
                                   dict(holder="强制外部审计说（部分观点）", basis="外部独立审计更能保障客观性")])],
        distinctions=[D("合规审计", "定期全面审计"), D("个人信息保护影响评估", "事前专项评估")],
        misconceptions=[dict(claim="审计只做一次即可", correction="合规审计应定期开展"),
                        dict(claim="审计记录无需保存", correction="应留存审计记录以备监管检查")],
    ),
    "data-automated-decision": dict(
        definition_source="《中华人民共和国个人信息保护法》第二十四条（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["自动化决策", "透明度要求", "公平公正", "拒绝权", "说明权"],
        conditions=["利用个人信息进行自动化决策", "决策对个人权益产生影响"],
        effects=["应保证决策透明与结果公平", "不得实行不合理差别待遇", "重大影响决定个人有权拒绝并要求说明"],
        exceptions=["法律、行政法规另有规定的", "不涉及个人权益的纯粹技术处理"],
        cases=[],
        controversies=[dict(issue="算法说明义务的深度",
                            views=[dict(holder="逻辑说明说", basis="告知决策逻辑与主要因素即可，不必公开源代码"),
                                   dict(holder="可解释性说（部分学者）", basis="应提供足以使个人理解并质疑的具体解释")])],
        distinctions=[D("自动化决策", "基于个人信息的自动分析决策"), D("算法推荐", "信息内容分发")],
        misconceptions=[dict(claim="自动化决策不需要告知", correction="应保证透明度并履行告知义务"),
                        dict(claim="个人无权拒绝自动化决策", correction="对重大影响决定个人有权拒绝")],
    ),
    "data-algorithm-recommendation": dict(
        definition_source="《互联网信息服务算法推荐管理规定》及《个人信息保护法》第二十四条（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["算法推荐服务", "备案", "用户选择权", "内容治理", "未成年人保护"],
        conditions=["向境内公众提供算法推荐服务", "具有舆论属性或社会动员能力"],
        effects=["应公示基本原理与运行机制", "应提供关闭算法推荐的选项", "应履行备案与安全评估义务"],
        exceptions=["依法无需备案的服务类型", "法律规定的其他情形"],
        cases=[],
        controversies=[dict(issue="关闭算法推荐后服务是否应保持同等质量",
                            views=[dict(holder="基本服务保障说", basis="关闭推荐后仍应提供基本服务，不得变相惩罚用户"),
                                   dict(holder="自主经营说（部分观点）", basis="服务提供者可依商业模式调整呈现方式")])],
        distinctions=[D("算法推荐治理", "内容分发规制"), D("自动化决策", "权益相关决策规制")],
        misconceptions=[dict(claim="算法推荐无需备案", correction="具有舆论属性或社会动员能力的应备案"),
                        dict(claim="用户可以要求完全关闭推荐", correction="应提供关闭选项，具体形态依规定与实践")],
    ),
    "data-minor": dict(
        definition_source="《中华人民共和国未成年人保护法》网络保护专章及《个人信息保护法》第三十一条（版本：2020年修订/2021年通过，核对日期：2026-11-24）。",
        elements=["网络素养", "信息内容管理", "个人信息保护", "沉迷防治", "网络欺凌"],
        conditions=["服务对象包含未成年人", "处理不满十四周岁未成年人个人信息须取得监护人同意"],
        effects=["网络服务提供者承担特殊保护义务", "应制定专门的处理规则", "违法处理面临更重责任"],
        exceptions=["法律、行政法规另有规定的", "为保护未成年人所必需的紧急情形"],
        cases=[],
        controversies=[dict(issue="未成年人模式的实际效果",
                            views=[dict(holder="强制模式说", basis="应以强制身份认证与时长限制保障未成年人"),
                                   dict(holder="自主选择说（部分观点）", basis="过度限制可能促使未成年人绕过监管，应兼顾教育与自主")])],
        distinctions=[D("未成年人网络保护", "专门保护制度"), D("一般个人信息保护", "适用于所有自然人")],
        misconceptions=[dict(claim="未成年人信息只要监护人同意就可任意处理", correction="还须遵循必要原则与专门保护规则"),
                        dict(claim="网络保护只针对游戏", correction="涵盖信息内容、个人信息、沉迷防治与网络欺凌等多方面")],
    ),
}