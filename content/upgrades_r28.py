# -*- coding: utf-8 -*-
"""R28 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R28 = {
    "admin-legislation": dict(
        definition_source="《中华人民共和国立法法》（版本：2023年修正，核对日期：2026-11-24）。",
        elements=["立法权限", "法律保留", "立法程序", "备案审查", "法律适用规则"],
        conditions=["立法主体具有法定权限", "遵守法定程序", "不与上位法相抵触"],
        effects=["法律、行政法规、地方性法规依法产生效力", "下位法不得抵触上位法", "备案审查保障法制统一"],
        exceptions=["法律保留事项不得由行政法规、地方性法规自行规定", "经济特区法规可依法作变通规定"],
        cases=[],
        controversies=[dict(issue="地方立法权的边界",
                            views=[dict(holder="法定权限说", basis="地方立法不得超越立法法规定的权限范围"),
                                   dict(holder="地方自主说（部分观点）", basis="应扩大地方立法自主空间以适应地方治理需要")])],
        distinctions=[D("立法法", "规范立法活动的基本法律"), D("宪法", "规定根本制度与最高法律效力")],
        misconceptions=[dict(claim="地方政府可以制定法律", correction="地方政府只能制定规章，不能制定法律"),
                        dict(claim="地方性法规可以规定任何事项", correction="不得违反法律保留与上位法规定")],
    ),
    "admin-government-info": dict(
        definition_source="《中华人民共和国政府信息公开条例》（版本：2019年修订，核对日期：2026-11-24）。",
        elements=["主动公开", "依申请公开", "不予公开情形", "监督保障"],
        conditions=["属于政府信息", "不属于法定不予公开情形", "依申请公开须提出申请"],
        effects=["行政机关应依法公开政府信息", "申请人可获得相关信息", "违法不公开可能被复议或诉讼纠正"],
        exceptions=["国家秘密", "商业秘密与个人隐私（第三方同意或公共利益需要的除外）", "内部事务信息与过程性信息可不予公开"],
        cases=[],
        controversies=[dict(issue="过程性信息公开的边界",
                            views=[dict(holder="过程性信息豁免说", basis="决策过程中的讨论记录公开可能影响坦诚表达"),
                                   dict(holder="公开优先说（部分观点）", basis="涉及公共利益的过程性信息应适度公开")])],
        distinctions=[D("政务公开", "更广泛的公开政策"), D("政府信息公开", "法定信息公开制度")],
        misconceptions=[dict(claim="所有政府信息都必须公开", correction="法定不予公开情形依法不公开"),
                        dict(claim="申请公开需要说明理由", correction="申请一般无需说明特殊理由，但需描述信息特征")],
    ),
    "civil-privacy": dict(
        definition_source="《中华人民共和国民法典》第一千零三十二条至第一千零三十九条及《个人信息保护法》（版本：2020年通过/2021年通过，核对日期：2026-11-24）。",
        elements=["私人生活安宁", "私密空间", "私密活动", "私密信息", "个人信息处理规则"],
        conditions=["属于隐私或个人信息", "处理活动未取得合法性基础", "造成或可能造成侵害"],
        effects=["权利人可请求停止侵害、删除、赔礼道歉、赔偿损失", "处理者承担合规义务", "违法处理可能承担行政与刑事责任"],
        exceptions=["法律另有规定", "为公共利益实施新闻报道、舆论监督等合理使用", "本人同意或主动公开"],
        cases=["case-google-spain"],
        controversies=[dict(issue="隐私权与个人信息保护的关系",
                            views=[dict(holder="交叉说（通说）", basis="隐私权保护私密信息，个人信息保护覆盖可识别信息，二者交叉"),
                                   dict(holder="并列说（部分学者）", basis="二者保护对象与规则不同，应分别适用")])],
        distinctions=[D("隐私权", "保护私密空间与生活安宁"), D("个人信息权益", "保护可识别个人的信息处理活动")],
        misconceptions=[dict(claim="公开过的信息就不受保护", correction="已公开信息仍受个人信息保护规则约束"),
                        dict(claim="只有名人才有隐私权", correction="自然人均享有隐私权")],
    ),
}