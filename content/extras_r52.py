# -*- coding: utf-8 -*-
"""R52 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R52 = {
    "u02": [
        E("admin-administrative-guidance", "行政指导", "concept", "补充", "中国", "行政法学·非强制行政",
          "行政指导是行政机关在其职能范围内，通过建议、劝告、示范、信息发布等非强制方式，引导相对人自愿作出或不作出一定行为的活动。",
          "行政指导不以强制力为后盾，相对人可选择是否接受；行政机关不得以指导为名变相强制，造成损失的应依法承担相应责任。",
          ["src-law-admin-penalty", "src-zgbk"], related=["admin-administrative-interview", "admin-principles", "admin-inspection"],
          pending="行政指导缺乏统一立法与救济规则，实务中多依部门规章运行。", needs_verification=True),
    ],
    "u03": [
        E("civil-joint-guarantee", "共同保证", "concept", "重要", "中国", "民法·保证合同",
          "共同保证是两个以上保证人为同一债务提供保证，分为按份共同保证与连带共同保证。",
          "保证人未约定保证份额的，债权人可以请求任何一个保证人在其保证范围内承担保证责任；承担保证责任的保证人有权向债务人追偿，或请求其他保证人清偿其应担份额。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-guarantee", "civil-guarantee-modes", "civil-guarantee-period"]),
    ],
    "u07": [
        E("data-standard-contract", "数据出境标准合同", "concept", "补充", "中国", "数据法·数据跨境",
          "数据出境标准合同是个人信息处理者依据国家网信部门制定的标准合同范本，与境外接收方订立合同并备案后向境外提供个人信息的出境路径。",
          "标准合同路径适用于未达到安全评估门槛的情形；订立后应向省级网信部门备案，并按要求开展个人信息保护影响评估。",
          ["src-law-personal-info-2", "src-zgbk"], related=["data-cross-border", "data-export-assessment", "data-pia"],
          pending="个人信息出境标准合同办法的备案要求与范本条款需按国家网信办官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-interim-measures", "国际仲裁中的临时措施", "concept", "补充", "国际", "国际私法·国际仲裁",
          "国际仲裁中的临时措施是仲裁庭或法院在裁决作出前，为保全争议标的、维持现状或保障裁决执行而采取的临时性救济。",
          "临时措施包括财产保全、证据保全与行为保全；仲裁庭作出的临时措施可依仲裁地法与纽约公约体系获得执行。",
          ["src-un-treaty", "src-zgbk"], related=["intl-commercial-arbitration", "proc-civil-preservation", "intl-award-setting-aside"],
          pending="各仲裁规则关于临时措施的条件与执行机制需按机构规则核对。", needs_verification=True),
    ],
}