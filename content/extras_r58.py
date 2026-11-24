# -*- coding: utf-8 -*-
"""R58 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R58 = {
    "u02": [
        E("admin-administrative-benefit", "行政给付", "concept", "补充", "中国", "行政法学·行政给付",
          "行政给付是行政机关依法向符合条件的相对人提供物质帮助或服务的行为，如最低生活保障、抚恤金、社会保险待遇与灾害救助。",
          "行政给付以保障基本生活与实现社会公平为目标，须依法定条件与程序进行；对符合条件的相对人，行政机关不得违法拒绝或拖延给付。",
          ["src-law-admin-license", "src-zgbk"], related=["social-protection", "admin-act", "admin-principles"],
          pending="行政给付的具体规则分散于社会保险法与社会救助制度，需按各领域规定核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-dation-in-payment", "代物清偿", "concept", "补充", "中国", "民法·债的消灭",
          "代物清偿是债务人以他种给付代替原定给付，经债权人受领而消灭原债务的行为，属于债的消灭方式之一。",
          "代物清偿须经当事人合意，并以实际履行的他种给付为要件；他种给付存在瑕疵的，可参照买卖等规则处理。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-obligation-extinction", "civil-offset", "civil-deposit-in-escrow"],
          pending="代物清偿与以物抵债的区分及效力需按最高人民法院裁判规则核对。", needs_verification=True),
    ],
    "u07": [
        E("data-platform-liability", "数据交易平台责任", "concept", "补充", "中国", "数据法·数据流通",
          "数据交易平台责任是数据交易平台运营者因未尽审核、安全保障与信息披露义务，对交易中的违法数据处理或损害承担的责任。",
          "平台应审核交易主体与数据来源合法性、留存交易记录、采取安全措施；违反义务可能承担民事、行政乃至刑事责任。",
          ["src-law-data-security", "src-law-personal-info-2", "src-zgbk"], related=["data-factor-market", "data-broker-liability", "data-trusted-circulation"],
          pending="数据交易平台的专门监管规则尚在完善，责任边界需结合现行法律解释。", needs_verification=True),
    ],
    "u08": [
        E("intl-carriage-of-goods", "国际货物运输法", "concept", "补充", "国际", "国际经济法·国际货物运输",
          "国际货物运输法是规范跨国货物海上、航空、铁路与多式联运的国际规则，主要渊源包括海牙—维斯比规则、汉堡规则、蒙特利尔公约与相关铁路运输公约。",
          "国际货物运输法就承运人责任、免责事由、责任限额与单据效力作出统一规定，不同运输方式适用不同的国际公约体系。",
          ["src-un-treaty", "src-zgbk"], related=["intl-cisg-application", "intl-aviation-law", "intl-commercial-arbitration"],
          pending="各运输公约的缔约国范围与最新修订需按联合国及相关国际组织官方资料核对。", needs_verification=True),
    ],
}