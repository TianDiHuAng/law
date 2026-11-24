# -*- coding: utf-8 -*-
"""R33 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R33 = {
    "u02": [
        E("admin-enforcement-procedure", "行政强制执行程序", "concept", "重要", "中国", "行政法学·行政强制执行",
          "行政强制执行程序是行政机关依法定步骤强制当事人履行已生效行政决定所确定义务的过程，通常包括催告、作出强制执行决定、实施执行与执行终结。",
          "行政机关作出强制执行决定前应事先催告当事人履行义务，当事人有权陈述申辩；执行中可与当事人达成执行协议，当事人不履行协议时恢复强制执行。",
          ["src-law-admin-penalty", "src-law-admin-litigation", "src-zgbk"],
          related=["admin-coercion", "admin-penalty", "admin-litigation"]),
    ],
    "u03": [
        E("civil-guarantee-modes", "保证方式与先诉抗辩权", "concept", "重要", "中国", "民法·保证合同",
          "保证方式分为一般保证与连带责任保证。一般保证的保证人享有先诉抗辩权，即债权人须先就债务人财产强制执行无效果后，才能请求保证人承担责任。",
          "保证方式没有约定或者约定不明确的，按照一般保证承担保证责任；连带责任保证的保证人不享有先诉抗辩权。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-guarantee", "civil-security", "civil-contract"]),
    ],
    "u07": [
        E("env-ecological-product-value", "生态产品价值实现", "concept", "补充", "中国", "环境法·生态补偿",
          "生态产品价值实现是通过生态补偿、生态产业化经营、生态资源权益交易等机制，将生态系统提供的产品与服务转化为经济价值的制度安排。",
          "生态产品价值实现包括政府主导的转移支付与市场化的生态产品交易两条路径，需建立价值核算、经营开发与保护补偿相衔接的机制。",
          ["src-law-environment", "src-law-yangtze", "src-zgbk"], related=["env-ecological", "env-ecological-redline", "env-carbon-market"],
          pending="生态产品价值核算规范与地方试点政策需按国家发展改革委等官方文件核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-tax-cooperation", "国际税务合作", "concept", "补充", "国际", "国际经济法·国际税法",
          "国际税务合作是国家之间通过税收协定、情报交换、征管互助与 BEPS 多边公约等机制，协调税权分配、防止双重征税与打击逃避税的制度。",
          "国际税务合作以税收协定网络与多边公约为基础，涉及常设机构、受益所有人、转让定价与情报交换等规则。",
          ["src-un-treaty", "src-zgbk"], related=["intl-wto", "intl-treaty", "intl-development-law"],
          pending="中国税收协定网络与 BEPS 多边公约适用情况需按国家税务总局官方资料核对。", needs_verification=True),
    ],
}