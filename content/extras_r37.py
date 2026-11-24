# -*- coding: utf-8 -*-
"""R37 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R37 = {
    "u02": [
        E("admin-compensation-scope", "行政赔偿范围与标准", "concept", "补充", "中国", "行政法学·国家赔偿",
          "行政赔偿范围是受害人可以请求国家赔偿的行政侵权行为类型，赔偿标准则依国家赔偿法确定具体金额的计算方式。",
          "侵犯人身自由的赔偿金按日计算，侵犯生命健康权的赔偿依医疗费、误工费、护理费等项目计算，财产损失按直接损失赔偿。",
          ["src-spp-portal", "src-zgbk"], related=["admin-compensation", "admin-litigation", "admin-coercion"],
          pending="国家赔偿法关于赔偿标准的具体条文与年度调整数据需按官方文本核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-standard-terms", "格式条款", "concept", "重要", "中国", "民法·合同订立",
          "格式条款是当事人为了重复使用而预先拟定，并在订立合同时未与对方协商的条款；提供格式条款的一方须履行提示与说明义务。",
          "不合理免除或减轻己方责任、加重对方责任、限制对方主要权利的格式条款无效；对格式条款有两种以上解释的，应作不利于提供方的解释。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract-formation", "civil-contract-interpretation", "civil-act"]),
    ],
    "u07": [
        E("data-pi-audit", "个人信息保护合规审计", "concept", "补充", "中国", "数据法·个人信息保护",
          "个人信息保护合规审计是个人信息处理者定期对其处理个人信息遵守法律法规情况进行审计，以发现和纠正合规风险的制度。",
          "处理者应建立合规审计制度，定期开展审计并留存记录；审计内容涉及处理规则、告知同意、个人权利响应、安全保障与跨境提供等。",
          ["src-law-personal-info-2", "src-zgbk"], related=["data-personal", "data-pia", "data-security"],
          pending="个人信息保护合规审计管理办法及配套标准需按国家网信部门官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-ihl-enforcement", "国际人道法的实施机制", "concept", "补充", "国际", "国际公法·国际人道法",
          "国际人道法的实施机制包括国内立法转化、保护国制度、红十字国际委员会探视与斡旋、国际刑事追诉与违反行为的责任追究。",
          "严重违反日内瓦公约的行为构成战争罪，可依普遍管辖原则在国内法院追诉或由国际刑事法院审理。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["intl-humanitarian-law", "intl-international-criminal", "intl-icc"],
          pending="日内瓦公约及附加议定书的具体实施条款需按红十字国际委员会资料核对。", needs_verification=True),
    ],
}