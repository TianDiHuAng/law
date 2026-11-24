# -*- coding: utf-8 -*-
"""R36 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R36 = {
    "civil-personality-injunction": dict(
        definition_source="《中华人民共和国民法典》第九百九十七条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["有证据证明侵害正在或即将实施", "不及时制止将造成难以弥补的损害", "申请人为民事主体", "请求责令停止有关行为"],
        conditions=["存在侵害人格权的现实危险", "损害具有难以弥补性", "申请人提供初步证据"],
        effects=["法院可裁定责令停止有关行为", "禁令具有临时救济性质", "违反禁令可能承担法律责任"],
        exceptions=["申请错误的应赔偿被申请人损失", "禁令不影响实体诉讼的最终裁判"],
        cases=[],
        controversies=[dict(issue="人格权禁令与行为保全的关系",
                            views=[dict(holder="独立制度说", basis="人格权禁令是民法典确立的独立救济方式，不依附于诉讼"),
                                   dict(holder="行为保全特别类型说（部分学者）", basis="其性质属于行为保全，应适用民事诉讼法保全规则")])],
        distinctions=[D("行为保全", "诉讼中或诉前的临时措施"), D("停止侵害判决", "实体裁判确定终局责任")],
        misconceptions=[dict(claim="禁令只能在起诉后申请", correction="人格权禁令可不以提起诉讼为前提"),
                        dict(claim="禁令等同于胜诉", correction="禁令是临时救济，实体责任仍需通过诉讼确定")],
    ),
    "civil-construction-contract": dict(
        definition_source="《中华人民共和国民法典》第七百八十八条至第八百零八条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["发包人", "承包人", "工程建设", "价款支付"],
        conditions=["合同采用书面形式", "承包人具有相应资质", "依法办理规划、施工许可等手续"],
        effects=["承包人按约完成工程", "发包人支付价款并组织验收", "承包人对建设工程享有价款优先受偿权"],
        exceptions=["违法转包、分包可能导致合同无效", "必须招标而未招标的建设工程合同无效"],
        cases=[],
        controversies=[dict(issue="建设工程价款优先受偿权的性质",
                            views=[dict(holder="法定抵押权说", basis="优先受偿权具有物权性质，优先于一般债权"),
                                   dict(holder="优先权说（部分学者）", basis="属于法律特别规定的优先权，非抵押权")])],
        distinctions=[D("承揽合同", "以工作成果为标的，一般无需资质"), D("建设工程合同", "以工程建设为标的，须书面形式与资质")],
        misconceptions=[dict(claim="口头约定施工也有效", correction="建设工程合同应当采用书面形式"),
                        dict(claim="工程款总是优先于抵押权", correction="优先受偿权顺位与消费者购房人等权利需依法确定")],
    ),
    "civil-legacy-support": dict(
        definition_source="《中华人民共和国民法典》第一千一百五十八条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["遗赠人", "扶养人", "生养死葬义务", "受遗赠权利"],
        conditions=["扶养人为继承人以外的组织或个人", "采用书面协议形式", "协议内容合法"],
        effects=["扶养人承担生养死葬义务并享有受遗赠权", "协议优先于遗嘱继承与法定继承", "扶养人无正当理由不履行的可能丧失受遗赠权"],
        exceptions=["扶养人不履行义务致协议解除的，应偿还已支付的扶养费用", "遗赠财产须为遗赠人合法财产"],
        cases=[],
        controversies=[dict(issue="遗赠扶养协议的性质",
                            views=[dict(holder="双务合同说（通说）", basis="协议双方互负义务，属双务有偿合同"),
                                   dict(holder="身份性协议说（部分学者）", basis="兼具扶养与继承功能，具有身份法色彩")])],
        distinctions=[D("遗赠", "单方无偿行为"), D("遗嘱继承", "以遗嘱指定继承人")],
        misconceptions=[dict(claim="签了协议就一定拿到遗产", correction="扶养人须履行生养死葬义务方可享有受遗赠权"),
                        dict(claim="遗赠扶养协议可以口头订立", correction="应采用书面形式明确权利义务")],
    ),
    "civil-adoption": dict(
        definition_source="《中华人民共和国民法典》第一千零九十三条至第一千一百一十八条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["收养人条件", "被收养人条件", "收养登记", "收养效力", "收养解除"],
        conditions=["收养人年满三十周岁、无子女或只有一名子女、有抚养能力", "被收养人一般为未成年人", "依法办理收养登记"],
        effects=["形成拟制血亲关系", "养子女与养父母间权利义务适用父母子女规定", "养子女与生父母间权利义务因收养而消除"],
        exceptions=["收养三代以内同辈旁系血亲的子女可放宽部分条件", "继父母收养继子女可放宽条件"],
        cases=[],
        controversies=[dict(issue="事实收养的效力",
                            views=[dict(holder="登记生效说（现行法）", basis="收养关系自登记之日起成立"),
                                   dict(holder="区分说（部分学者）", basis="历史形成的事实收养应依当时法律与政策处理")])],
        distinctions=[D("寄养", "不改变亲子关系"), D("收养", "形成拟制血亲关系")],
        misconceptions=[dict(claim="双方同意就能收养", correction="须符合法定条件并办理收养登记"),
                        dict(claim="收养后养子女仍可继承生父母遗产", correction="收养关系成立后与生父母权利义务消除，除法律另有规定")],
    ),
}