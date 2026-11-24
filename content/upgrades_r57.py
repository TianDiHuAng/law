# -*- coding: utf-8 -*-
"""R57 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R57 = {
    "civil-act-effect": dict(
        definition_source="《中华人民共和国民法典》第一百四十三条至第一百五十八条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["有效要件", "无效", "可撤销", "效力待定"],
        conditions=["行为人具有相应民事行为能力", "意思表示真实", "不违反法律、行政法规的强制性规定与公序良俗"],
        effects=["有效行为产生当事人预期的法律效果", "无效行为自始无效", "可撤销行为经撤销后自始无效"],
        exceptions=["违背公序良俗或违反强制性规定的一般无效（强制性规定不导致无效的除外）", "恶意串通损害他人权益的无效"],
        cases=[],
        controversies=[dict(issue="效力性强制性规定与管理性强制性规定的区分",
                            views=[dict(holder="区分说（通说）", basis="只有效力性强制性规定才导致行为无效"),
                                   dict(holder="统合说（部分学者）", basis="应结合规范目的综合判断，不宜机械二分")])],
        distinctions=[D("无效", "自始当然确定不发生效力"), D("可撤销", "须由撤销权人行使撤销权")],
        misconceptions=[dict(claim="合同签字就一定有效", correction="违反强制性规定、违背公序良俗等情形可导致无效"),
                        dict(claim="可撤销合同自动无效", correction="可撤销合同在被撤销前有效，须由撤销权人行使撤销权")],
    ),
    "civil-contract-termination": dict(
        definition_source="《中华人民共和国民法典》第五百六十二条至第五百六十六条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["协议解除", "约定解除", "法定解除", "解除程序", "解除后果"],
        conditions=["出现法定或约定的解除事由", "依法通知或提起诉讼主张解除", "在法定期限内行使解除权"],
        effects=["合同关系终止", "尚未履行的终止履行", "已履行的可请求恢复原状或采取其他补救措施并赔偿损失"],
        exceptions=["解除权因除斥期间届满而消灭", "违约轻微不影响合同目的的不得解除"],
        cases=[],
        controversies=[dict(issue="违约解除的实质条件",
                            views=[dict(holder="根本违约说", basis="只有致使不能实现合同目的的违约方可解除"),
                                   dict(holder="宽严结合说（部分观点）", basis="应结合违约程度与当事人利益综合判断")])],
        distinctions=[D("合同解除", "合同关系提前终止"), D("合同撤销", "因意思表示瑕疵否定效力")],
        misconceptions=[dict(claim="任何违约都能解除合同", correction="须达到法定解除条件，轻微违约一般不能解除"),
                        dict(claim="解除后合同完全无效", correction="解除终止履行，但结算与清理条款仍有效")],
    ),
    "civil-privity": dict(
        definition_source="《中华人民共和国民法典》第四百六十五条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["合同当事人", "第三人利益合同", "相对性突破", "代位与撤销"],
        conditions=["合同依法成立", "原则上仅约束当事人", "法律特别规定可涉第三人"],
        effects=["当事人享有合同权利并承担义务", "第三人一般不享有合同权利", "特定情形下第三人可主张权利或被追究责任"],
        exceptions=["为第三人利益的合同", "买卖不破租赁", "代位权、撤销权", "第三人侵害债权等"],
        cases=[],
        controversies=[dict(issue="第三人侵害债权是否可依侵权救济",
                            views=[dict(holder="否定说（传统）", basis="债权不具公示性，第三人难以知悉，不宜成立侵权"),
                                   dict(holder="有限肯定说（部分学者）", basis="第三人故意以背于善良风俗方式侵害债权的可成立侵权")])],
        distinctions=[D("合同相对性", "合同效力限于当事人"), D("物权绝对性", "对世效力")],
        misconceptions=[dict(claim="合同可以随意约束第三人", correction="合同原则上不约束第三人，例外须有法律规定"),
                        dict(claim="相对性没有任何例外", correction="存在为第三人利益合同、代位权等法定例外")],
    ),
    "civil-guarantee-modes": dict(
        definition_source="《中华人民共和国民法典》第六百八十六条至第六百八十七条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["一般保证", "连带责任保证", "先诉抗辩权", "保证方式推定"],
        conditions=["保证合同有效成立", "明确约定或依法定规则确定保证方式"],
        effects=["一般保证人享有先诉抗辩权", "连带保证人不享有先诉抗辩权", "保证人承担责任后可向债务人追偿"],
        exceptions=["约定不明或没有约定的按一般保证处理", "债务人下落不明且无财产可供执行等情形下先诉抗辩权受限"],
        cases=[],
        controversies=[dict(issue="保证方式约定不明的推定规则",
                            views=[dict(holder="一般保证推定说（现行法）", basis="约定不明时推定为一般保证，倾向保护保证人"),
                                   dict(holder="连带保证推定说（旧法）", basis="原担保法推定连带责任保证，倾向保护债权人")])],
        distinctions=[D("一般保证", "享有先诉抗辩权"), D("连带责任保证", "债权人可直接请求保证人")],
        misconceptions=[dict(claim="保证方式没约定就是连带保证", correction="民法典规定约定不明的按一般保证承担"),
                        dict(claim="一般保证人永远可以拒绝承担责任", correction="先诉抗辩权在法定情形下受限")],
    ),
}