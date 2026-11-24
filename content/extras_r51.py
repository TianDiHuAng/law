# -*- coding: utf-8 -*-
"""R51 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R51 = {
    "u02": [
        E("admin-administrative-interview", "行政约谈", "concept", "补充", "中国", "行政法学·柔性监管",
          "行政约谈是行政机关为督促相关主体履行法定义务、整改问题，通过约见谈话方式进行提醒、告诫与指导的柔性监管方式。",
          "行政约谈一般不直接产生强制法律效果，但可能成为后续处罚或信用惩戒的考量因素；约谈应依法定职责范围进行并留存记录。",
          ["src-law-admin-penalty", "src-zgbk"], related=["admin-inspection", "admin-penalty", "admin-principles"],
          pending="行政约谈缺乏统一立法，各部门规章中的规定不一，需按具体领域规定核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-claim-pledge", "债权质权", "concept", "重要", "中国", "民法·担保物权",
          "债权质权是以可转让的债权为标的设立的质权，属于权利质权的一种；以债权出质应订立书面合同并办理登记或通知债务人。",
          "债权质权实现时，质权人可就出质债权的清偿优先受偿；出质债权先于主债权到期的，质权人可提存其给付。",
          ["src-law-civil-code", "src-jd-civil-property", "src-zgbk"], related=["civil-security", "civil-obligation-transfer", "civil-guarantee"]),
    ],
    "u07": [
        E("data-broker-liability", "数据经纪人责任", "concept", "补充", "中国", "数据法·数据流通",
          "数据经纪人责任是数据经纪人在撮合、加工与交易数据过程中，因违反个人信息保护与数据安全义务而承担的法律责任。",
          "责任类型包括民事赔偿、行政处罚与刑事责任；经纪人应核验数据来源合法性、取得合法性基础并履行告知与安全保障义务。",
          ["src-law-personal-info-2", "src-law-data-security", "src-zgbk"], related=["data-broker", "data-trusted-circulation", "data-personal"],
          pending="数据经纪人专门监管规则尚未出台，责任边界需结合现行法律解释。", needs_verification=True),
    ],
    "u08": [
        E("intl-sports-appeal", "国际体育仲裁的上诉机制", "concept", "补充", "国际", "国际私法·体育仲裁",
          "国际体育仲裁的上诉机制是当事人对体育组织纪律决定不服，向国际体育仲裁院上诉仲裁庭提起上诉并请求撤销或变更决定的程序。",
          "上诉仲裁庭可对事实与法律进行重新审查；裁决可依瑞士法向瑞士联邦最高法院申请有限审查，但撤销理由极为有限。",
          ["src-un-treaty", "src-zgbk"], related=["intl-sports-arbitration", "intl-sports-law", "intl-award-setting-aside"],
          pending="国际体育仲裁院上诉程序与瑞士联邦最高法院审查实践需按其官方资料核对。", needs_verification=True),
    ],
}