# -*- coding: utf-8 -*-
"""R19 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R19 = {
    "u02": [
        E("admin-administrative-confirmation", "行政确认", "concept", "补充", "中国", "行政法学·行政确认",
          "行政确认是行政机关依法对特定的法律事实、法律关系或者法律状态进行认定、证明并予以宣告的行为。",
          "行政确认包括身份确认、权属确认、工伤认定、事故责任认定等；确认行为通常不具有创设权利的效果，但对后续权利义务有重要影响。",
          ["src-law-admin-litigation", "src-zgbk"], related=["admin-act", "admin-license", "admin-litigation"],
          pending="行政确认的具体类型与救济途径需按各专门法律、法规核对。", needs_verification=True),
    ],
    "u07": [
        E("data-personal-portability", "个人信息可携带权", "concept", "补充", "中国", "数据法·个人信息保护",
          "个人信息可携带权是个人请求将个人信息转移至其指定的个人信息处理者，在符合国家网信部门规定条件时，个人信息处理者应当提供转移途径的权利。",
          "可携带权是个人信息保护法赋予个人的重要权利，旨在增强个人对信息的控制、促进数据流通与市场竞争；具体条件与格式以网信部门规定为准。",
          ["src-law-personal-info-2", "src-zgbk"], related=["data-personal", "data-sensitive-personal", "data-algorithm"],
          pending="个人信息可携带权的具体实施条件与技术标准需按国家网信部门规定核对。", needs_verification=True),
        E("env-wetland", "湿地保护", "concept", "补充", "中国", "环境法·湿地生态",
          "湿地保护是对具有重要生态功能的湿地生态系统进行保护、修复与合理利用的制度，坚持保护优先、严格管理、系统治理、科学修复、合理利用原则。",
          "湿地保护法建立湿地分级管理、湿地保护规划、湿地占用审批与生态修复等制度；建设项目占用重要湿地须依法办理审批手续。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-ecological", "env-ecological-redline"],
          pending="湿地保护法及配套名录需按国家林草局、生态环境部官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-investment-arbitration", "国际投资仲裁", "concept", "补充", "国际", "国际投资法·ISDS",
          "国际投资仲裁是外国投资者依据投资条约或投资合同，将与国际东道国的投资争端提交仲裁庭解决的制度，典型机构为ICSID。",
          "国际投资仲裁以条约同意为基础，适用条约保护标准与程序规则；裁决的承认与执行依《ICSID公约》或《纽约公约》进行。",
          ["src-icsid", "src-un-treaty", "src-zgbk"], related=["intl-investment", "intl-commercial-arbitration", "intl-sources"],
          pending="ICSID仲裁规则与主要投资条约文本需按官方资料核对。", needs_verification=True),
    ],
}
