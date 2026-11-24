# -*- coding: utf-8 -*-
"""R41 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R41 = {
    "u02": [
        E("admin-license-revocation", "行政许可的撤销与撤回", "concept", "补充", "中国", "行政法学·行政许可",
          "行政许可的撤销针对违法作出的许可决定，撤回则针对合法作出但因法律依据修改、客观情况变化而需要终止的许可。",
          "撤销由作出许可决定的行政机关或其上级机关依法定情形作出；撤回许可给被许可人造成财产损失的，行政机关应当依法给予补偿。",
          ["src-law-admin-license", "src-zgbk"], related=["admin-license", "admin-license-hearing", "admin-compensation"],
          pending="行政许可法关于撤销与撤回的具体条文需按现行文本核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-deposit-in-escrow", "提存", "concept", "补充", "中国", "民法·债的消灭",
          "提存是债务人在债权人无正当理由拒绝受领、债权人下落不明等法定情形下，将标的物交付提存机关从而消灭债务的制度。",
          "提存后标的物毁损灭失风险由债权人承担，提存费用由债权人负担；债权人可随时领取提存物，但须履行到期债务或提供担保。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-obligation-extinction", "civil-offset", "civil-contract"]),
    ],
    "u07": [
        E("data-cross-border-whitelist", "数据跨境白名单机制", "concept", "补充", "中国", "数据法·数据跨境",
          "数据跨境白名单是监管机构认定某些国家、地区或特定接收方具备充分数据保护水平，从而允许数据在满足条件时更便利出境的管理机制。",
          "白名单机制可降低企业逐案评估的合规成本；中国目前以安全评估、标准合同与认证为主要出境路径，白名单制度仍在探索中。",
          ["src-law-personal-info-2", "src-law-data-security", "src-zgbk"], related=["data-cross-border", "data-cross-border-cases", "data-pi-certification"],
          pending="中国数据跨境白名单或负面清单制度的立法与实施进展需持续跟踪官方文件。", needs_verification=True),
    ],
    "u08": [
        E("intl-social-security-agreement", "国际社会保障协定", "concept", "补充", "国际", "国际私法·社会保障合作",
          "国际社会保障协定是国家之间为避免双重缴费、保障劳动者跨境流动期间社会保障权益而缔结的双边协议，通常涉及养老、医疗、工伤与失业保险。",
          "协定一般通过出具参保凭证实现缴费豁免，并规定待遇计算与支付、工龄互认与信息交换；中国已与多国签署社会保障协定。",
          ["src-un-treaty", "src-ilo", "src-zgbk"], related=["social-insurance", "intl-private", "intl-treaty"],
          pending="中国已签署社会保障协定的清单与生效状态需按人力资源社会保障部官方资料核对。", needs_verification=True),
    ],
}