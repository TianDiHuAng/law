# -*- coding: utf-8 -*-
"""R16 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R16 = {
    "u02": [
        E("admin-government-procurement", "政府采购", "concept", "重要", "中国", "行政法学·政府采购",
          "政府采购是各级国家机关、事业单位和团体组织使用财政性资金采购依法制定的集中采购目录以内的或者采购限额标准以上的货物、工程和服务的行为。",
          "政府采购遵循公开透明、公平竞争、公正和诚实信用原则，采购方式包括公开招标、邀请招标、竞争性谈判、单一来源采购、询价等。",
          ["src-gov-cn", "src-zgbk"], related=["admin-act", "admin-license", "admin-principles"],
          pending="政府采购法及其实施条例的具体条文与最新修订需按官方文本核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-estate-administrator", "遗产管理人制度", "concept", "重要", "中国", "民法·继承",
          "遗产管理人是在继承开始后负责清理、管理、保护、分割遗产并处理相关事务的主体，由遗嘱指定、继承人推选或法院指定。",
          "遗产管理人应依法履行职责，因故意或者重大过失造成继承人、受遗赠人、债权人损害的，应承担民事责任。",
          ["src-law-civil-code", "src-jd-civil-inheritance", "src-zgbk"], related=["civil-inheritance", "civil-testate", "civil-legacy-support"]),
    ],
    "u07": [
        E("env-marine-pollution", "海洋环境保护", "concept", "补充", "中国", "环境法·海洋环境",
          "海洋环境保护是防治陆源污染物、海岸工程、海洋工程、船舶等对海洋环境造成污染损害，保护海洋生态系统的法律制度。",
          "海洋环境保护法规定海洋环境监督管理、海洋生态保护、污染防治与法律责任；向海洋排放污染物须符合标准并依法取得许可。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-pollution", "env-ecological"],
          pending="海洋环境保护法及配套标准需按生态环境部现行文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-space-law", "外层空间法", "concept", "补充", "国际", "国际公法·外层空间",
          "外层空间法是规范外层空间探索、利用与天体活动的国际法分支，核心渊源包括《外层空间条约》《责任公约》《登记公约》等。",
          "外层空间法确立外层空间不得据为己有、和平利用、国际合作、国家责任与空间物体登记等原则。",
          ["src-un-charter", "src-icj", "src-zgbk"], related=["intl-sources", "intl-treaty", "intl-organization-law"],
          pending="外层空间条约体系与各国空间立法需按联合国外空事务厅官方资料核对。", needs_verification=True),
    ],
}
