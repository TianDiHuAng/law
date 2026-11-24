# -*- coding: utf-8 -*-
"""R29 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R29 = {
    "proc-civil-preservation": dict(
        definition_source="《中华人民共和国民事诉讼法》保全与先予执行（版本：2023年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["诉前保全", "诉中保全", "担保", "保全措施", "错误保全责任"],
        conditions=["可能因当事人一方行为或其他原因使判决难以执行", "申请人提出申请或法院依职权", "诉前保全须提供担保"],
        effects=["法院裁定查封、扣押、冻结财产", "申请人在法定期限内不起诉的，解除保全", "申请有错误的应赔偿被申请人损失"],
        exceptions=["保全限于请求范围或与本案有关的财物", "对案外人财产的保全应依法审查"],
        cases=[],
        controversies=[dict(issue="保全必要性的审查标准",
                            views=[dict(holder="宽松审查说", basis="为保障判决执行，应对保全申请从宽把握"),
                                   dict(holder="严格审查说（部分实务观点）", basis="保全影响被申请人经营，应严格审查必要性")])],
        distinctions=[D("财产保全", "限制财产处分"), D("行为保全", "责令作出或不作出一定行为")],
        misconceptions=[dict(claim="申请保全不需要任何成本", correction="通常需提供担保，错误保全还要赔偿损失"),
                        dict(claim="诉前保全后可以不起诉", correction="诉前保全后应在法定期限内起诉，否则解除保全")],
    ),
    "proc-civil-mediation": dict(
        definition_source="《中华人民共和国民事诉讼法》调解（版本：2023年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["自愿原则", "合法原则", "调解协议", "调解书"],
        conditions=["双方当事人自愿", "调解内容不违反法律强制性规定", "在法院主持下进行"],
        effects=["调解书经签收后生效", "具有强制执行力", "调解不成的及时判决"],
        exceptions=["婚姻关系、身份关系确认案件不适用调解", "适用特别程序、督促程序、公示催告程序的案件不适用调解"],
        cases=[],
        controversies=[dict(issue="调解是否应追求查明事实",
                            views=[dict(holder="事实清楚说（现行法）", basis="调解应在事实清楚的基础上进行"),
                                   dict(holder="效率优先说（部分实务观点）", basis="调解重在化解纠纷，可适当简化事实查明")])],
        distinctions=[D("法院调解", "诉讼中由法院主持"), D("人民调解", "诉讼外由人民调解委员会主持")],
        misconceptions=[dict(claim="调解书不能强制执行", correction="生效调解书与判决书一样可申请强制执行"),
                        dict(claim="调解必须双方都让步", correction="调解内容由当事人自愿协商，法律不强制让步幅度")],
    ),
    "proc-admin-litigation": dict(
        definition_source="《中华人民共和国行政诉讼法》受案范围（版本：2017年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["可诉行政行为", "不可诉事项", "规范性文件附带审查", "原告资格"],
        conditions=["行政行为侵犯原告合法权益", "属于法定的可诉范围", "原告与被诉行为有利害关系"],
        effects=["法院受理并审查行政行为合法性", "不属于受案范围的可裁定不予立案", "规范性文件可附带审查"],
        exceptions=["国家行为", "内部行政行为", "终局裁决行为", "调解与仲裁行为"],
        cases=[],
        controversies=[dict(issue="受案范围的扩张",
                            views=[dict(holder="逐步扩大说", basis="行政诉讼受案范围应随法治发展逐步扩大"),
                                   dict(holder="法定范围说（部分实务观点）", basis="应严格依照法律规定确定受案范围")])],
        distinctions=[D("受案范围", "法院可以审理的行政争议范围"), D("原告资格", "谁有权提起诉讼")],
        misconceptions=[dict(claim="所有行政行为都可诉", correction="法律明确排除的行为不可诉"),
                        dict(claim="任何人都可以起诉行政行为", correction="原告须与被诉行为有利害关系")],
    ),
    "com-insider": dict(
        definition_source="《中华人民共和国证券法》禁止内幕交易的规定及《刑法》内幕交易罪条款（版本：2019年修订/历次修正案，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["内幕信息", "内幕信息知情人", "内幕交易行为", "法律责任"],
        conditions=["信息属于内幕信息", "行为人在敏感期内买卖或建议他人买卖", "或泄露内幕信息"],
        effects=["没收违法所得并处罚款", "情节严重的构成内幕交易罪", "给投资者造成损失的依法承担赔偿责任"],
        exceptions=["依法进行的收购、重组等已履行披露义务的行为", "法律规定的其他豁免情形"],
        cases=[],
        controversies=[dict(issue="内幕信息敏感期的起算",
                            views=[dict(holder="重大事件发生时说", basis="自重大事件发生或形成时起算敏感期"),
                                   dict(holder="动议形成时说（部分观点）", basis="应自相关动议形成时起算，防止提前交易")])],
        distinctions=[D("内幕交易", "利用未公开重大信息交易"), D("操纵市场", "通过交易或信息影响证券价格")],
        misconceptions=[dict(claim="只有公司高管才可能构成内幕交易", correction="非法获取内幕信息的人同样可能构成"),
                        dict(claim="内幕交易只承担行政责任", correction="情节严重的可构成犯罪")],
    ),
}