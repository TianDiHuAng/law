# -*- coding: utf-8 -*-
"""R29 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R29 = {
    "u02": [
        E("admin-procurement-contract", "政府采购合同的法律性质", "concept", "补充", "中国", "行政法学·政府采购合同",
          "政府采购合同是采购人与中标、成交供应商依照政府采购程序订立的合同，其法律性质在行政协议与民事合同之间存在讨论。",
          "政府采购合同适用合同法的原则与规定，采购人与供应商的权利义务按照平等自愿原则约定；但采购人依法享有一定的管理性权力，需依政府采购法规定行使。",
          ["src-gov-cn", "src-zgbk"], related=["admin-government-procurement", "admin-administrative-agreement", "civil-contract"],
          pending="政府采购法关于合同性质与争议解决的条文需按现行文本核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-privity", "合同的相对性", "concept", "重要", "中国", "民法·合同效力范围",
          "合同的相对性是指合同仅在当事人之间产生法律效力，原则上不对第三人产生约束力；第三人一般不享有合同权利、不承担合同义务。",
          "合同相对性存在例外：为第三人利益的合同、第三人代为履行、买卖不破租赁、代位权与撤销权等，均体现对相对性的突破。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-contract-preservation", "civil-contract-termination"]),
    ],
    "u07": [
        E("data-internet-finance", "互联网金融治理", "concept", "补充", "中国", "数据法·金融科技",
          "互联网金融治理是规范互联网支付、网络借贷、互联网保险、互联网基金销售等业态的监管制度，涉及准入、信息披露、消费者保护、数据安全与反洗钱。",
          "互联网金融治理强调持牌经营、穿透式监管与功能监管，平台不得违规从事金融业务或为非法金融活动提供信息服务。",
          ["src-law-network-security-2", "src-law-data-security", "src-zgbk"], related=["data-platform-economy", "data-cybercrime", "com-securities"],
          pending="互联网金融监管规则与平台整改要求需按中国人民银行等监管部门官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-treaty-domestic", "国际条约在国内的适用", "concept", "补充", "国际", "国际公法·条约国内适用",
          "国际条约在国内的适用是各国依宪法与法律规定，将条约义务转化为国内法或允许条约直接适用的制度安排。",
          "中国宪法未统一规定条约的国内地位，实践中区分条约类型：民商事条约可依法直接适用，涉及主权与刑罚的条约一般需经立法转化。",
          ["src-un-treaty", "src-law-constitution", "src-zgbk"], related=["intl-treaty", "intl-sources", "intl-private"],
          pending="中国条约适用实践与相关法律规定需按外交部及全国人大官方资料核对。", needs_verification=True),
    ],
}