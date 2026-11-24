# -*- coding: utf-8 -*-
"""R28 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R28 = {
    "u02": [
        E("admin-agreement-rules", "行政协议案件审理规则", "concept", "重要", "中国", "行政法学·行政协议诉讼",
          "行政协议案件审理规则是人民法院审理因行政协议订立、履行、变更、解除等引发的争议时，在受案范围、管辖、举证责任、法律适用与判决方式上的特别规则。",
          "审理行政协议案件应优先适用行政法律规范，并可参照适用民事法律规范；行政机关对行使优益权等行为的合法性承担举证责任。",
          ["src-law-admin-litigation", "src-zgbk"], related=["admin-administrative-agreement", "admin-litigation", "civil-contract"],
          pending="最高人民法院关于审理行政协议案件若干问题的规定的具体条文需按现行文本核对。", needs_verification=True),
        E("court-organization", "人民法院组织与审判制度", "concept", "重要", "中国", "司法制度·法院组织",
          "人民法院组织与审判制度规定人民法院的设置、审判组织、审判人员职责与审判原则，依据宪法和人民法院组织法。",
          "人民法院依法独立行使审判权，实行两审终审、公开审判、合议与独任审判、回避、辩护与陪审等制度。",
          ["src-law-constitution", "src-court-gongbao", "src-zgbk"], related=["const-state-organs", "crim-trial", "proc-civil-trial"]),
    ],
    "u03": [
        E("civil-contract-termination", "合同解除", "concept", "重要", "中国", "民法·合同权利义务终止",
          "合同解除是合同有效成立后，因法定或约定事由出现，当事人一方或双方使合同关系归于消灭的行为，分为协议解除、约定解除与法定解除。",
          "法定解除事由包括不可抗力致使不能实现合同目的、预期违约、迟延履行经催告仍不履行、根本违约等；解除权须在法定期限内行使。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-contract-liability", "civil-contract-preservation"]),
    ],
    "u07": [
        E("data-cross-border-cases", "数据跨境流动的典型情形", "concept", "补充", "中国", "数据法·数据跨境",
          "数据跨境流动的典型情形包括跨国公司集团内部管理、境外提供服务、跨境并购与尽职调查、境外上市与监管报送、跨境物流与支付等。",
          "不同情形对应不同的出境路径与合规要求，处理者应结合数据类别、数量、接收方所在国家或地区与处理目的选择评估、标准合同或认证。",
          ["src-law-personal-info-2", "src-law-data-security", "src-zgbk"], related=["data-cross-border", "data-important-data", "data-pia"],
          pending="各典型情形的监管口径需按国家网信部门发布的问答与指南核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-assistance-cases", "国际刑事司法协助的典型情形", "concept", "补充", "国际", "国际公法·刑事司法合作",
          "国际刑事司法协助的典型情形包括跨境取证与证人询问、资产冻结与追缴、文书送达、引渡、被判刑人移管与刑事诉讼移管。",
          "不同情形适用不同条约与程序；引渡须符合双重犯罪、政治犯不引渡、本国国民不引渡等原则，并受国内法程序约束。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["intl-judicial-assistance", "intl-international-criminal", "crim-investigation"],
          pending="各类协助的条约依据与操作程序需按外交部、司法部官方文本核对。", needs_verification=True),
    ],
}