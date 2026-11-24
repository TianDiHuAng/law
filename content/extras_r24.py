# -*- coding: utf-8 -*-
"""R24 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R24 = {
    "u03": [
        E("civil-co-ownership", "共有", "concept", "重要", "中国", "民法·物权",
          "共有是两个以上单位、个人对同一动产或者不动产共同享有所有权，分为按份共有和共同共有。",
          "按份共有人按照份额享有所有权，可依法转让其份额；共同共有人对共有财产共同享有所有权，处分共有财产须经全体共同共有人同意（法律另有规定除外）。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-ownership", "civil-property", "civil-marriage"]),
    ],
    "u07": [
        E("env-water-pollution", "水污染防治", "concept", "补充", "中国", "环境法·水污染",
          "水污染防治是防治江河、湖泊、运河、渠道、水库等地表水体以及地下水体的污染，保护水环境质量的制度。",
          "水污染防治法规定水环境质量标准、污染物排放标准、排污许可、饮用水水源保护、水污染事故应急等制度。",
          ["src-law-water-pollution", "src-zgbk"], related=["env-law", "env-pollution", "env-marine-pollution"],
          pending="水污染防治法及地方水污染物排放标准需按生态环境部现行文本核对。", needs_verification=True),
        E("data-algorithm-recommendation", "算法推荐治理", "concept", "补充", "中国", "数据法·算法治理",
          "算法推荐治理是规范互联网信息服务算法推荐活动，要求算法推荐服务提供者坚持主流价值导向、保障用户知情权与选择权、防止算法歧视与沉迷的制度。",
          "算法推荐服务提供者应公示算法推荐服务的基本原理、目的意图和主要运行机制，向用户提供便捷的关闭算法推荐服务的选项。",
          ["src-law-personal-info-2", "src-law-data-security", "src-zgbk"], related=["data-algorithm", "data-automated-decision", "data-platform-economy"],
          pending="互联网信息服务算法推荐管理规定及备案要求需按国家网信办官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-sanctions", "国际制裁", "concept", "补充", "国际", "国际公法·国际制裁",
          "国际制裁是国际组织或国家为维护国际和平与安全、回应违反国际法行为，对特定国家、实体或个人采取的强制性措施，包括经济制裁、旅行禁令、资产冻结、武器禁运等。",
          "联合国安理会依《联合国宪章》第七章可决定采取制裁措施，成员国应履行安理会决议；单边制裁的合法性在国际法上存在争议。",
          ["src-un-charter", "src-icj", "src-zgbk"], related=["intl-sources", "intl-organization-law", "intl-state-responsibility"],
          pending="联合国安理会制裁清单与各国单边制裁措施需按联合国及各国官方文本核对。", needs_verification=True),
    ],
}
