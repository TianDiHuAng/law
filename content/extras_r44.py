# -*- coding: utf-8 -*-
"""R44 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R44 = {
    "u02": [
        E("admin-license-renewal", "行政许可的有效期与延续", "concept", "补充", "中国", "行政法学·行政许可",
          "行政许可的有效期是许可决定所确定的效力存续期间；被许可人需要延续有效期的，应在期限届满前依法提出延续申请。",
          "法律、法规、规章未规定期限的，行政机关应根据事项性质确定期限；行政机关应在有效期届满前作出是否准予延续的决定，逾期未决定的视为准予延续。",
          ["src-law-admin-license", "src-zgbk"], related=["admin-license", "admin-license-revocation", "admin-principles"]),
    ],
    "u03": [
        E("civil-intention-interpretation", "意思表示的解释", "concept", "重要", "中国", "民法·法律行为",
          "意思表示的解释是确定表意人表示的规范含义，以判断法律行为的内容与效力；有相对人的意思表示与无相对人的意思表示解释规则不同。",
          "有相对人的意思表示应按照所使用的词句，结合相关条款、性质、目的、习惯以及诚信原则确定含义；无相对人的意思表示应结合相关条款、性质、目的、习惯以及诚信原则确定。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-act", "civil-act-effect", "civil-contract-interpretation"]),
    ],
    "u07": [
        E("data-data-space", "数据空间", "concept", "补充", "中国", "数据法·数据基础设施",
          "数据空间是面向特定行业或领域，以数据可信流通与共享为目标的基础设施与治理机制，强调数据主权、互操作与可控共享。",
          "数据空间建设涉及数据目录、身份认证、使用控制与安全审计等技术标准与治理规则；中国相关实践以行业数据空间与地方试点为主。",
          ["src-law-data-security", "src-zgbk"], related=["data-data-governance", "data-factor-market", "data-cross-border"],
          pending="数据空间相关标准与试点政策需按国家数据局及行业主管部门官方文件核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-climate-litigation", "国际气候变化诉讼", "concept", "补充", "国际", "国际公法·气候变化",
          "国际气候变化诉讼是当事人通过国内或国际司法程序，要求国家或企业承担气候变化减缓、适应责任或赔偿损失的诉讼类型。",
          "国际层面主要体现为国际法院咨询意见、区域人权法院裁判与投资仲裁中的气候抗辩；国内层面则以环境公益诉讼与行政不作为诉讼为主。",
          ["src-icj", "src-un-treaty", "src-zgbk"], related=["env-climate", "intl-environmental-law", "intl-human-rights"],
          pending="国际法院气候变化咨询意见与各区域法院裁判的最新进展需按官方资料核对。", needs_verification=True),
    ],
}