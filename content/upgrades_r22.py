# -*- coding: utf-8 -*-
"""R22 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R22 = {
    "crim-prosecution": dict(
        definition_source="《中华人民共和国刑事诉讼法》审查起诉程序（版本：2018年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["受理案件", "审查证据", "讯问犯罪嫌疑人", "听取辩护人意见", "决定起诉或不起诉"],
        conditions=["侦查终结移送起诉", "检察院具有管辖权", "证据达到起诉条件"],
        effects=["提起公诉或作出不起诉决定", "退回补充侦查", "对不起诉决定可申请复议、复核"],
        exceptions=["犯罪情节轻微不需要判处刑罚的可不起诉", "证据不足的可退回补充侦查或存疑不起诉"],
        cases=[],
        controversies=[dict(issue="不起诉权的监督",
                            views=[dict(holder="检察监督说", basis="不起诉决定应接受上级检察院与被害人监督"),
                                   dict(holder="司法审查说（部分观点）", basis="法院应对重大不起诉决定进行司法审查")])],
        distinctions=[D("审查起诉", "检察院审查侦查结果"), D("提起公诉", "检察院向法院提出指控")],
        misconceptions=[dict(claim="检察院不起诉等于无罪", correction="不起诉是程序处理，不等于法院判决无罪"),
                        dict(claim="被害人对不起诉没有救济", correction="被害人可依法申诉或向法院提起自诉")],
    ),
    "crim-plea": dict(
        definition_source="《中华人民共和国刑事诉讼法》认罪认罚从宽制度（版本：2018年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["自愿认罪", "认罚", "从宽处理", "律师帮助", "具结书"],
        conditions=["犯罪嫌疑人、被告人自愿如实供述", "承认指控犯罪事实", "愿意接受处罚", "签署具结书"],
        effects=["检察机关提出从宽量刑建议", "法院一般应当采纳量刑建议（法定例外除外）", "程序可适用速裁、简易程序"],
        exceptions=["被告人不构成犯罪或不应当追究刑事责任", "违背意愿认罪认罚", "否认指控事实"],
        cases=[],
        controversies=[dict(issue="认罪认罚的自愿性保障",
                            views=[dict(holder="程序保障说", basis="值班律师、具结书、庭审审查共同保障自愿性"),
                                   dict(holder="实质审查说（部分学者）", basis="应加强法院对认罪认罚自愿性与事实基础的实质审查")])],
        distinctions=[D("认罪认罚从宽", "实体从宽与程序从简"), D("自首", "自动投案并如实供述")],
        misconceptions=[dict(claim="认罪认罚就一定判缓刑", correction="从宽幅度依案件情况依法确定，不必然缓刑"),
                        dict(claim="认罪认罚后不能上诉", correction="被告人仍依法享有上诉权")],
    ),
    "crim-death-review": dict(
        definition_source="《中华人民共和国刑事诉讼法》死刑复核程序（版本：2018年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["死刑立即执行案件", "最高人民法院核准", "讯问被告人", "听取辩护律师意见"],
        conditions=["中级人民法院判处死刑立即执行", "高级人民法院复核后报请最高人民法院核准", "案件事实清楚、证据确实充分"],
        effects=["核准死刑或不予核准", "不予核准的可发回重审或改判", "核准后依法执行"],
        exceptions=["死刑缓期执行案件由高级人民法院核准", "依法不适用死刑的对象（未成年人、怀孕妇女等）"],
        cases=["case-nie"],
        controversies=[dict(issue="死刑复核程序的诉讼化",
                            views=[dict(holder="诉讼化改造说", basis="应增强控辩双方参与，保障被告人辩护权"),
                                   dict(holder="内部审查说（部分实务观点）", basis="死刑复核是法院内部监督程序，应保持效率")])],
        distinctions=[D("死刑复核", "对死刑判决的特别核准程序"), D("二审", "对未生效判决的普通救济程序")],
        misconceptions=[dict(claim="死刑判决二审后立即执行", correction="死刑立即执行须经最高人民法院核准"),
                        dict(claim="死刑复核不听取律师意见", correction="复核时应讯问被告人并听取辩护律师意见")],
    ),
    "com-company-liquidation": dict(
        definition_source="《中华人民共和国公司法》公司解散和清算的规定（版本：2023年修订，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["解散事由", "清算义务人", "清算组", "债权申报", "剩余财产分配"],
        conditions=["公司依法解散", "在法定期限内成立清算组", "依法通知债权人并公告"],
        effects=["公司进入清算程序", "清算期间公司存续但不得开展与清算无关的经营活动", "清算结束后办理注销登记"],
        exceptions=["公司因合并、分立解散的无需清算", "人民法院指定清算组进行清算"],
        cases=[],
        controversies=[dict(issue="清算义务人怠于清算的责任",
                            views=[dict(holder="连带责任说", basis="清算义务人怠于履行义务造成债权人损失的应承担连带责任"),
                                   dict(holder="过错责任说（部分学者）", basis="应依过错程度与因果关系确定责任范围")])],
        distinctions=[D("解散", "公司终止的原因"), D("破产清算", "资不抵债时的特别清算程序")],
        misconceptions=[dict(claim="公司不注销就自动消失", correction="公司解散后应依法清算并办理注销登记"),
                        dict(claim="清算期间公司可以继续正常经营", correction="清算期间不得开展与清算无关的经营活动")],
    ),
}
