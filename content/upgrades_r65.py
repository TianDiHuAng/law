# -*- coding: utf-8 -*-
"""R65 体检轮附加升级：国际法 2 条高价值补充条目。"""


def D(w, d):
    return {"with": w, "difference": d}


def _l2(src, elements, conditions, effects, exceptions, controversies, distinctions, misconceptions):
    return dict(definition_source=src, elements=elements, conditions=conditions, effects=effects,
                exceptions=exceptions, cases=[], controversies=controversies,
                distinctions=distinctions, misconceptions=misconceptions)


UPGRADES_R65 = {
    "intl-state-responsibility": _l2(
        "《国家对国际不法行为的责任条款草案》（2001年联合国国际法委员会通过）及国际法院实践（核对日期：2026-11-24）。",
        ["国际不法行为", "归属", "违反国际义务", "法律后果", "援引与反措施"],
        ["存在作为或不作为", "行为可归因于国家", "构成对国际义务的违反"],
        ["停止不法行为并保证不重犯", "充分赔偿（恢复原状、金钱赔偿、抵偿）", "严重违反强行法时产生加重后果"],
        ["同意、自卫、反措施、不可抗力、危难、危急情况等可排除不法性", "反措施须符合比例并不得使用武力"],
        [dict(issue="赔偿方式的选择顺序",
               views=[dict(holder="恢复原状优先说（条款草案倾向）", basis="能恢复原状的应优先恢复原状"),
                      dict(holder="金钱赔偿优先说（实务倾向）", basis="恢复原状不可行或不合理时以金钱赔偿为主")])],
        [D("国家责任", "国家违反国际义务的责任"), D("个人刑事责任", "个人犯罪的责任")],
        [dict(claim="国家责任只限于赔偿", correction="还包括停止、保证不重犯与抵偿等后果"),
         dict(claim="任何情形下违反义务都构成不法行为", correction="存在同意、自卫等排除不法性的情形")],
    ),
    "intl-humanitarian-law": _l2(
        "1949年日内瓦四公约及1977年两个附加议定书（核对日期：2026-11-24）。",
        ["区分原则", "比例原则", "军事必要", "预防措施", "受保护人员"],
        ["存在国际性或非国际性武装冲突", "行为主体为冲突一方", "所涉行为落入人道法调整范围"],
        ["冲突各方须遵守人道法义务", "严重违反构成战争罪", "受保护人员享有免受攻击与虐待的权利"],
        ["军事目标可依法攻击，但须遵守区分与比例", "人道法不禁止一切暴力，只限制作战手段与方法"],
        [dict(issue="非国际性武装冲突的适用",
               views=[dict(holder="共同第三条底线说", basis="非国际性冲突至少适用共同第三条的基本保护"),
                      dict(holder="扩展适用说（部分观点）", basis="第二附加议定书标准应逐步适用于更多非国际性冲突")])],
        [D("国际人道法", "限制作战手段与方法"), D("国际人权法", "平时与战时均适用的人权保护")],
        [dict(claim="人道法禁止一切战争", correction="人道法调整而非禁止战争，旨在限制其残酷性"),
         dict(claim="反恐行动不受人道法约束", correction="符合武装冲突门槛的反恐行动仍受人道法约束")],
    ),
}