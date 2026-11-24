# -*- coding: utf-8 -*-
"""R27 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R27 = {
    "u03": [
        E("civil-act-effect", "民事法律行为的效力形态", "concept", "重要", "中国", "民法·法律行为效力",
          "民事法律行为的效力形态包括有效、无效、可撤销与效力待定；不同形态对应不同的法律后果与救济方式。",
          "无效行为自始、当然、确定不发生效力；可撤销行为在撤销权行使前有效，撤销后自始无效；效力待定行为经追认后有效。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-act", "civil-good-faith", "civil-agency"]),
    ],
    "u07": [
        E("env-ozone", "臭氧层保护", "concept", "补充", "中国", "环境法·臭氧层",
          "臭氧层保护是规范消耗臭氧层物质的生产、使用、进出口与淘汰，保护平流层臭氧层的制度。",
          "中国通过《保护臭氧层维也纳公约》与《蒙特利尔议定书》履约，对消耗臭氧层物质实行配额许可与淘汰管理。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-air-pollution", "env-climate"],
          pending="消耗臭氧层物质管理条例与履约进展需按生态环境部官方文本核对。", needs_verification=True),
        E("data-public-data-open", "公共数据开放", "concept", "补充", "中国", "数据法·公共数据",
          "公共数据开放是行政机关、公共企事业单位依法向社会开放其在履职过程中制作或获取的数据，促进数据开发利用与公共治理。",
          "公共数据开放应遵循分类分级、安全可控、需求导向原则；涉及国家秘密、商业秘密与个人信息的依法不予开放或脱敏处理。",
          ["src-law-data-security", "src-zgbk"], related=["data-security", "data-classification", "data-important-data"],
          pending="公共数据开放目录与授权运营规则需按各地与行业主管部门官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-development-law", "国际发展法", "concept", "补充", "国际", "国际公法·国际经济法",
          "国际发展法是调整国际社会与发展中国家之间关于发展援助、技术合作、贸易优惠与债务安排等关系的国际法规则。",
          "国际发展法体现发展权与特殊差别待遇理念，渊源包括联合国大会决议、发展援助协定与多边开发机构规则；多数文件属软法性质。",
          ["src-un-charter", "src-un-treaty", "src-zgbk"], related=["intl-sources", "intl-wto", "intl-organization-law"],
          pending="联合国发展权宣言与官方发展援助数据需按联合国官方资料核对。", needs_verification=True),
    ],
}