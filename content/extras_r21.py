# -*- coding: utf-8 -*-
"""R21 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R21 = {
    "u03": [
        E("civil-contract-interpretation", "合同解释", "concept", "重要", "中国", "民法·合同解释",
          "合同解释是法院或仲裁机构对合同条款的含义、内容与适用范围进行阐明，以确定当事人权利义务的活动。",
          "合同解释应按照所使用的词句，结合相关条款、行为的性质和目的、习惯以及诚信原则，确定意思表示的含义。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-contract-formation", "civil-good-faith"]),
    ],
    "u07": [
        E("data-pia", "个人信息保护影响评估", "concept", "重要", "中国", "数据法·个人信息保护",
          "个人信息保护影响评估是个人信息处理者在处理敏感个人信息、利用个人信息进行自动化决策、委托处理、向他人提供、公开个人信息或向境外提供个人信息等情形下，对处理活动对个人权益的影响进行事前评估的制度。",
          "影响评估应针对处理目的、处理方式、个人信息种类、对个人权益的影响及安全风险等作出评估，并保存评估报告至少三年。",
          ["src-law-personal-info-2", "src-law-data-security", "src-zgbk"], related=["data-personal", "data-sensitive-personal", "data-cross-border"],
          pending="个人信息保护影响评估的具体模板与监管要求需按国家网信部门规定核对。", needs_verification=True),
        E("env-biodiversity", "生物多样性保护", "concept", "补充", "中国", "环境法·生物多样性",
          "生物多样性保护是保护生态系统、物种和遗传资源多样性，维护生态平衡与生态安全的制度。",
          "中国通过自然保护区、国家公园、生物安全、外来物种入侵防控与遗传资源保护等制度履行《生物多样性公约》义务。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-ecological", "env-wetland"],
          pending="生物多样性保护法立法进展与配套名录需按官方最新文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-judicial-assistance", "国际刑事司法协助", "concept", "补充", "国际", "国际公法·国际刑事司法合作",
          "国际刑事司法协助是国家之间在刑事犯罪侦查、起诉、审判和执行中相互提供协助的制度，包括引渡、送达文书、调查取证、查封扣押冻结、移送被判刑人等。",
          "国际刑事司法协助以双边条约、多边公约或互惠原则为基础，遵循双重犯罪、政治犯不引渡等原则。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["intl-international-criminal", "intl-icc", "crim-investigation"],
          pending="中国缔结的刑事司法协助条约与引渡条约清单需按外交部官方资料核对。", needs_verification=True),
    ],
}
