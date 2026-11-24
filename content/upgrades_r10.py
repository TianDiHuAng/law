# -*- coding: utf-8 -*-
"""R10 体检轮附加升级：2 条重要条目。"""

UPGRADES_R10 = {
    "civil-unjust-enrichment": dict(
        definition_source="《中华人民共和国民法典》第九百八十五条至第九百八十八条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["一方取得利益", "他方受损失", "取得利益没有法律根据", "利益与损失之间存在因果关系"],
        conditions=["得利人没有法律根据取得利益", "他人因此受到损失", "得利与损失之间存在因果关系"],
        effects=["得利人应返还取得的利益", "善意得利人返还范围以现存利益为限", "恶意得利人应返还全部利益并赔偿损失"],
        exceptions=["为履行道德义务进行的给付", "债务到期之前的清偿", "明知无给付义务而进行的债务清偿"],
        cases=[],
        controversies=[dict(issue="给付型不当得利中“没有法律根据”的判断",
                            views=[dict(holder="给付目的说", basis="应考察给付是否具有法律上的原因"),
                                   dict(holder="权益归属说（部分学者）", basis="应看利益变动是否符合法秩序所定的权益归属")])],
        distinctions=[dict(**{"with": "合同", "difference": "合同是约定之债，不当得利是法定之债"}),
                      dict(**{"with": "侵权", "difference": "侵权以违法行为与过错为基础，不当得利关注无法律根据的利益变动"})],
        misconceptions=[dict(claim="只要对方多收了钱就构成不当得利", correction="还须没有法律根据且造成他方损失"),
                        dict(claim="不当得利必须返还原物", correction="返还范围依善意/恶意及利益是否存在确定")],
    ),
    "com-company-capital": dict(
        definition_source="《中华人民共和国公司法》关于注册资本、股东出资与公司资本的规定（版本：2023年修订，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["注册资本", "股东认缴出资", "实缴出资", "资本维持", "资本不变"],
        conditions=["公司依法登记注册资本", "股东按章程约定认缴并缴纳出资", "减资须依法定程序"],
        effects=["股东以认缴出资为限对公司承担责任", "公司应维持与其资本相应的财产", "抽逃出资的股东应返还并承担相应责任"],
        exceptions=["法律规定的认缴期限与加速到期情形", "公司减资须通知债权人并公告"],
        cases=["case-salomon"],
        controversies=[dict(issue="注册资本认缴制下债权人保护",
                            views=[dict(holder="2023年公司法取向", basis="五年缴足与加速到期强化资本充实与债权人保护"),
                                   dict(holder="部分学者", basis="应避免过度干预企业自治与融资安排")])],
        distinctions=[dict(**{"with": "公司资产", "difference": "注册资本是登记资本额，公司资产是公司实际拥有的财产"}),
                      dict(**{"with": "股东借款", "difference": "股东借款形成债权债务，抽逃出资则违反资本维持义务"})],
        misconceptions=[dict(claim="注册资本越高公司越有实力", correction="注册资本是认缴承诺，过高会增加股东出资责任"),
                        dict(claim="认缴出资可以永远不缴", correction="2023年公司法规定五年内缴足，特定情形可加速到期")],
    ),
}

UPGRADES_R10["civil-negotiorum"] = dict(
    definition_source="《中华人民共和国民法典》第九百七十九条至第九百八十四条（版本：2020年通过，核对日期：2026-11-24）。",
    elements=["没有法定或约定义务", "管理他人事务", "为避免他人利益受损失", "管理行为"],
    conditions=["管理人没有法定或约定义务", "管理他人事务", "管理行为有利于受益人且不违反其真实意思"],
    effects=["管理人有权请求受益人偿还因管理事务而支出的必要费用", "管理人因管理事务受到损失的，可请求适当补偿", "管理人应依受益人真实意思管理并报告"],
    exceptions=["管理事务不符合受益人真实意思的，不享有费用偿还请求权，但受益人真实意思违反法律或公序良俗的除外"],
    cases=[],
    controversies=[dict(issue="无因管理与不当得利的界限", views=[dict(holder="通说", basis="无因管理是合法管理他人事务，不当得利是无法律根据取得利益"), dict(holder="部分学者", basis="二者可能竞合，应依具体利益变动判断")])],
    distinctions=[dict(**{"with": "委托合同", "difference": "委托合同有约定义务，无因管理无法定或约定义务"}), dict(**{"with": "侵权", "difference": "无因管理以利于他人为目的，侵权以侵害他人权益为特征"})],
    misconceptions=[dict(claim="帮别人做事就一定构成无因管理", correction="须没有法定或约定义务，且为避免他人利益受损失"), dict(claim="无因管理可以随意处分他人财产", correction="管理人应依受益人真实意思管理，不得擅自处分")],
)
