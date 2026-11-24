# -*- coding: utf-8 -*-
"""R12 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R12 = {
    "u03": [
        E("civil-adoption", "收养制度", "concept", "重要", "中国", "民法·婚姻家庭",
          "收养是自然人依法领养他人子女为自己子女，使收养人与被收养人之间形成拟制血亲关系的法律行为。",
          "收养须符合收养人与被收养人条件并依法办理登记；收养关系成立后，养父母与养子女间的权利义务适用父母子女关系的规定。",
          ["src-law-civil-code", "src-jd-civil-marriage", "src-zgbk"], related=["civil-marriage", "civil-inheritance", "civil-person"]),
    ],
    "u07": [
        E("data-automated-decision", "自动化决策", "concept", "重要", "中国", "数据法·个人信息保护",
          "自动化决策是利用个人信息，通过计算机程序自动分析、评估个人的行为习惯、兴趣爱好或者经济、健康、信用状况等，并进行决策的活动。",
          "个人信息保护法要求自动化决策透明、结果公平公正，不得对个人在交易价格等交易条件上实行不合理的差别待遇；通过自动化决策方式作出对个人权益有重大影响的决定，个人有权要求说明并拒绝。",
          ["src-law-personal-info-2", "src-zgbk"], related=["data-personal", "data-algorithm", "data-security"],
          pending="自动化决策相关配套规定与算法备案要求需按国家网信部门官方文本核对。", needs_verification=True),
        E("env-soil-pollution", "土壤污染防治", "concept", "重要", "中国", "环境法·土壤保护",
          "土壤污染防治是预防、控制、修复土壤污染，保障土壤环境质量、农产品质量安全和公众健康的法律制度。",
          "土壤污染防治坚持预防为主、保护优先、分类管理、风险管控、污染担责、公众参与原则；土地使用权人负有土壤污染风险管控和修复义务。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-pollution", "env-ecological"],
          pending="土壤污染防治法及配套标准需按生态环境部现行文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-diplomatic-law", "外交关系法", "concept", "补充", "国际", "国际公法·外交与领事关系",
          "外交关系法是规范国家之间外交关系、外交代表机关与外交人员地位和特权豁免的国际法分支，核心渊源为1961年《维也纳外交关系公约》。",
          "外交关系法确立使馆馆舍不可侵犯、外交人员人身不可侵犯与外交豁免等规则；领事关系另有1963年《维也纳领事关系公约》规范。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["intl-sources", "intl-sovereignty", "intl-organization-law"],
          pending="《维也纳外交关系公约》具体条文与各国实践需按联合国条约集核对。", needs_verification=True),
    ],
}
