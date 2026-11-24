# -*- coding: utf-8 -*-
"""R31 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R31 = {
    "labor-dispute": dict(
        definition_source="《中华人民共和国劳动争议调解仲裁法》（版本：2007年通过，2008年5月1日施行，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["协商", "调解", "仲裁", "诉讼"],
        conditions=["属于劳动争议受案范围", "当事人适格", "在法定时效内提出"],
        effects=["仲裁裁决对部分事项为终局裁决", "不服裁决可依法起诉", "调解协议可申请仲裁审查或司法确认"],
        exceptions=["劳动争议仲裁不收费", "追索劳动报酬等案件可先予执行"],
        cases=[],
        controversies=[dict(issue="仲裁前置是否妨碍救济效率",
                            views=[dict(holder="前置必要说", basis="仲裁专业、便捷，可分流大量劳动争议"),
                                   dict(holder="选择权说（部分观点）", basis="应允许当事人直接选择诉讼，减少救济环节")])],
        distinctions=[D("劳动争议仲裁", "由劳动人事争议仲裁委员会处理"), D("商事仲裁", "依仲裁协议一裁终局")],
        misconceptions=[dict(claim="劳动争议必须先仲裁才能起诉", correction="仲裁前置是原则，但特定情形与终局裁决另有规定"),
                        dict(claim="劳动仲裁要收费", correction="劳动争议仲裁不收费")],
    ),
    "social-protection": dict(
        definition_source="《中华人民共和国社会保险法》及社会救助相关制度（版本：2018年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["社会保险", "社会救助", "社会福利", "社会优抚"],
        conditions=["符合法定救助或保障条件", "依法申请或经认定", "家庭经济状况核查"],
        effects=["符合条件的对象获得物质帮助", "保障基本生活与基本医疗", "骗取救助应退还并承担法律责任"],
        exceptions=["法定不予救助情形", "临时救助的紧急程序"],
        cases=[],
        controversies=[dict(issue="社会救助的给付水平",
                            views=[dict(holder="保基本说", basis="救助以保障基本生活为目标，避免福利依赖"),
                                   dict(holder="适度提高说（部分观点）", basis="应随经济发展逐步提高救助标准")])],
        distinctions=[D("社会保险", "缴费型保障"), D("社会救助", "非缴费型兜底保障")],
        misconceptions=[dict(claim="有工作就不能申请救助", correction="符合条件的最低生活保障家庭仍可依法申请"),
                        dict(claim="救助申请不需要审核", correction="需经家庭经济状况核对与审核确认程序")],
    ),
    "com-bankruptcy-avoidance": dict(
        definition_source="《中华人民共和国企业破产法》第三十一条、第三十二条（版本：2006年通过，核对日期：2026-11-24）。",
        elements=["可撤销行为", "临界期间", "管理人", "撤销后果"],
        conditions=["行为发生在法院受理破产申请前法定期间内", "行为损害债权人利益", "由管理人请求法院撤销"],
        effects=["行为被撤销后财产回归债务人财产", "相对人返还财产或折价补偿", "相关责任人员可能承担赔偿责任"],
        exceptions=["使债务人财产受益的个别清偿不可撤销", "善意相对人已支付合理对价的处理依法律规定"],
        cases=[],
        controversies=[dict(issue="个别清偿撤销的例外",
                            views=[dict(holder="严格撤销说", basis="临界期内的个别清偿原则上应撤销，保障公平清偿"),
                                   dict(holder="例外扩张说（部分学者）", basis="应扩大使债务人财产受益的例外，维护交易安全")])],
        distinctions=[D("破产撤销权", "针对临界期内的不当处分行为"), D("民法撤销权", "针对债务人无偿处分或明显不合理交易")],
        misconceptions=[dict(claim="破产前所有清偿都可撤销", correction="仅限法定临界期内损害债权人利益的行为"),
                        dict(claim="撤销权由债权人行使", correction="破产程序中由管理人依法行使")],
    ),
    "com-bill-defense": dict(
        definition_source="《中华人民共和国票据法》关于票据抗辩与追索权的规定（版本：2004年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["对物抗辩", "对人抗辩", "追索权", "拒绝证明"],
        conditions=["持票人行使追索权须具备法定事由", "在法定期间内作成拒绝证明并通知前手", "票据背书连续"],
        effects=["持票人可向前手追索票据金额及费用", "票据债务人可依抗辩事由拒绝履行", "逾期未追索可能丧失对前手的追索权"],
        exceptions=["对物抗辩可对抗任何持票人", "善意取得票据的持票人权利受保护"],
        cases=[],
        controversies=[dict(issue="票据抗辩切断的范围",
                            views=[dict(holder="严格切断说", basis="票据债务人不得以与出票人或前手的抗辩事由对抗善意持票人"),
                                   dict(holder="恶意例外说（部分观点）", basis="持票人明知抗辩事由取得票据的，抗辩不切断")])],
        distinctions=[D("票据抗辩", "债务人拒绝履行"), D("票据追索", "持票人向前手请求偿还")],
        misconceptions=[dict(claim="票据到期不获付款可直接起诉出票人", correction="应先依法作成拒绝证明并通知前手"),
                        dict(claim="票据抗辩可以对抗任何持票人", correction="对人抗辩不得对抗善意持票人")],
    ),
}