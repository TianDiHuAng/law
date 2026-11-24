# -*- coding: utf-8 -*-
"""R46 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R46 = {
    "intl-commercial-arbitration": dict(
        definition_source="《承认及执行外国仲裁裁决公约》（纽约公约）及主要仲裁机构规则（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["仲裁协议", "仲裁地", "仲裁庭组成", "裁决效力", "承认与执行"],
        conditions=["存在有效书面仲裁协议", "争议具有可仲裁性", "仲裁程序符合约定与仲裁地法"],
        effects=["裁决具有终局性与拘束力", "可依纽约公约在其他缔约国申请承认与执行", "裁决可被仲裁地法院撤销"],
        exceptions=["仲裁协议无效", "程序不当或超裁", "争议事项不可仲裁", "公共政策例外"],
        cases=[],
        controversies=[dict(issue="国际仲裁的保密性与透明度",
                            views=[dict(holder="保密优先说", basis="保密是商事仲裁的核心优势，当事人可约定不公开"),
                                   dict(holder="透明度说（部分领域）", basis="涉及公共利益的投资与 sport 仲裁应提高透明度")])],
        distinctions=[D("国内仲裁", "适用国内仲裁法"), D("国际商事仲裁", "具有涉外因素并适用纽约公约执行机制")],
        misconceptions=[dict(claim="国际仲裁裁决在任何国家都能执行", correction="须依纽约公约或互惠安排，且可能因法定事由被拒绝"),
                        dict(claim="仲裁不能上诉就绝对终局", correction="可依仲裁地法申请撤销，或在执行地抗辩")],
    ),
    "intl-investment-arbitration": dict(
        definition_source="《ICSID公约》及投资条约仲裁条款（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["投资者", "投资", "东道国同意", "仲裁庭", "裁决执行"],
        conditions=["存在受保护的投资", "投资者符合条约国籍要求", "东道国以条约或合同表示同意仲裁"],
        effects=["仲裁庭对争端有管辖权", "裁决对当事方具有拘束力", "裁决可依 ICSID 公约执行"],
        exceptions=["不属于条约保护范围的投资", "用尽当地救济要求未满足", "条约中的例外条款"],
        cases=[],
        controversies=[dict(issue="ISDS 与东道国规制权",
                            views=[dict(holder="投资保护说", basis="ISDS 保障投资者免受任意征收与不公正待遇"),
                                   dict(holder="规制权说（部分学者）", basis="应保留东道国为公共健康、环境采取规制措施的空间")])],
        distinctions=[D("国际商事仲裁", "解决平等商事主体争议"), D("投资仲裁", "一方为东道国的条约争端")],
        misconceptions=[dict(claim="任何外国投资者都可提起 ICSID 仲裁", correction="须满足条约同意、投资者资格与投资定义"),
                        dict(claim="投资仲裁裁决不可执行", correction="ICSID 裁决在缔约国具有与终审判决同等效力")],
    ),
    "intl-international-watercourses": dict(
        definition_source="1997年《国际水道非航行使用法公约》及相关习惯法（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["国际水道", "公平合理利用", "不造成重大损害", "通知协商", "合作义务"],
        conditions=["水道位于两个以上国家境内", "使用行为影响他国", "当事国应善意合作"],
        effects=["沿岸国享有公平合理利用权利", "造成重大损害的应采取措施消除或减轻", "争端应通过协商或公约机制解决"],
        exceptions=["公约尚未普遍生效，部分规则以习惯法形式适用"],
        cases=[],
        controversies=[dict(issue="公平合理利用与不造成重大损害的优先顺序",
                            views=[dict(holder="利用优先说", basis="公平合理利用是核心原则，不造成重大损害是其限制"),
                                   dict(holder="损害优先说（部分观点）", basis="避免重大损害应作为优先约束")])],
        distinctions=[D("国际河流航行权", "涉及航行"), D("国际水道法", "涉及非航行使用与保护")],
        misconceptions=[dict(claim="上游国家可以任意用水", correction="须遵守公平合理利用与不造成重大损害义务"),
                        dict(claim="国际水道公约对所有国家生效", correction="公约生效范围有限，部分规则仍依习惯法")],
    ),
    "intl-development-law": dict(
        definition_source="联合国发展权宣言及相关决议、发展援助协定（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["发展权", "官方发展援助", "特殊与差别待遇", "技术合作", "债务安排"],
        conditions=["发展中国家身份认定", "援助或合作协定生效", "符合受援国发展战略"],
        effects=["受援国获得资金与技术合作", "援助方承担承诺义务（多为政治或软法义务）", "发展权在国际人权体系中获得确认"],
        exceptions=["援助常附条件，具体义务依协定确定", "发展权多属软法性质，缺乏强制争端解决机制"],
        cases=[],
        controversies=[dict(issue="发展权是否具有可诉性",
                            views=[dict(holder="软法说（通说）", basis="发展权多为宣言性文件，缺乏条约约束力"),
                                   dict(holder="可诉权说（部分学者）", basis="发展权可作为人权诉讼与国际监督的依据")])],
        distinctions=[D("国际经济法", "规范经济交往"), D("国际发展法", "关注发展援助与能力建设")],
        misconceptions=[dict(claim="发展援助是法律义务", correction="多数援助承诺属政治承诺或软法义务"),
                        dict(claim="发展权只是道义主张", correction="发展权已在联合国文件与人权体系中获得确认")],
    ),
}