# -*- coding: utf-8 -*-
"""R26 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R26 = {
    "u03": [
        E("civil-marital-debt", "夫妻共同债务", "concept", "重要", "中国", "民法·婚姻家庭",
          "夫妻共同债务是夫妻双方共同签名或者夫妻一方事后追认等共同意思表示所负的债务，以及夫妻一方在婚姻关系存续期间以个人名义为家庭日常生活需要所负的债务。",
          "夫妻一方在婚姻关系存续期间以个人名义超出家庭日常生活需要所负的债务，债权人能够证明该债务用于夫妻共同生活、共同生产经营或者基于夫妻双方共同意思表示的，属于夫妻共同债务。",
          ["src-law-civil-code", "src-jd-civil-marriage", "src-zgbk"], related=["civil-marriage", "civil-divorce", "civil-contract"]),
    ],
    "u07": [
        E("env-climate-adaptation", "气候适应", "concept", "补充", "中国", "环境法·气候变化",
          "气候适应是通过调整自然系统与人类活动，降低气候变化不利影响和风险的制度与行动，包括基础设施韧性、农业适应、水资源管理、公共卫生与灾害风险管理。",
          "气候适应与减缓并重，国家通过适应气候变化战略、规划与地方行动提升气候韧性；具体政策以国家发展改革委、生态环境部等官方文件为准。",
          ["src-law-environment", "src-zgbk"], related=["env-climate", "env-ecological", "admin-public-health-emergency"],
          pending="国家适应气候变化战略与地方实施方案需按官方最新文件核对。", needs_verification=True),
        E("data-data-governance", "数据治理", "concept", "补充", "中国", "数据法·数据治理",
          "数据治理是围绕数据质量、数据安全、数据流通与数据价值实现而建立的制度、组织与技术措施的总称。",
          "数据治理包括数据分类分级、质量管理、安全管理、权限控制、生命周期管理与合规审计；企业应建立数据治理组织与制度。",
          ["src-law-data-security", "src-zgbk"], related=["data-security", "data-classification", "data-important-data"],
          pending="数据治理相关国家标准与行业规范需按全国信标委/行业主管部门文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-international-watercourses", "国际水道法", "concept", "补充", "国际", "国际公法·国际水道",
          "国际水道法是规范跨国河流、湖泊等国际水道利用与保护的规则，核心原则包括公平合理利用、不造成重大损害、合作与通知协商。",
          "1997年《国际水道非航行使用法公约》是重要渊源，但尚未普遍生效；相关规则也体现在双边条约与习惯法中。",
          ["src-un-charter", "src-icj", "src-zgbk"], related=["intl-sources", "intl-treaty", "env-water-pollution"],
          pending="《国际水道非航行使用法公约》生效状态与相关条约需按联合国资料核对。", needs_verification=True),
    ],
}
