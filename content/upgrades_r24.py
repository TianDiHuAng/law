# -*- coding: utf-8 -*-
"""R24 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R24 = {
    "civil-inheritance": dict(
        definition_source="《中华人民共和国民法典》第六编继承（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["法定继承", "遗嘱继承", "遗赠", "遗赠扶养协议", "遗产处理"],
        conditions=["被继承人死亡", "遗产范围确定", "继承人具有继承资格"],
        effects=["继承人依法取得遗产", "遗产债务在遗产范围内清偿", "放弃继承产生相应法律后果"],
        exceptions=["遗嘱继承优先于法定继承", "遗赠扶养协议优先于遗嘱继承和法定继承", "丧失继承权的情形"],
        cases=["case-luzhou", "case-riggs"],
        controversies=[dict(issue="遗产债务清偿与继承人利益保护",
                            views=[dict(holder="限定继承说", basis="继承人以所得遗产实际价值为限清偿被继承人债务"),
                                   dict(holder="债权人优先说（部分观点）", basis="应保障债权人先于继承人受偿")])],
        distinctions=[D("遗嘱继承", "依遗嘱确定继承人"), D("法定继承", "依法律规定的顺序与份额继承")],
        misconceptions=[dict(claim="父债子还天经地义", correction="继承人仅在继承遗产范围内承担清偿责任，放弃继承可不承担"),
                        dict(claim="遗嘱可以处分全部遗产", correction="应为缺乏劳动能力又没有生活来源的继承人保留必要份额")],
    ),
    "civil-testate": dict(
        definition_source="《中华人民共和国民法典》第一千一百三十三条至第一千一百四十四条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["遗嘱形式", "遗嘱能力", "遗嘱内容", "遗嘱效力"],
        conditions=["遗嘱人具有完全民事行为能力", "遗嘱意思表示真实", "遗嘱形式符合法律规定"],
        effects=["遗嘱继承按遗嘱内容执行", "遗嘱可变更、撤回", "无效遗嘱不产生效力"],
        exceptions=["受欺诈、胁迫所立遗嘱无效", "伪造、篡改的遗嘱无效", "遗嘱未保留必要份额的部分无效"],
        cases=[],
        controversies=[dict(issue="打印遗嘱与录音录像遗嘱的效力",
                            views=[dict(holder="严格形式说", basis="须严格符合见证人、签名、日期等形式要件"),
                                   dict(holder="实质真实说（部分观点）", basis="只要能证明遗嘱真实意思，形式瑕疵不应一律否定")])],
        distinctions=[D("遗赠", "将遗产赠与国家、集体或法定继承人以外的人"), D("遗赠扶养协议", "以扶养义务换取遗赠的双方协议")],
        misconceptions=[dict(claim="公证遗嘱效力最高", correction="民法典已取消公证遗嘱效力优先，以最后一份合法有效遗嘱为准"),
                        dict(claim="口头遗嘱随时有效", correction="口头遗嘱仅在危急情况下有效，危急情况消除后另立遗嘱的失效")],
    ),
    "civil-product": dict(
        definition_source="《中华人民共和国民法典》第一千二百零二条至第一千二百零七条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["产品", "缺陷", "损害", "生产者/销售者"],
        conditions=["产品存在缺陷", "造成他人损害", "缺陷与损害之间存在因果关系"],
        effects=["生产者承担无过错责任", "销售者承担过错责任", "明知缺陷仍生产销售的可适用惩罚性赔偿"],
        exceptions=["未将产品投入流通", "产品投入流通时缺陷尚不存在", "科学技术水平尚不能发现缺陷存在"],
        cases=[],
        controversies=[dict(issue="产品缺陷的认定标准",
                            views=[dict(holder="不合理危险说", basis="产品存在危及人身、财产安全的不合理危险即构成缺陷"),
                                   dict(holder="国家标准说（部分实务观点）", basis="符合国家标准的产品原则上不应认定缺陷")])],
        distinctions=[D("产品责任", "因产品缺陷造成的侵权责任"), D("产品质量责任", "包括合同责任与行政责任")],
        misconceptions=[dict(claim="产品有缺陷就一定由生产者赔偿", correction="销售者有过错也承担相应责任，生产者可依法抗辩"),
                        dict(claim="所有产品责任都可惩罚性赔偿", correction="惩罚性赔偿以明知缺陷仍生产销售等法定情形为限")],
    ),
    "civil-tort-strict": dict(
        definition_source="《中华人民共和国民法典》第一千一百六十六条及特殊侵权责任条款（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["法律规定", "无过错责任", "损害", "因果关系"],
        conditions=["属于法律规定的无过错责任情形", "造成他人损害", "行为与损害之间存在因果关系"],
        effects=["不论行为人有无过错均承担侵权责任", "免责事由由法律严格限定", "赔偿范围依法确定"],
        exceptions=["不可抗力", "受害人故意", "法律规定的其他免责事由"],
        cases=[],
        controversies=[dict(issue="无过错责任的归责基础",
                            views=[dict(holder="危险责任说", basis="从事高风险活动者应承担由此产生的损害"),
                                   dict(holder="报偿责任说（部分学者）", basis="从危险活动中获利者应承担相应责任")])],
        distinctions=[D("过错责任", "以行为人过错为要件"), D("过错推定", "先推定过错，由行为人举证免责")],
        misconceptions=[dict(claim="无过错责任就是没有任何免责", correction="法律仍规定不可抗力、受害人故意等免责事由"),
                        dict(claim="所有侵权都适用无过错责任", correction="无过错责任仅限法律明确规定的情形")],
    ),
}
