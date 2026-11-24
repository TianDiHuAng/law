# -*- coding: utf-8 -*-
"""R47 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R47 = {
    "data-personal-portability": dict(
        definition_source="《中华人民共和国个人信息保护法》第四十五条第三款（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["请求主体", "可携带的信息", "指定接收方", "转移途径"],
        conditions=["由个人提出请求", "符合国家网信部门规定条件", "信息属于可携带范围"],
        effects=["处理者应提供转移途径", "个人可将信息转移至其他处理者", "处理者不得设置不合理障碍"],
        exceptions=["法律、行政法规规定的例外", "技术上不具备可行性时的合理处理"],
        cases=[],
        controversies=[dict(issue="可携带权的实现方式",
                            views=[dict(holder="直接转移说", basis="处理者应直接向指定接收方传输数据"),
                                   dict(holder="副本提供说（部分观点）", basis="提供机器可读副本即可，由个人自行转移")])],
        distinctions=[D("查阅复制权", "获取个人信息副本"), D("删除权", "请求删除个人信息")],
        misconceptions=[dict(claim="可携带权可以转移全部个人信息", correction="须符合法定条件与可携带范围"),
                        dict(claim="处理者可以技术不兼容为由一概拒绝", correction="应在合理范围内提供可互操作的转移途径")],
    ),
    "data-right-to-erasure": dict(
        definition_source="《中华人民共和国个人信息保护法》第四十七条（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["删除请求", "法定删除情形", "主动删除义务", "通知接收方"],
        conditions=["处理目的已实现、无法实现或为实现目的不再必要", "处理者停止提供产品或服务", "个人撤回同意", "处理者违法或违约处理", "法律规定的其他情形"],
        effects=["处理者应主动删除", "应通知接收方删除", "无法删除的应停止处理并采取必要安全保护措施"],
        exceptions=["法律、行政法规规定的保存期限未届满", "删除技术上难以实现的，可采取必要安全保护措施"],
        cases=[],
        controversies=[dict(issue="删除权与被遗忘权的区别",
                            views=[dict(holder="区别说（通说）", basis="删除权针对处理者持有的信息，被遗忘权还涉及搜索引擎索引"),
                                   dict(holder="功能重合说（部分学者）", basis="二者在效果上高度重合，可统一理解")])],
        distinctions=[D("更正权", "请求更正不准确信息"), D("删除权", "请求删除个人信息")],
        misconceptions=[dict(claim="提出删除请求后处理者必须立即删除", correction="存在法定保存期限等例外情形"),
                        dict(claim="删除权可以要求删除他人发布的信息", correction="删除权针对个人信息处理者，不直接约束其他用户")],
    ),
    "data-data-breach": dict(
        definition_source="《中华人民共和国个人信息保护法》第五十七条（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["泄露、篡改、丢失", "立即补救措施", "通知监管部门", "通知个人"],
        conditions=["发生或可能发生个人信息泄露、篡改、丢失", "可能对个人权益造成影响"],
        effects=["处理者应立即采取补救措施", "应通知履行个人信息保护职责的部门和个人", "通知应说明相关情况与补救措施"],
        exceptions=["处理者采取措施能够有效避免信息泄露造成危害的，可不通知个人（监管部门认为有必要的除外）"],
        cases=[],
        controversies=[dict(issue="通知个人的门槛",
                            views=[dict(holder="可能影响说（现行法）", basis="可能对个人权益造成影响即应通知"),
                                   dict(holder="实际损害说（部分实务观点）", basis="应以实际造成损害为通知门槛，避免通知疲劳")])],
        distinctions=[D("数据泄露通知", "面向监管与个人的事后告知"), D("安全事件报告", "网络安全的报告义务")],
        misconceptions=[dict(claim="信息泄露只要内部处理即可", correction="达到法定条件应通知监管部门与个人"),
                        dict(claim="通知个人会暴露漏洞所以可以不通知", correction="法律明确要求在符合条件时通知")],
    ),
    "data-important-data": dict(
        definition_source="《中华人民共和国数据安全法》第二十一条及重要数据相关标准（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["重要数据认定", "安全负责人", "风险评估", "出境安全评估"],
        conditions=["数据属于行业主管部门确定的重要数据目录范围", "处理者处理重要数据"],
        effects=["应明确数据安全负责人与管理机构", "应定期开展风险评估并报送报告", "出境须依法进行安全评估"],
        exceptions=["行业主管部门另有规定的", "依法无需评估的情形"],
        cases=[],
        controversies=[dict(issue="重要数据与个人信息的界分",
                            views=[dict(holder="分别规制说", basis="重要数据侧重国家安全，个人信息侧重个人权益，分别适用不同规则"),
                                   dict(holder="交叉规制说（部分学者）", basis="大规模个人信息可能同时构成重要数据，应建立衔接规则")])],
        distinctions=[D("重要数据", "危害国家安全与公共利益的数据"), D("个人信息", "可识别特定自然人的信息")],
        misconceptions=[dict(claim="重要数据等于涉密数据", correction="重要数据与国家秘密不同，认定标准由行业目录确定"),
                        dict(claim="中小企业不涉及重要数据", correction="只要处理目录内数据即负有相应义务")],
    ),
}