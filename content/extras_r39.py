# -*- coding: utf-8 -*-
"""R39 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R39 = {
    "u02": [
        E("admin-due-process", "行政程序的正当原则", "concept", "补充", "中国", "行政法学·行政程序",
          "行政程序的正当原则要求行政机关作出影响相对人权益的决定时，遵循公开、公平、公正与参与的基本要求，包括告知、听取意见、说明理由与送达。",
          "正当程序原则在我国由行政处罚法、行政许可法、行政强制法等法律具体化，并在行政审判中作为审查行政行为程序合法性的依据。",
          ["src-law-admin-penalty", "src-law-admin-license", "src-zgbk"],
          related=["admin-principles", "admin-hearing", "admin-litigation"],
          pending="正当程序原则在制定法中的具体表述散见于多部法律，未形成统一程序法典。", needs_verification=True),
    ],
    "u03": [
        E("civil-deposit", "定金", "concept", "重要", "中国", "民法·合同担保",
          "定金是合同当事人约定一方向对方给付一定数额金钱作为债权担保的方式；债务人履行债务后，定金应抵作价款或收回。",
          "给付定金一方不履行债务的，无权请求返还定金；收受定金一方不履行的，应双倍返还定金；定金数额不得超过主合同标的额的百分之二十。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-guarantee", "civil-contract-liability"]),
    ],
    "u07": [
        E("data-pi-certification", "个人信息保护认证", "concept", "补充", "中国", "数据法·个人信息保护",
          "个人信息保护认证是由专业机构依照国家标准对个人信息处理者的处理活动进行评价并出具认证证明的制度。",
          "认证可用于证明处理者合规水平，也是个人信息出境的合法路径之一；认证机构与认证规则须依法取得资质并符合国家标准。",
          ["src-law-personal-info-2", "src-zgbk"], related=["data-personal", "data-cross-border", "data-pi-audit"],
          pending="个人信息保护认证的具体实施规则需按国家市场监管总局、网信办官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-energy-law", "国际能源法", "concept", "补充", "国际", "国际经济法·能源",
          "国际能源法是规范跨国能源投资、能源贸易、能源过境运输与能源安全合作的国际法规则，渊源包括能源宪章条约、WTO 规则与双边投资协定。",
          "国际能源法涉及能源投资保护、能源过境自由、争端解决与气候变化背景下的能源转型要求。",
          ["src-un-treaty", "src-wto", "src-zgbk"], related=["intl-investment", "intl-wto", "intl-environmental-law"],
          pending="能源宪章条约现代化进程与中国参与情况需按官方资料核对。", needs_verification=True),
    ],
}