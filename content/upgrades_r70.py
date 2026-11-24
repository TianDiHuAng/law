# -*- coding: utf-8 -*-
"""R70 体检轮附加升级：国际法 2 条。"""


def D(w, d):
    return {"with": w, "difference": d}


def _l2(src, elements, conditions, effects, exceptions, controversies, distinctions, misconceptions):
    return dict(definition_source=src, elements=elements, conditions=conditions, effects=effects,
                exceptions=exceptions, cases=[], controversies=controversies,
                distinctions=distinctions, misconceptions=misconceptions)


UPGRADES_R70 = {
    "intl-sanctions": _l2(
        "《联合国宪章》第七章（第四十一条）及安理会制裁决议实践（核对日期：2026-11-24）。",
        ["安理会制裁", "单边制裁", "定向制裁", "执行与人道豁免"],
        ["存在对和平与安全的威胁", "安理会依第七章作出决议", "成员国履行决议义务"],
        ["成员国应执行安理会制裁决议", "可采取经济、旅行、资产等限制措施", "设置人道主义豁免与除名机制"],
        ["人道主义豁免与基本生活保障", "除名与救济程序保障被列名者权利"],
        [dict(issue="单边制裁的合法性",
               views=[dict(holder="原则违法说", basis="未经安理会授权的单边制裁缺乏国际法依据，涉及域外管辖争议"),
                      dict(holder="反措施说（部分观点）", basis="在特定情形下可作为反措施具有有限合法性")])],
        [D("国际制裁", "国际组织或国家的强制措施"), D("国内处罚", "一国对内违法行为的制裁")],
        [dict(claim="任何国家都可任意制裁他国", correction="单边制裁的合法性存在争议，须符合国际法"),
         dict(claim="制裁决议不需成员国执行", correction="成员国负有履行安理会决议的义务")],
    ),
    "intl-interim-measures": _l2(
        "主要仲裁规则（如 UNCITRAL 仲裁规则）与《纽约公约》体系（核对日期：2026-11-24）。",
        ["财产保全", "证据保全", "行为保全", "紧急性临时措施", "执行"],
        ["仲裁程序已启动或即将启动", "存在使裁决难以执行的现实风险", "申请人提供担保"],
        ["仲裁庭可作出临时措施命令", "可依仲裁地法或法院协助执行", "违反措施可能影响最终裁决"],
        ["紧急性临时措施可在通知对方前作出（须迅速审查）", "法院亦可依申请采取保全措施"],
        [dict(issue="仲裁庭临时措施的可执行性",
               views=[dict(holder="有限可执行说", basis="依仲裁地法与纽约公约体系，部分临时措施可获承认执行"),
                      dict(holder="需法院协助说（部分观点）", basis="仲裁庭缺乏强制力，多依赖法院协助执行")])],
        [D("临时措施", "裁决前的临时救济"), D("最终裁决", "确定实体权利义务")],
        [dict(claim="仲裁庭的临时措施自动具有强制力", correction="其执行力依赖仲裁地法与法院协助"),
         dict(claim="申请临时措施无需担保", correction="通常需提供担保以平衡双方利益")],
    ),
}