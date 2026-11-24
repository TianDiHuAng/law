# -*- coding: utf-8 -*-
"""R19 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R19 = {
    "crim-punishment": dict(
        definition_source="《中华人民共和国刑法》第三章刑罚（版本：1997年修订，历次修正案至（十二），核对日期：2026-11-24）。",
        elements=["主刑", "附加刑", "刑罚种类", "刑罚执行"],
        conditions=["行为人被依法定罪", "依照刑法分则与总则确定刑罚", "符合量刑情节"],
        effects=["对犯罪人适用相应刑罚", "刑罚执行与变更依法进行", "犯罪记录产生附随后果"],
        exceptions=["犯罪情节轻微不需要判处刑罚的可免予刑事处罚", "不满十八周岁、怀孕妇女等特殊规则"],
        cases=["case-xuting"],
        controversies=[dict(issue="死刑存废",
                            views=[dict(holder="保留死刑说（现行法）", basis="对极严重犯罪保留死刑，严格限制适用"),
                                   dict(holder="废除死刑说（部分学者）", basis="生命权不可剥夺，应逐步废除死刑")])],
        distinctions=[D("主刑", "可独立适用的刑罚"), D("附加刑", "可附加或独立适用的刑罚")],
        misconceptions=[dict(claim="所有犯罪都会判刑", correction="免予刑事处罚、不起诉等情形也可能不判刑"),
                        dict(claim="罚金是主刑", correction="罚金是附加刑，可独立适用或附加适用")],
    ),
    "crim-recant": dict(
        definition_source="《中华人民共和国刑法》关于自首与立功的规定（版本：1997年修订，历次修正案至（十二），核对日期：2026-11-24；具体条文号待核实）。",
        elements=["自动投案", "如实供述", "立功表现", "重大立功"],
        conditions=["自首须自动投案并如实供述", "立功须揭发他人犯罪、提供重要线索或协助抓捕等", "重大立功须有重大贡献"],
        effects=["自首可以从轻或减轻处罚", "立功可以从轻或减轻处罚", "重大立功可以减轻或免除处罚"],
        exceptions=["被采取强制措施后如实供述司法机关尚未掌握的罪行，可视为自首（法定情形）", "坦白不等于自首"],
        cases=[],
        controversies=[dict(issue="自首“自动投案”的认定",
                            views=[dict(holder="实质说", basis="只要自愿置于司法机关控制下并如实供述即可认定"),
                                   dict(holder="形式说（部分实务观点）", basis="应严格按投案时间、方式等形式要件判断")])],
        distinctions=[D("自首", "自动投案+如实供述"), D("坦白", "被动归案后如实供述")],
        misconceptions=[dict(claim="被抓后交代就是自首", correction="自首须自动投案，被抓后交代可能构成坦白"),
                        dict(claim="立功可以免除所有刑罚", correction="立功从轻、减轻或免除处罚，须依法裁量")],
    ),
    "intl-wto-dispute": dict(
        definition_source="《关于争端解决规则与程序的谅解》（DSU）及WTO相关实践（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["磋商", "专家组", "上诉机构或替代安排", "执行监督", "报复授权"],
        conditions=["争端属于WTO协定适用范围", "成员方磋商未解决", "专家组设立与报告通过"],
        effects=["争端解决机构通过报告", "败诉方须执行或提供补偿", "不执行可能被授权报复"],
        exceptions=["发展中成员特殊与差别待遇", "涉及国家安全等例外"],
        cases=[],
        controversies=[dict(issue="上诉机构停摆后的替代机制",
                            views=[dict(holder="临时上诉仲裁说", basis="部分成员建立临时上诉仲裁，维持两审功能"),
                                   dict(holder="改革谈判说（部分观点）", basis="应通过WTO改革恢复正式上诉机构")])],
        distinctions=[D("磋商", "争端解决第一阶段"), D("专家组", "争端解决核心审理程序")],
        misconceptions=[dict(claim="WTO争端解决可以判决国内法无效", correction="WTO裁决针对成员方措施是否符合WTO协定，不直接改变国内法"),
                        dict(claim="败诉方必须立即修改法律", correction="败诉方可在合理期限内执行，也可提供补偿")],
    ),
    "intl-trade-services": dict(
        definition_source="《服务贸易总协定》（GATS）及WTO服务贸易规则（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["跨境交付", "境外消费", "商业存在", "自然人流动"],
        conditions=["属于GATS调整的服务贸易", "成员方作出具体承诺", "不违反最惠国待遇等一般义务"],
        effects=["成员方按承诺开放服务市场", "外国服务提供者享有国民待遇", "违反承诺可能引发WTO争端"],
        exceptions=["一般例外与安全例外", "发展中国家逐步开放安排"],
        cases=[],
        controversies=[dict(issue="商业存在模式与投资保护的重叠",
                            views=[dict(holder="GATS优先说", basis="服务贸易商业存在应适用GATS规则"),
                                   dict(holder="投资协定补充说（部分学者）", basis="投资保护与市场准入可适用投资条约")])],
        distinctions=[D("货物贸易", "GATT调整货物"), D("服务贸易", "GATS调整服务")],
        misconceptions=[dict(claim="服务贸易不需要开放承诺", correction="成员方通过具体承诺表决定开放部门与条件"),
                        dict(claim="GATS适用于所有服务", correction="政府采购、航空运输等部分服务另有规则或除外")],
    ),
}
