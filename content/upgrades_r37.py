# -*- coding: utf-8 -*-
"""R37 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R37 = {
    "civil-name": dict(
        definition_source="《中华人民共和国民法典》第一千零一十二条至第一千零一十七条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["姓名决定权", "姓名使用权", "姓名变更权", "许可他人使用权"],
        conditions=["主体为自然人", "依法选取姓氏", "不得违背公序良俗"],
        effects=["可决定、使用、变更姓名", "可许可他人使用自己的姓名", "禁止他人干涉、盗用、假冒"],
        exceptions=["自然人选取姓氏应随父姓或母姓，特定情形可在父姓母姓之外选取", "笔名、艺名等受姓名权保护规则参照适用"],
        cases=["case-jordan"],
        controversies=[dict(issue="姓名权与商标权、名人姓名的保护边界",
                            views=[dict(holder="在先权利说", basis="姓名权属在先权利，可对抗恶意抢注商标"),
                                   dict(holder="混淆可能说（部分观点）", basis="应结合是否造成公众混淆判断保护范围")])],
        distinctions=[D("名称权", "法人或非法人组织的名称权"), D("肖像权", "对肖像利益的支配权")],
        misconceptions=[dict(claim="可以随便改名", correction="变更姓名须依法办理登记，且不得违背公序良俗"),
                        dict(claim="重名就是侵权", correction="姓名权保护不以 exclusivity 为前提，需结合使用场景判断")],
    ),
    "civil-estate-administrator": dict(
        definition_source="《中华人民共和国民法典》第一千一百四十五条至第一千一百四十九条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["产生方式", "职责范围", "责任承担", "报酬"],
        conditions=["继承开始后需要管理遗产", "由遗嘱指定、继承人推选或法院指定产生"],
        effects=["清理、管理、保护遗产", "处理被继承人债务与税款", "分割遗产并报告履职情况"],
        exceptions=["遗产管理人可以依法辞任", "因故意或重大过失造成损害的应承担民事责任"],
        cases=[],
        controversies=[dict(issue="遗产管理人的法律地位",
                            views=[dict(holder="代理人说", basis="遗产管理人代理继承人与债权人处理事务"),
                                   dict(holder="独立职务说（部分学者）", basis="遗产管理人是依法独立的职务主体，以自己名义履职")])],
        distinctions=[D("遗嘱执行人", "依遗嘱指定执行遗嘱事务"), D("遗产管理人", "更广泛的遗产清理与管理职责")],
        misconceptions=[dict(claim="遗产管理人须为继承人", correction="可由遗嘱指定、继承人推选或法院指定，不必是继承人"),
                        dict(claim="遗产管理人无需承担责任", correction="因故意或重大过失造成损害的应承担民事责任")],
    ),
    "civil-contract-preservation": dict(
        definition_source="《中华人民共和国民法典》第五百三十五条至第五百四十二条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["代位权", "撤销权", "债权人的债权", "债务人的行为"],
        conditions=["债权人对债务人的债权合法且到期", "债务人怠于行使权利或不当处分财产影响债权实现"],
        effects=["债权人可请求次债务人向自己履行", "可请求撤销债务人的不当处分行为", "行使范围以债权为限"],
        exceptions=["专属于债务人自身的权利不得代位", "撤销权须在知道或应当知道撤销事由之日起一年内行使"],
        cases=[],
        controversies=[dict(issue="代位权行使的效果归属",
                            views=[dict(holder="直接受领说（现行法）", basis="次债务人向债权人履行，债权人直接受偿"),
                                   dict(holder="入库说（部分学者）", basis="代位权行使所得应归入债务人责任财产，供全体债权人平等受偿")])],
        distinctions=[D("债的保全", "维持债务人责任财产"), D("债的担保", "增强特定债权实现保障")],
        misconceptions=[dict(claim="代位权可以针对任何债务人权利", correction="专属于债务人自身的权利不得代位行使"),
                        dict(claim="撤销权没有时间限制", correction="撤销权有法定除斥期间，逾期消灭")],
    ),
    "civil-good-faith": dict(
        definition_source="《中华人民共和国民法典》第七条、第五百零九条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["诚实不欺", "恪守承诺", "善意行使权利", "履行附随义务"],
        conditions=["民事主体从事民事活动", "存在权利行使或义务履行的具体情境"],
        effects=["可作为解释、补充与限制权利的依据", "违反诚信可能构成违约或侵权", "法院可依诚信原则调整当事人权利义务"],
        exceptions=["诚信原则的适用不得排除法律强制性规定", "具体化适用需结合个案"],
        cases=["case-riggs"],
        controversies=[dict(issue="诚信原则能否作为独立裁判依据",
                            views=[dict(holder="具体化适用说（通说）", basis="诚信原则应通过具体规则适用，不宜直接作为裁判依据"),
                                   dict(holder="直接适用说（部分学者）", basis="在无具体规则时可依诚信原则直接裁判")])],
        distinctions=[D("公平原则", "强调利益均衡"), D("公序良俗", "强调公共秩序与道德")],
        misconceptions=[dict(claim="诚信只是道德要求", correction="诚信是民法典明文规定的基本原则，具有法律约束力"),
                        dict(claim="任何不诚信行为都可撤销合同", correction="须符合欺诈、胁迫等法定要件方可撤销")],
    ),
}