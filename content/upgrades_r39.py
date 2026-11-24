# -*- coding: utf-8 -*-
"""R39 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R39 = {
    "admin-government-procurement": dict(
        definition_source="《中华人民共和国政府采购法》及其实施条例（版本：2014年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["采购人", "供应商", "采购方式", "采购程序", "监督管理"],
        conditions=["使用财政性资金", "采购集中采购目录以内或限额标准以上的货物、工程和服务", "依法确定采购方式"],
        effects=["采购合同依法成立并履行", "违法采购可能导致合同无效或撤销", "供应商可依法质疑投诉"],
        exceptions=["因严重自然灾害等紧急情况可采用单一来源采购", "涉密采购适用特别规定"],
        cases=[],
        controversies=[dict(issue="集中采购与分散采购的边界",
                            views=[dict(holder="集中优先说（现行制度）", basis="纳入集中采购目录的项目必须委托集中采购机构"),
                                   dict(holder="效率优先说（部分观点）", basis="应扩大采购人自主选择空间，提高采购效率")])],
        distinctions=[D("政府采购", "使用财政性资金的采购"), D("企业采购", "市场主体自主采购")],
        misconceptions=[dict(claim="只要价格低就可以直接采购", correction="须依法定采购方式与程序进行"),
                        dict(claim="政府采购不受合同法调整", correction="采购合同同时受政府采购法与合同法规则约束")],
    ),
    "admin-public-health-emergency": dict(
        definition_source="《中华人民共和国突发事件应对法》与《突发公共卫生事件应急条例》（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["监测预警", "应急决策", "处置措施", "信息发布", "恢复重建"],
        conditions=["发生或可能发生突发公共卫生事件", "依法启动相应级别应急响应", "采取措施符合比例原则"],
        effects=["政府可依法采取隔离、封锁、征用等措施", "单位和个人应予配合", "违法采取措施造成损害的可申请救济"],
        exceptions=["紧急状态下的特别措施须有法律依据", "措施应当与事件危害程度相适应"],
        cases=[],
        controversies=[dict(issue="应急措施与公民权利的限制边界",
                            views=[dict(holder="依法应急说", basis="应急措施须有法律依据并遵守比例原则，保障基本权利底线"),
                                   dict(holder="效率优先说（部分观点）", basis="紧急情况下应赋予行政机关更大裁量空间")])],
        distinctions=[D("常态行政管理", "常规行政程序"), D("应急管理", "特殊状态下的特别程序")],
        misconceptions=[dict(claim="应急状态下可以不受法律约束", correction="应急措施仍须有法律依据并接受监督"),
                        dict(claim="应急征用不需要补偿", correction="依法征用应给予补偿")],
    ),
    "court-organization": dict(
        definition_source="《中华人民共和国人民法院组织法》（版本：2018年修订，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["法院设置", "审判组织", "审判人员", "审判原则", "监督机制"],
        conditions=["依法设立法院", "法官依法产生", "审判组织依法组成"],
        effects=["法院依法独立行使审判权", "生效裁判具有既判力与执行力", "审判人员违法履职依法追责"],
        exceptions=["专门法院的设置依特别规定", "审判委员会讨论重大疑难案件"],
        cases=[],
        controversies=[dict(issue="审判委员会与合议庭的关系",
                            views=[dict(holder="讨论决定说（现行制度）", basis="审判委员会对重大疑难案件有讨论决定权"),
                                   dict(holder="咨询说（部分学者）", basis="应强化合议庭独立裁判，审委会限于统一法律适用")])],
        distinctions=[D("法院组织", "审判机关的设置与职权"), D("检察组织", "检察机关的设置与职权")],
        misconceptions=[dict(claim="法官可以任意裁判不受约束", correction="法官须依法裁判并接受监督"),
                        dict(claim="所有案件都由合议庭审理", correction="简易程序与部分案件可适用独任审判")],
    ),
    "admin-reconsideration-prerequisite": dict(
        definition_source="《中华人民共和国行政复议法》（版本：2023年修订，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["法定前置情形", "申请期限", "复议决定", "诉讼衔接"],
        conditions=["属于法律规定复议前置的事项", "在法定期限内申请复议", "对复议决定不服或复议机关逾期不决"],
        effects=["未经复议不得直接起诉", "复议决定成为诉讼审查对象", "复议机关不作为可被起诉"],
        exceptions=["法律另有规定的除外", "复议机关不受理的救济途径依法律规定"],
        cases=[],
        controversies=[dict(issue="复议前置范围扩大的利弊",
                            views=[dict(holder="扩大说（2023年修法取向）", basis="发挥行政复议主渠道作用，实质化解争议"),
                                   dict(holder="选择权说（部分学者）", basis="应保留当事人直接诉讼的选择权")])],
        distinctions=[D("复议前置", "必须先复议"), D("复议选择", "可复议也可直接诉讼")],
        misconceptions=[dict(claim="所有案件都必须先复议", correction="仅法律明确规定的事项适用前置"),
                        dict(claim="复议前置会剥夺诉权", correction="复议后仍可依法提起行政诉讼")],
    ),
}