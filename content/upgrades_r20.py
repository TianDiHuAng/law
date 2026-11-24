# -*- coding: utf-8 -*-
"""R20 体检轮附加升级：3 条重要条目。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R20 = {
    "admin-administrative-confirmation": dict(
        definition_source="行政法学通说及《中华人民共和国行政诉讼法》关于行政行为审查的规定（版本：2017年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["行政主体", "特定法律事实或法律关系", "认定与证明", "宣告"],
        conditions=["行政机关具有法定确认职权", "事实或关系依法需要确认", "遵守法定程序"],
        effects=["确认结果对后续行政与民事关系具有证明力", "错误确认可依法撤销", "造成损害的可申请行政赔偿"],
        exceptions=["纯技术鉴定不属于行政确认", "行政机关内部确认行为原则上不可诉"],
        cases=[],
        controversies=[dict(issue="行政确认是否具有创设权利效力",
                            views=[dict(holder="宣示说（通说）", basis="行政确认仅对既有事实或关系予以认定，不创设权利"),
                                   dict(holder="形成说（部分观点）", basis="某些确认行为对权利状态具有形成作用")])],
        distinctions=[D("行政许可", "许可赋予从事特定活动的资格"), D("行政登记", "登记侧重信息公示与形式审查")],
        misconceptions=[dict(claim="行政确认就是行政许可", correction="确认是对既有事实或关系的认定，许可赋予新资格"),
                        dict(claim="行政确认不能起诉", correction="对确认行为不服可依法申请复议或提起行政诉讼")],
    ),
    "data-personal-portability": dict(
        definition_source="《中华人民共和国个人信息保护法》第四十五条（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["个人信息", "可携带权", "指定处理者", "转移途径"],
        conditions=["个人提出请求", "符合国家网信部门规定条件", "信息属于可携带范围"],
        effects=["处理者应提供转移途径", "个人可选择将信息转移至其他处理者", "处理者不得设置不合理障碍"],
        exceptions=["法律、行政法规规定的例外", "技术条件不具备时的合理处理"],
        cases=[],
        controversies=[dict(issue="可携带权与商业秘密、他人权利的关系",
                            views=[dict(holder="个人控制优先说", basis="增强个人对信息的控制，促进数据流通"),
                                   dict(holder="权利平衡说（部分学者）", basis="行使可携带权不得损害他人合法权益与商业秘密")])],
        distinctions=[D("查阅复制权", "获取个人信息副本"), D("删除权", "请求删除个人信息")],
        misconceptions=[dict(claim="可携带权可以转移所有个人信息", correction="须符合法定条件与可携带范围"),
                        dict(claim="处理者可以拒绝提供转移途径", correction="符合条件时处理者应提供转移途径")],
    ),
    "env-wetland": dict(
        definition_source="《中华人民共和国湿地保护法》（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["湿地", "湿地保护规划", "湿地分级管理", "占用审批", "生态修复"],
        conditions=["属于湿地保护范围", "建设项目占用重要湿地须依法审批", "遵守湿地保护规划"],
        effects=["湿地纳入保护体系", "违法占用湿地承担法律责任", "破坏湿地应依法修复"],
        exceptions=["因公共利益确需占用重要湿地的，应依法办理审批并修复"],
        cases=[],
        controversies=[dict(issue="湿地保护与合理利用的边界",
                            views=[dict(holder="严格保护说", basis="重要湿地应严格保护，限制开发活动"),
                                   dict(holder="合理利用说（部分观点）", basis="在不损害生态功能前提下可适度开展生态旅游与利用")])],
        distinctions=[D("湿地保护", "保护湿地生态系统"), D("土地利用", "土地开发与用途管制")],
        misconceptions=[dict(claim="湿地只是荒滩", correction="湿地具有重要生态功能，受法律保护"),
                        dict(claim="占用湿地只要补偿就可以", correction="须依法审批并落实生态修复责任")],
    ),
}
