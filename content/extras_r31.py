# -*- coding: utf-8 -*-
"""R31 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R31 = {
    "u02": [
        E("admin-reconsideration-prerequisite", "行政复议前置", "concept", "重要", "中国", "行政法学·行政复议",
          "行政复议前置是法律规定当事人对特定行政行为不服，必须先申请行政复议，对复议决定不服或复议机关逾期不作决定的，才能向人民法院提起行政诉讼的制度。",
          "2023年修订的行政复议法扩大了复议前置范围，将当场作出的行政处罚、行政机关不履行法定职责、政府信息公开等情形纳入前置。",
          ["src-law-admin-reconsideration", "src-law-admin-litigation", "src-zgbk"],
          related=["admin-reconsideration", "admin-litigation", "proc-admin-litigation"]),
    ],
    "u03": [
        E("civil-estate-partition", "遗产分割", "concept", "补充", "中国", "民法·继承",
          "遗产分割是继承开始后，在清偿遗产债务、确定各继承人应得份额的基础上，将遗产实际分配给继承人的行为。",
          "遗产分割应遵循有利于生产和生活需要、不损害遗产效用的原则；不宜分割的遗产可采取折价、适当补偿或共有等方式处理。",
          ["src-law-civil-code", "src-jd-civil-inheritance", "src-zgbk"],
          related=["civil-inheritance", "civil-testate", "civil-co-ownership"]),
    ],
    "u06": [
        E("com-securities-representative", "证券代表人诉讼", "concept", "重要", "中国", "商法·证券法",
          "证券代表人诉讼是投资者因证券虚假陈述、内幕交易、操纵市场等行为遭受损失，由投资者保护机构或部分投资者作为代表人提起的群体性诉讼制度。",
          "证券法规定投资者保护机构受五十名以上投资者委托，可以作为代表人参加诉讼；法院判决对未声明退出的投资者发生效力。",
          ["src-law-securities", "src-zgbk"], related=["com-investor-protection", "com-disclosure", "proc-civil-party"]),
    ],
    "u08": [
        E("intl-environmental-law", "国际环境法", "concept", "补充", "国际", "国际公法·国际环境法",
          "国际环境法是调整国家之间在环境保护领域权利义务关系的国际法分支，渊源包括气候变化、生物多样性、海洋环境保护、危险废物越境转移等条约与习惯规则。",
          "国际环境法确立预防原则、共同但有区别的责任、可持续发展、国际合作与损害赔偿责任等原则。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["intl-sources", "env-law", "intl-treaty"],
          pending="主要多边环境协定的缔约方与履约机制需按联合国环境规划署官方资料核对。", needs_verification=True),
    ],
}