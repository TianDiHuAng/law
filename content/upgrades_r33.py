# -*- coding: utf-8 -*-
"""R33 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R33 = {
    "theory-right-duty": dict(
        definition_source="《中华人民共和国宪法》第二章及法理学通说（版本：2018年修正，核对日期：2026-11-24）。",
        elements=["权利主体", "权利内容", "义务主体", "义务内容"],
        conditions=["由法律规范确认", "主体具有相应资格", "权利行使不损害他人与社会公共利益"],
        effects=["权利人可请求义务人为或不为一定行为", "权利受侵害可请求法律救济", "义务人须依法履行义务"],
        exceptions=["权利不得滥用原则的限制", "法律规定的权利限制与克减"],
        cases=[],
        controversies=[dict(issue="权利本位与义务本位",
                            views=[dict(holder="权利本位说（现代通说）", basis="法以保障权利为核心，义务服务于权利实现"),
                                   dict(holder="义务本位说（历史与部分观点）", basis="社会连带要求义务优先，尤其在传统法制中")])],
        distinctions=[D("权利", "可为或请求他人为一定行为的资格"), D("义务", "应为或不得为的约束")],
        misconceptions=[dict(claim="权利可以任意行使", correction="权利行使须受不得滥用与公共利益限制"),
                        dict(claim="义务只是道德要求", correction="法律义务由法律确认并可强制执行")],
    ),
    "history-civil-law": dict(
        definition_source="《中国大百科全书·法学》及中国法制史通说（核对日期：2026-11-24）；参考中文维基百科“中华法系”条目。",
        elements=["礼法结合", "以刑为主", "家族本位", "行政司法合一", "律令体系"],
        conditions=["适用于中国古代及受其影响的东亚地区", "以成文律典与礼制规范为核心"],
        effects=["形成独特的律令体系与法律文化", "影响东亚各国法制", "清末修律后逐步解体"],
        exceptions=["中华法系内部各朝代差异明显", "少数民族习惯法自成体系"],
        cases=[],
        controversies=[dict(issue="中华法系是否以刑法为核心",
                            views=[dict(holder="以刑为主说（通说）", basis="律典以刑罚为制裁手段，民事规范多附于刑律"),
                                   dict(holder="综合规范说（部分学者）", basis="礼制与民间习惯承担大量民事调整功能，不能仅以律典判断")])],
        distinctions=[D("大陆法系", "以罗马法为基础、法典化为特征"), D("英美法系", "以判例法为基础")],
        misconceptions=[dict(claim="中华法系没有民法", correction="民事关系主要由礼制、习惯与律典中的相关条款调整"),
                        dict(claim="中华法系已完全消失", correction="其法律文化仍影响当代纠纷解决与法律观念")],
    ),
    "history-civil-law-family": dict(
        definition_source="《中国大百科全书·法学》及比较法通说（核对日期：2026-11-24）；参考中文维基百科“大陆法系”条目。",
        elements=["成文法典", "公法私法划分", "法官适用法律", "法学教育与体系化"],
        conditions=["以罗马法为历史基础", "经中世纪复兴与近代法典化", "在欧陆及受其影响地区适用"],
        effects=["形成系统的法典体系", "影响全球多数国家的私法结构", "与英美法系形成对照"],
        exceptions=["各国法典化程度不同", "欧盟法带来新的超国家法律层次"],
        cases=[],
        controversies=[dict(issue="大陆法系是否排斥判例",
                            views=[dict(holder="成文法唯一渊源说（传统）", basis="法官仅依成文法裁判，判例不具正式拘束力"),
                                   dict(holder="判例事实拘束力说（现代通说）", basis="最高法院判例在实务中具有重要指导作用")])],
        distinctions=[D("英美法系", "以判例法与遵循先例为特征"), D("中华法系", "以礼法结合为特征")],
        misconceptions=[dict(claim="大陆法系法官没有造法空间", correction="法律解释与漏洞填补实质上具有造法功能"),
                        dict(claim="大陆法系只存在于欧洲", correction="拉美、东亚多地均属大陆法系")],
    ),
    "history-common-law-family": dict(
        definition_source="《中国大百科全书·法学》及比较法通说（核对日期：2026-11-24）；参考中文维基百科“英美法系”条目。",
        elements=["判例法", "遵循先例", "衡平法", "制定法", "陪审与对抗制"],
        conditions=["以英国普通法为历史基础", "经殖民与法律移植传播", "法院体系具有统一上诉结构"],
        effects=["判例成为主要法律渊源", "形成对抗制诉讼模式", "与大陆法系形成对照"],
        exceptions=["制定法可推翻判例", "欧盟法曾对英国法产生超国家影响"],
        cases=["case-donoghue"],
        controversies=[dict(issue="英美法系是否正在成文化",
                            views=[dict(holder="成文化趋势说", basis="制定法数量激增，判例法领域相对收缩"),
                                   dict(holder="判例核心说（部分学者）", basis="制定法仍依赖判例解释，判例法仍是核心")])],
        distinctions=[D("大陆法系", "以成文法典为核心"), D("中华法系", "以礼法结合为核心")],
        misconceptions=[dict(claim="英美法系没有成文法", correction="英美法国家有大量制定法"),
                        dict(claim="先例永远不可推翻", correction="上级法院可推翻先例，制定法也可改变判例")],
    ),
}