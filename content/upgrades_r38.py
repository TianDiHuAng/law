# -*- coding: utf-8 -*-
"""R38 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R38 = {
    "civil-property-service": dict(
        definition_source="《中华人民共和国民法典》第九百三十七条至第九百五十条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["物业服务人", "业主", "物业服务区域", "物业费", "业主共有部分"],
        conditions=["物业服务合同依法成立", "物业服务人依约提供服务", "业主按约定支付物业费"],
        effects=["合同对全体业主具有法律约束力", "物业服务人负有维修养护与秩序维护义务", "业主可依法共同决定解聘物业服务人"],
        exceptions=["物业服务人不得采取停止供电、供水等方式催交物业费", "前期物业服务合同对业主的效力依法律规定"],
        cases=[],
        controversies=[dict(issue="业主共同决定解聘物业服务人的门槛",
                            views=[dict(holder="严格程序说", basis="解聘须经业主共同决定并符合法定表决比例"),
                                   dict(holder="便利解聘说（部分观点）", basis="应降低解聘门槛，保障业主自主选择权")])],
        distinctions=[D("物业服务合同", "持续性服务合同"), D("委托合同", "处理事务的合同")],
        misconceptions=[dict(claim="物业可以断水断电催费", correction="物业服务人不得采取停止供电、供水等方式催交物业费"),
                        dict(claim="没入住就不用交物业费", correction="业主应按约定支付物业费，除非合同另有约定或法律另有规定")],
    ),
    "civil-co-ownership": dict(
        definition_source="《中华人民共和国民法典》第二百九十七条至第三百一十条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["按份共有", "共同共有", "份额处分", "共有物管理", "共有物分割"],
        conditions=["两个以上主体对同一物享有所有权", "按份共有须确定份额，共同共有依法律规定或约定"],
        effects=["按份共有人可转让其份额，其他共有人享有优先购买权", "处分共有物须依法定或约定程序", "共有人可请求分割共有物"],
        exceptions=["共同共有人处分共有财产须经全体同意（法律另有规定除外）", "因共有物性质不能分割的可折价补偿"],
        cases=[],
        controversies=[dict(issue="按份共有人优先购买权的行使条件",
                            views=[dict(holder="同等条件说（现行法）", basis="其他共有人须在同等条件下方可主张优先购买"),
                                   dict(holder="宽松说（部分学者）", basis="应适度放宽条件，维护共有关系稳定")])],
        distinctions=[D("共有", "数人共享一个所有权"), D("区分所有", "建筑物区分所有权")],
        misconceptions=[dict(claim="共有人可以随意处分共有物", correction="处分共有物须依法定或约定程序，共同共有须全体同意"),
                        dict(claim="共有关系永远不能解除", correction="共有人可依法请求分割共有物")],
    ),
    "civil-contract-interpretation": dict(
        definition_source="《中华人民共和国民法典》第一百四十二条、第四百六十六条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["文义解释", "体系解释", "目的解释", "习惯与诚信", "不利解释规则"],
        conditions=["合同条款含义存在争议", "由法院或仲裁机构作出", "依法律规定的方法进行"],
        effects=["确定当事人权利义务", "影响合同效力与责任分配", "格式条款有两种以上解释时作不利于提供方的解释"],
        exceptions=["当事人有共同理解的可优先适用", "合同约定明确且不违反法律的从其约定"],
        cases=[],
        controversies=[dict(issue="合同解释应以表示主义还是意思主义为主",
                            views=[dict(holder="表示主义说（交易安全优先）", basis="应以相对人客观理解为准，保护交易信赖"),
                                   dict(holder="意思主义说（部分学者）", basis="应探求当事人真实意思，兼顾公平")])],
        distinctions=[D("法律解释", "阐明法律规范含义"), D("合同解释", "阐明合同条款含义")],
        misconceptions=[dict(claim="合同文字清楚就不需要解释", correction="文字清楚仍可能因上下文与目的产生争议"),
                        dict(claim="解释只能依据合同文本", correction="还可结合交易习惯、履约行为与诚信原则")],
    ),
    "civil-obligation-extinction": dict(
        definition_source="《中华人民共和国民法典》第五百五十七条至第五百七十六条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["清偿", "抵销", "提存", "免除", "混同"],
        conditions=["债的关系有效存在", "出现法定或约定的消灭事由"],
        effects=["债权债务关系终止", "从权利随之消灭", "债务人可请求返还债权凭证"],
        exceptions=["提存后债权人可随时领取提存物（须承担费用）", "免除不得损害第三人利益"],
        cases=[],
        controversies=[dict(issue="清偿抵充的顺序",
                            views=[dict(holder="法定顺序说", basis="债务种类相同且均到期时，优先抵充已到期或对债权人不利的债务"),
                                   dict(holder="约定优先说（部分学者）", basis="应充分尊重当事人约定的抵充顺序")])],
        distinctions=[D("债的消灭", "债权债务终止"), D("债的移转", "主体变更而内容不变")],
        misconceptions=[dict(claim="债务人还了钱债就自动消灭", correction="清偿须向有权受领人作出并足额履行"),
                        dict(claim="提存后债务人仍需承担风险", correction="提存后标的物风险由债权人承担")],
    ),
}