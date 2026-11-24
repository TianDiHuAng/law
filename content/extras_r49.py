# -*- coding: utf-8 -*-
"""R49 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R49 = {
    "u02": [
        E("admin-inspection", "行政检查", "concept", "补充", "中国", "行政法学·行政检查",
          "行政检查是行政机关依法对公民、法人或其他组织遵守法律、法规和行政决定情况进行了解、核查的行政行为，常见于市场监管、安全生产与环境保护领域。",
          "行政检查应依法定权限与程序进行，推行双随机一公开与信用分级分类监管；检查结果可作为后续处罚与信用监管的依据。",
          ["src-law-admin-penalty", "src-zgbk"], related=["admin-investigation", "admin-penalty", "admin-principles"],
          pending="各类行政检查的具体规则分散于部门法，缺乏统一行政检查法。", needs_verification=True),
    ],
    "u03": [
        E("civil-debt-assumption", "债务承担", "concept", "重要", "中国", "民法·债的移转",
          "债务承担是第三人承担债务人的债务，分为免责的债务承担与并存的债务承担（债务加入）。",
          "免责的债务承担须经债权人同意，原债务人脱离债的关系；未经债权人同意，债务转移对债权人不发生效力。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-obligation-transfer", "civil-debt-joinder", "civil-contract"]),
    ],
    "u07": [
        E("data-trusted-circulation", "数据可信流通", "concept", "补充", "中国", "数据法·数据流通",
          "数据可信流通是在保障数据安全与权益的前提下，通过技术与管理机制实现数据可控、可追溯、可审计的流通模式。",
          "可信流通依赖隐私计算、数据使用控制、可信执行环境与区块链存证等技术，并结合合同、认证与审计等治理手段。",
          ["src-law-data-security", "src-law-personal-info-2", "src-zgbk"], related=["data-data-space", "data-factor-market", "data-revenue-sharing"],
          pending="可信数据空间与隐私计算相关标准需按国家数据局及标准化机构官方文件核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-sports-law", "国际体育法", "concept", "补充", "国际", "国际经济法·体育法",
          "国际体育法是规范国际体育组织治理、赛事规则、反兴奋剂、运动员权利与体育争议解决的规则体系，兼具行业自治与国际公法、私法要素。",
          "世界反兴奋剂条例、国际体育仲裁院判例与各国际单项体育联合会规则构成其主要渊源，行业自治与运动员权利保障之间存在持续张力。",
          ["src-un-treaty", "src-zgbk"], related=["intl-sports-arbitration", "intl-human-rights", "intl-sources"],
          pending="世界反兴奋剂机构规则与国际体育仲裁院判例需按其官方资料核对。", needs_verification=True),
    ],
}