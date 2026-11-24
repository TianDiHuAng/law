# -*- coding: utf-8 -*-
"""R38 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R38 = {
    "u03": [
        E("civil-offset", "抵销", "concept", "重要", "中国", "民法·债的消灭",
          "抵销是当事人互负债务，标的物种类、品质相同且债务均已到履行期时，一方以自己的债务与对方债务在对等额度内相互消灭的行为。",
          "抵销分为法定抵销与约定抵销；法定抵销须通知对方，通知到达对方时生效，不得附条件或者附期限。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-obligation-extinction", "civil-contract", "com-bankruptcy-avoidance"]),
    ],
    "u04": [
        E("crim-case-property", "刑事诉讼涉案财物处置", "concept", "补充", "中国", "刑事诉讼法学·涉案财物",
          "刑事诉讼涉案财物处置是对查封、扣押、冻结的财物依法保管、返还、没收、拍卖或上缴国库的程序制度。",
          "涉案财物应与案件无关的及时返还；经查明确实与案件无关的，应在法定期限内解除措施并退还；违法所得依法追缴或没收。",
          ["src-law-cpc", "src-law-criminal", "src-zgbk"], related=["crim-investigation", "crim-coercive", "crim-trial"],
          pending="涉案财物处置的具体期限与程序需按刑事诉讼法及两高解释核对。", needs_verification=True),
    ],
    "u07": [
        E("data-broker", "数据经纪人", "concept", "补充", "中国", "数据法·数据流通",
          "数据经纪人是在数据供需双方之间提供撮合、加工、合规评估与交易服务的中介主体，是数据要素市场的重要参与者。",
          "数据经纪活动须遵守个人信息保护与数据安全规定，不得非法获取、出售或提供个人信息；具体资质与监管要求以国家数据主管部门规定为准。",
          ["src-law-data-security", "src-law-personal-info-2", "src-zgbk"], related=["data-data-governance", "data-public-data-open", "data-security"],
          pending="数据经纪相关管理办法尚未形成统一官方文本，具体规则需持续跟踪。", needs_verification=True),
    ],
    "u08": [
        E("intl-aviation-law", "国际航空法", "concept", "补充", "国际", "国际公法·国际航空",
          "国际航空法是规范航空器运行、航空运输、航空安全与航空器权利的国际法规则，核心渊源包括《芝加哥公约》《华沙公约》《蒙特利尔公约》。",
          "国际航空法确立领空主权、航空器国籍与登记、航空运输承运人责任与航空安全保卫等制度。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["intl-sources", "intl-treaty", "intl-commercial-arbitration"],
          pending="国际民航组织公约体系与中国批准情况需按 ICAO 与外交部官方资料核对。", needs_verification=True),
    ],
}