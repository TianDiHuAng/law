# -*- coding: utf-8 -*-
"""R25 体检轮附加升级：3 条重要条目。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R25 = {
    "civil-possession": dict(
        definition_source="《中华人民共和国民法典》第四百五十八条至第四百六十二条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["占有", "有权占有", "无权占有", "善意占有", "恶意占有"],
        conditions=["对物具有事实上的控制与支配", "占有具有合法依据或事实状态"],
        effects=["占有人可请求返还占有、排除妨害、消除危险", "善意占有人与恶意占有人返还范围不同", "占有保护请求权有除斥期间"],
        exceptions=["基于合同关系的占有依合同处理", "占有辅助人不享有占有保护请求权"],
        cases=[],
        controversies=[dict(issue="占有保護的基礎",
                            views=[dict(holder="事实秩序说", basis="占有保护旨在维护社会和平与事实秩序"),
                                   dict(holder="权利推定说（部分学者）", basis="占有具有权利推定功能，保护占有即保护本权")])],
        distinctions=[D("所有权", "对物的法律支配权"), D("占有", "对物的事实控制")],
    misconceptions=[dict(claim="占有就是所有", correction="占有是事实控制，所有权是法律权利"), dict(claim="恶意占有人不受任何保护", correction="恶意占有人也受占有保护，但返还范围更重")],
    ),
    "civil-tort-online": dict(
        definition_source="《中华人民共和国民法典》第一千一百九十四条至第一千一百九十七条及信息网络侵权司法解释（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["网络用户", "网络服务提供者", "通知规则", "知道或应当知道"],
        conditions=["网络用户利用网络实施侵权行为", "网络服务提供者接到通知未及时采取必要措施", "或明知/应知侵权未采取措施"],
        effects=["网络服务提供者对损害扩大部分承担连带责任", "权利人可要求删除、屏蔽、断开链接", "错误通知造成损失应承担侵权责任"],
        exceptions=["避风港规则：及时采取必要措施可免责", "反通知规则"],
        cases=[],
        controversies=[dict(issue="平台注意义务的边界",
                            views=[dict(holder="通知删除说", basis="平台以通知删除规则为主，避免事前审查"),
                                   dict(holder="主动审查说（部分观点）", basis="平台应利用技术能力主动过滤明显侵权内容")])],
        distinctions=[D("网络侵权", "通过信息网络侵害他人民事权益"), D("传统侵权", "线下实施的侵权行为")],
        misconceptions=[dict(claim="平台对用户发布内容一律负责", correction="平台在符合避风港规则时可不承担责任"), dict(claim="通知删除后平台就完全免责", correction="对明知或应知侵权仍可能承担责任")],
    ),
    "civil-tort-fault": dict(
        definition_source="《中华人民共和国民法典》第一千一百六十五条（版本：2020年通过，核对日期：2026-11-24）。",
        elements=["侵权行为", "过错", "损害", "因果关系"],
        conditions=["行为人实施侵害他人民事权益的行为", "行为人具有故意或过失", "造成损害", "行为与损害有因果关系"],
        effects=["行为人承担侵权责任", "赔偿范围依过错程度与损害确定", "受害人可请求停止侵害、赔偿损失等"],
        exceptions=["正当防卫、紧急避险", "不可抗力", "受害人故意或重大过失"],
        cases=["case-donoghue"],
        controversies=[dict(issue="过错与违法性的关系",
                            views=[dict(holder="过错吸收违法性说", basis="过错判断已包含行为违法性"),
                                   dict(holder="违法性独立说（部分学者）", basis="应区分违法性与过错，分别判断")])],
        distinctions=[D("无过错责任", "不以过错为要件"), D("过错推定", "先推定过错，行为人举证免责")],
        misconceptions=[dict(claim="没有主观恶意就不构成侵权", correction="过失也可能构成过错，重大过失与一般过失均可能承担责任"), dict(claim="受害人有过错就完全不赔", correction="过失相抵可能减轻责任，但不一定完全免除")],
    ),
}
