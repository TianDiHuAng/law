# -*- coding: utf-8 -*-
"""R58 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R58 = {
    "civil-debt-security-comparison": dict(
        definition_source="《中华人民共和国民法典》合同编（债的保全）与物权编、合同编（担保）（核对日期：2026-11-24）。",
        elements=["债的保全手段", "债的担保手段", "功能定位", "法律效果"],
        conditions=["债权合法有效", "保全以债务人责任财产不当减少为前提", "担保依约定或法定设立"],
        effects=["保全维持债务人责任财产", "担保产生优先受偿或第三人责任", "二者可并用"],
        exceptions=["专属于债务人的权利不得代位", "担保物权须依法设立并公示"],
        cases=[],
        controversies=[dict(issue="债的保全的性质",
                            views=[dict(holder="债的效力说（通说）", basis="保全属于债的一般效力，非独立担保"),
                                   dict(holder="法定担保说（部分学者）", basis="保全具有担保债权实现的功能，可视为广义担保")])],
        distinctions=[D("债的保全", "维持责任财产"), D("债的担保", "增强特定债权保障")],
        misconceptions=[dict(claim="保全和担保是一回事", correction="保全针对责任财产减少，担保通过特定财产或第三人信用"),
                        dict(claim="有担保就不需要保全", correction="二者功能不同，可并用强化债权保障")],
    ),
    "civil-obligation-transfer": dict(
        definition_source="《中华人民共和国民法典》第五百四十五条至第五百五十六条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["债权让与", "债务承担", "概括移转", "通知与同意"],
        conditions=["债权具有可让与性", "债务承担须经债权人同意", "概括移转须经对方同意"],
        effects=["债权让与通知债务人后对其生效", "债务承担后原债务人免责（免责式）", "概括移转由受让人承受合同地位"],
        exceptions=["依性质、约定或法律规定不得让与的债权不得让与", "从权利随主债权移转（专属于债权人的除外）"],
        cases=[],
        controversies=[dict(issue="债权让与的通知主体",
                            views=[dict(holder="让与人通知说（现行法）", basis="原则上由让与人通知债务人"),
                                   dict(holder="受让人可持凭证通知说（部分观点）", basis="受让人持转让凭证通知亦可发生效力")])],
        distinctions=[D("债权让与", "债权人变更"), D("债务承担", "债务人变更")],
        misconceptions=[dict(claim="债权转让无需通知债务人", correction="未经通知，转让对债务人不发生效力"),
                        dict(claim="债务可以随意转给他人", correction="免责的债务承担须经债权人同意")],
    ),
    "civil-standard-terms": dict(
        definition_source="《中华人民共和国民法典》第四百九十六条至第四百九十八条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["格式条款定义", "提示说明义务", "无效情形", "不利解释规则"],
        conditions=["条款为重复使用而预先拟定", "订立时未与对方协商", "提供方须履行提示说明义务"],
        effects=["不合理免责或加重对方责任的条款无效", "有两种以上解释时作不利于提供方的解释", "未尽提示说明义务致对方未注意的，对方可主张该条款不成为合同内容"],
        exceptions=["格式条款经对方同意且不违反法律的可有效", "非格式条款与格式条款不一致的，采用非格式条款"],
        cases=[],
        controversies=[dict(issue="提示说明义务的履行标准",
                            views=[dict(holder="显著提示说", basis="以合理方式提请对方注意即可"),
                                   dict(holder="实质说明说（部分观点）", basis="还须按对方要求予以说明，确保其理解条款含义")])],
        distinctions=[D("格式条款", "预先拟定未协商"), D("个别磋商条款", "经双方协商确定")],
        misconceptions=[dict(claim="格式条款一律无效", correction="仅不合理免责等特定情形无效，其余可有效"),
                        dict(claim="小字条款都有效", correction="未尽提示说明义务的，对方可主张不成为合同内容")],
    ),
    "civil-offset": dict(
        definition_source="《中华人民共和国民法典》第五百六十八条至第五百六十九条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["法定抵销", "约定抵销", "抵销条件", "抵销通知"],
        conditions=["双方互负债务", "标的物种类、品质相同", "债务均已到期（或依约定可抵销）"],
        effects=["抵销后债务在对等额度内消灭", "法定抵销须通知对方，通知到达时生效", "抵销不得附条件或附期限"],
        exceptions=["依债务性质不得抵销的不得抵销", "依照法律规定不得抵销的不得抵销"],
        cases=[],
        controversies=[dict(issue="抵销的溯及效力",
                            views=[dict(holder="抵销适状时说", basis="抵销效力溯及至抵销适状之时"),
                                   dict(holder="通知生效说（部分观点）", basis="抵销自通知到达对方时生效")])],
        distinctions=[D("法定抵销", "符合法定条件单方主张"), D("约定抵销", "双方合意抵销")],
        misconceptions=[dict(claim="任何债务都可以抵销", correction="须种类品质相同且依法可抵销"),
                        dict(claim="抵销可以附加条件", correction="法定抵销不得附条件或附期限")],
    ),
}