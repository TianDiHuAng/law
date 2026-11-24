# -*- coding: utf-8 -*-
"""R32 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R32 = {
    "u02": [
        E("admin-license-hearing", "行政许可听证", "concept", "重要", "中国", "行政法学·行政许可程序",
          "行政许可听证是行政机关在作出涉及公共利益或他人重大利益的行政许可决定前，依法组织听证、听取申请人、利害关系人意见的程序。",
          "法律、法规、规章规定实施行政许可应当听证的事项，或者行政机关认为需要听证的其他涉及公共利益的重大行政许可事项，应当向社会公告并举行听证。",
          ["src-law-admin-license", "src-zgbk"], related=["admin-license", "admin-hearing", "admin-principles"]),
    ],
    "u03": [
        E("civil-obligation-extinction", "债的消灭", "concept", "重要", "中国", "民法·债法总论",
          "债的消灭是债权债务关系在客观上归于终止，包括清偿、抵销、提存、免除与混同五种原因。",
          "清偿是债的消灭最常态；抵销须双方债务种类品质相同且到期；提存适用于债权人无正当理由拒绝受领等情形。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-contract-termination", "civil-unjust-enrichment"]),
    ],
    "u07": [
        E("data-data-trust", "数据信托", "concept", "补充", "中国", "数据法·数据治理",
          "数据信托是借鉴信托结构，由数据主体或数据控制者将数据权益委托给受托机构，按约定目的管理、使用与收益分配的制度构想与实践探索。",
          "数据信托在中国尚处于探索阶段，尚无专门立法；其落地需兼顾个人信息保护、数据安全与信托法原理，具体规则以官方探索文件为准。",
          ["src-law-personal-info-2", "src-wiki-trust-law", "src-zgbk"], related=["com-trust", "data-data-governance", "data-personal"],
          pending="数据信托的监管口径与试点规则尚未形成统一官方文本，需持续跟踪。", needs_verification=True),
    ],
    "u08": [
        E("intl-sports-arbitration", "国际体育仲裁", "concept", "补充", "国际", "国际私法·体育仲裁",
          "国际体育仲裁是通过国际体育仲裁院（CAS）等机构解决体育赛事纪律、合同、参赛资格与反兴奋剂等争议的制度。",
          "体育仲裁以当事人协议或体育组织章程中的仲裁条款为基础，裁决可依《纽约公约》申请承认与执行；瑞士联邦最高法院对CAS裁决有有限审查权。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["proc-arbitration", "intl-commercial-arbitration", "intl-private"],
          pending="国际体育仲裁院规则与案例需按其官方资料核对，本站未逐一核实。", needs_verification=True),
    ],
}