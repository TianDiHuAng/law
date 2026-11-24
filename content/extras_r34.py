# -*- coding: utf-8 -*-
"""R34 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R34 = {
    "u02": [
        E("admin-procurement-complaint", "政府采购质疑与投诉", "concept", "补充", "中国", "行政法学·政府采购救济",
          "政府采购质疑与投诉是供应商对政府采购活动中的采购文件、采购过程、中标或成交结果有异议时，依法向采购人提出质疑、向财政部门投诉的救济制度。",
          "供应商应在知道或应知其权益受到损害之日起法定期限内提出质疑；对质疑答复不满意或采购人未答复的，可向同级财政部门投诉。",
          ["src-gov-cn", "src-zgbk"], related=["admin-government-procurement", "admin-procurement-contract", "admin-litigation"],
          pending="政府采购法及其实施条例中质疑投诉的具体期限与程序需按现行文本核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-debt-security-comparison", "债的保全与债的担保", "concept", "重要", "中国", "民法·债的效力与担保",
          "债的保全与债的担保都是保障债权实现的法律工具，但性质不同：保全针对债务人责任财产的不当减少，担保则通过特定财产或第三人信用增强债权。",
          "债的保全包括代位权与撤销权，属于债的一般效力；债的担保包括保证与担保物权，产生优先受偿权或第三人责任。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract-preservation", "civil-security", "civil-guarantee"]),
    ],
    "u07": [
        E("data-right-to-erasure", "个人信息删除权", "concept", "补充", "中国", "数据法·个人信息保护",
          "个人信息删除权是个人在法定情形下请求个人信息处理者删除其个人信息的权利，属于个人信息权益的重要内容。",
          "法定情形包括处理目的已实现或无法实现、处理者停止提供产品或服务、个人撤回同意、处理者违法处理等；处理者应主动删除并通知接收方。",
          ["src-law-personal-info-2", "src-zgbk"], related=["data-personal", "data-sensitive-personal", "civil-privacy"]),
    ],
    "u08": [
        E("intl-financial-law", "国际金融法", "concept", "补充", "国际", "国际经济法·国际金融",
          "国际金融法是调整跨国货币、信贷、证券、支付与金融监管关系的国际法规则，渊源包括国际货币基金组织协定、巴塞尔协议、支付与清算规则等。",
          "国际金融法涉及汇率安排、跨境资本流动、银行审慎监管、反洗钱与金融稳定合作；多数监管标准属软法性质。",
          ["src-un-treaty", "src-zgbk"], related=["intl-wto", "intl-tax-cooperation", "intl-sources"],
          pending="IMF 协定条文与巴塞尔框架最新版本需按官方资料核对。", needs_verification=True),
    ],
}