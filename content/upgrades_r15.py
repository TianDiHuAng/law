# -*- coding: utf-8 -*-
"""R15 体检轮附加升级：2 条重要条目。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R15 = {
    "data-classification": dict(
        definition_source="《中华人民共和国数据安全法》第二十一条及数据分类分级相关国家标准（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["数据分类", "数据分级", "重要数据", "核心数据", "保护义务"],
        conditions=["依据数据重要程度与危害程度分类分级", "行业主管部门制定重要数据目录", "数据处理者落实分级保护措施"],
        effects=["确定数据安全保护等级", "重要数据与核心数据适用更严格保护", "违反分类分级义务可能承担法律责任"],
        exceptions=["涉及国家秘密的数据依照保密法律法规管理", "个人信息同时适用个人信息保护法"],
        cases=[],
        controversies=[dict(issue="重要数据目录的制定主体与范围",
                            views=[dict(holder="行业主管部门主导说", basis="各行业数据特性差异大，应由行业部门制定目录"),
                                   dict(holder="统一目录说（部分学者）", basis="应建立全国统一的重要数据认定标准，避免碎片化")])],
        distinctions=[D("数据分类", "按属性与用途分类"), D("数据分级", "按重要程度与危害程度分级")],
        misconceptions=[dict(claim="所有数据都要按最高等级保护", correction="应根据分类分级结果采取相应保护措施"),
                        dict(claim="数据分类分级是一次性工作", correction="应随业务、法规与风险变化动态调整")],
    ),
    "intl-human-rights-treaties": dict(
        definition_source="《世界人权宣言》《公民权利和政治权利国际公约》《经济、社会及文化权利国际公约》及专门人权公约（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["核心人权公约", "专门人权公约", "缔约国义务", "条约机构", "个人来文"],
        conditions=["国家批准或加入公约", "公约对当事国生效", "用尽国内救济（个人来文程序）"],
        effects=["缔约国承担报告与实施义务", "条约机构发布一般性意见与结论性意见", "个人来文可触发国际审查"],
        exceptions=["公约允许的保留与克减", "联邦制国家对联邦组成部分的适用安排"],
        cases=[],
        controversies=[dict(issue="条约机构一般性意见的法律效力",
                            views=[dict(holder="软法说（主流）", basis="一般性意见不具正式拘束力，但对公约解释具有权威指导作用"),
                                   dict(holder="权威解释说（部分学者）", basis="条约机构是公约监督机构，其解释应具有高度权威")])],
        distinctions=[D("国际人权法", "国际人权公约体系是其核心渊源"), D("国际人道法", "人道法适用于武装冲突")],
        misconceptions=[dict(claim="批准公约后国内法自动修改", correction="各国需通过立法或司法途径实施公约义务"),
                        dict(claim="条约机构可以直接判决国内案件", correction="条约机构主要审查报告与个人来文，不能直接执行国内判决")],
    ),
}


UPGRADES_R15["admin-hearing"] = dict(
    definition_source="《中华人民共和国行政处罚法》听证程序规定及《行政许可法》听证规定（核对日期：2026-11-24；具体条文号待核实）。",
    elements=["听证告知", "当事人申请", "听证会", "听证笔录"],
    conditions=["属于法定听证范围", "当事人依法提出申请", "行政机关依法组织听证"],
    effects=["行政机关应充分听取当事人意见", "听证笔录作为作出决定的重要依据", "未依法听证可能构成程序违法"],
    exceptions=["当事人放弃听证权利", "涉及国家秘密、商业秘密或个人隐私的依法不公开听证"],
    cases=[],
    controversies=[dict(issue="听证程序对行政决定的影响", views=[dict(holder="程序保障说", basis="听证保障当事人陈述申辩权，提升决定可接受性"), dict(holder="效率优先说（部分观点）", basis="听证增加行政成本，应限定适用范围")])],
    distinctions=[dict(**{"with": "行政复议", "difference": "听证是作出决定前的程序，复议是对已作出行为的救济"}), dict(**{"with": "座谈会", "difference": "听证具有法定程序效力，座谈会多为征求意见"})],
    misconceptions=[dict(claim="所有行政处罚都必须听证", correction="只有法定较大数额罚款、吊销许可证等情形才适用听证"), dict(claim="听证只是走形式", correction="未依法听证可能导致行政行为被撤销")],
)
