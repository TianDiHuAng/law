# -*- coding: utf-8 -*-
"""R34 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R34 = {
    "history-zhou": dict(
        definition_source="《中国大百科全书·法学》及中国法制史通说（核对日期：2026-11-24）；参考中文维基百科“周礼”条目。",
        elements=["礼", "刑", "宗法制", "分封制", "礼刑关系"],
        conditions=["适用于西周宗法分封体制", "以礼调整贵族内部关系，以刑惩治违礼与犯罪"],
        effects=["确立等级化的规范秩序", "形成礼法结合的早期传统", "影响后世中华法系"],
        exceptions=["“礼不下庶人、刑不上大夫”体现身份差异", "具体制度在不同时期有变化"],
        cases=[],
        controversies=[dict(issue="礼是否具有法的性质",
                            views=[dict(holder="礼即法说（部分学者）", basis="礼具有强制约束力并由国家保障实施，具有法的属性"),
                                   dict(holder="礼刑分立说（通说）", basis="礼主要靠教化与舆论，刑才是国家强制制裁")])],
        distinctions=[D("唐律疏议", "礼法结合的成熟法典"), D("秦律", "以法家思想为指导的严密成文法")],
        misconceptions=[dict(claim="西周只有刑罚没有规范体系", correction="礼构成调整贵族与社会关系的重要规范"),
                        dict(claim="礼刑完全对立", correction="礼刑互补，共同维护宗法秩序")],
    ),
    "history-late-qing": dict(
        definition_source="《中国大百科全书·法学》及中国法制史通说（核对日期：2026-11-24）；参考中文维基百科“清末新政”条目。",
        elements=["修律馆", "新刑律", "民律草案", "审判独立", "罪刑法定"],
        conditions=["清末新政与收回领事裁判权的压力", "沈家本等主持修律", "参照大陆法系起草法典"],
        effects=["中华法系开始解体", "引入近代法律原则与体例", "为民国立法奠定基础"],
        exceptions=["多数草案未及施行清朝即亡", "礼教派与法理派存在激烈争论"],
        cases=[],
        controversies=[dict(issue="清末修律的性质",
                            views=[dict(holder="近代化开端说（通说）", basis="修律引入大陆法系体例与原则，开启法律近代化"),
                                   dict(holder="被动回应说（部分学者）", basis="修律主要为收回治外法权，具有工具性")])],
        distinctions=[D("中华法系", "修律前的传统法律体系"), D("民国立法", "修律成果的延续与发展")],
        misconceptions=[dict(claim="修律彻底废除了传统法律", correction="修律后传统礼制与习惯仍长期影响实务"),
                        dict(claim="修律成果全部实施", correction="多数草案因清亡未及施行")],
    ),
    "civil-property": dict(
        definition_source="《中华人民共和国民法典》第二编物权（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["物权法定", "公示公信", "一物一权", "物权种类", "物权变动"],
        conditions=["物权种类与内容由法律规定", "不动产物权变动依法登记、动产物权变动依法交付"],
        effects=["物权具有排他性与优先性", "登记或交付产生对抗或生效效力", "物权受侵害可行使物权请求权"],
        exceptions=["法律规定的地役权、居住权等特殊物权", "船舶、航空器等动产抵押登记对抗规则"],
        cases=[],
        controversies=[dict(issue="物权行为无因性",
                            views=[dict(holder="有因说（现行法通说）", basis="我国民法典未采纳物权行为无因性理论"),
                                   dict(holder="无因说（部分学者）", basis="应借鉴德国民法区分负担行为与处分行为")])],
        distinctions=[D("债权", "请求特定人为一定行为"), D("物权", "对物的直接支配权")],
        misconceptions=[dict(claim="占有就等于所有权", correction="占有是事实状态，所有权是法律权利"),
                        dict(claim="合同生效即取得所有权", correction="不动产物权须登记、动产须交付才发生变动")],
    ),
    "civil-divorce": dict(
        definition_source="《中华人民共和国民法典》第一千零七十六条至第一千零九十二条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["协议离婚", "诉讼离婚", "离婚冷静期", "子女抚养", "财产分割", "离婚损害赔偿"],
        conditions=["协议离婚须双方自愿并达成书面协议", "诉讼离婚须感情确已破裂且调解无效"],
        effects=["婚姻关系解除", "子女抚养与财产分割依法处理", "无过错方可请求损害赔偿"],
        exceptions=["女方怀孕期间、分娩后一年内或终止妊娠后六个月内男方原则上不得提出离婚", "现役军人配偶离婚须征得军人同意（军人有重大过错的除外）"],
        cases=["case-luzhou"],
        controversies=[dict(issue="离婚冷静期的适用范围",
                            views=[dict(holder="限缩适用说", basis="冷静期仅适用于协议离婚，涉及家暴等情形可通过诉讼离婚"),
                                   dict(holder="扩大适用说（部分观点）", basis="冷静期应设例外，避免延长受害方脱离婚姻的时间")])],
        distinctions=[D("协议离婚", "双方自愿并经登记"), D("诉讼离婚", "由法院判决解除婚姻")],
        misconceptions=[dict(claim="分居满两年自动离婚", correction="分居满两年是感情破裂的法定情形之一，仍需经法定程序"),
                        dict(claim="离婚时房产一律平分", correction="应区分个人财产与共同财产，并照顾子女、女方和无过错方权益")],
    ),
}