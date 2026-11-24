# -*- coding: utf-8 -*-
"""R14 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R14 = {
    "u07": [
        E("env-air-pollution", "大气污染防治", "concept", "重要", "中国", "环境法·大气污染",
          "大气污染防治是规范大气污染物排放、改善大气环境质量、保护公众健康的制度，坚持源头治理、协同控制、重点区域联防联控。",
          "大气污染防治法规定排污许可、总量控制、重污染天气应对、机动车与非道路移动机械排放控制等制度。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-pollution", "env-eia"],
          pending="大气污染防治法及地方实施条例需按生态环境部现行文本核对。", needs_verification=True),
        E("data-cybersecurity-review", "网络安全审查", "concept", "重要", "中国", "数据法·网络安全",
          "网络安全审查是对关键信息基础设施运营者采购网络产品和服务、数据处理者开展数据处理活动等影响国家安全的情形进行审查的制度。",
          "网络安全审查重点评估产品和服务的安全性、可控性，以及数据处理活动对国家安全的影响；具体程序以国家网信部门规定为准。",
          ["src-law-network-security-2", "src-law-data-security", "src-zgbk"], related=["data-network", "data-critical-infrastructure", "data-security"],
          pending="网络安全审查办法及申报指南需按国家网信办官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-icj", "国际法院", "concept", "补充", "国际", "国际公法·国际司法",
          "国际法院是联合国的主要司法机关，依《国际法院规约》审理国家之间的法律争端，并应联合国机关请求提供咨询意见。",
          "国际法院只受理国家之间的诉讼，个人和非国家实体不能作为诉讼当事方；法院管辖权须基于当事国同意、条约或任择强制管辖声明。",
          ["src-icj", "src-un-charter", "src-zgbk"], related=["intl-sources", "intl-treaty", "intl-organization-law"],
          pending="国际法院管辖权声明与案例需按国际法院官网核对。", needs_verification=True),
    ],
    "u10": [
        E("law-administrative-license", "《中华人民共和国行政许可法》导读", "law", "重要", "中国", "2019年修正，2019年4月23日公布",
          "行政许可法规定行政许可的设定、实施机关、实施程序、收费、监督检查与法律责任。",
          "行政许可法确立许可法定、公开公平公正、便民高效、信赖保护等原则，规范行政许可的设定与实施。",
          ["src-law-admin-license", "src-zgbk"], related=["admin-license", "admin-principles", "admin-litigation"],
          law=dict(status="现行有效", version="2019年修正", effective_date="2019-04-23", checked_date="2026-11-24",
                   background="行政许可法2003年制定，2019年修正适应放管服改革与优化营商环境需要，规范行政许可行为。",
                   structure=[dict(name="第一章 总则", content="立法目的、许可法定、公开公平公正、便民高效"),
                              dict(name="第二章 行政许可的设定", content="设定权限、设定事项、设定程序"),
                              dict(name="第三章 行政许可的实施机关", content="实施主体、相对集中许可权"),
                              dict(name="第四章 行政许可的实施程序", content="申请、受理、审查、决定、期限、听证"),
                              dict(name="第五章 行政许可的费用", content="收费规则"),
                              dict(name="第六章 监督检查", content="监督与被许可人义务"),
                              dict(name="第七章 法律责任", content="违法许可与法律责任"),
                              dict(name="第八章 附则", content="施行日期")],
                   key_articles=[dict(article="第二条", content="本法所称行政许可，是指行政机关根据公民、法人或者其他组织的申请，经依法审查，准予其从事特定活动的行为。"),
                                 dict(article="第五条", content="设定和实施行政许可，应当遵循公开、公平、公正、非歧视的原则。"),
                                 dict(article="第八条", content="公民、法人或者其他组织依法取得的行政许可受法律保护，行政机关不得擅自改变已经生效的行政许可。")],
                   amendments=["2003年制定", "2019年修正"],
                   interpretations=["行政许可法配套规章与国务院决定，具体以官方现行文本为准。"]),
          pending="2019年修正后条文序号与配套规定需按官方文本核对。", needs_verification=False),
    ],
}
