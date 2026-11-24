# -*- coding: utf-8 -*-
"""R54 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R54 = {
    "u02": [
        E("admin-administrative-charge", "行政收费", "concept", "补充", "中国", "行政法学·行政收费",
          "行政收费是行政机关或法定组织依法向特定相对人收取费用，以补偿特定行政服务成本或调节资源使用的行为，如证照工本费、排污费（已改税）等。",
          "行政收费须有法律、法规依据并实行目录清单管理，收费标准应公开；无依据收费、超标准收费的，相对人可依法申请退还并寻求救济。",
          ["src-law-admin-license", "src-zgbk"], related=["admin-license", "admin-penalty", "admin-compensation"],
          pending="行政收费的项目与标准需按财政部、发展改革委的收费目录清单核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-transfer-security", "让与担保", "concept", "补充", "中国", "民法·非典型担保",
          "让与担保是债务人或第三人将标的物所有权（或股权等权利）移转给债权人，以担保债务履行的非典型担保方式，债务清偿后标的物返还。",
          "让与担保虽非民法典明定的典型担保，但司法实践通过合同解释与清算义务规则予以承认，禁止流质式约定，债权人负有清算义务。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-security", "civil-guarantee", "civil-property"],
          pending="让与担保的效力与清算规则需按最高人民法院担保制度解释与裁判规则核对。", needs_verification=True),
    ],
    "u07": [
        E("data-cross-border-case-types", "数据出境案例的类型化", "concept", "补充", "中国", "数据法·数据跨境",
          "数据出境案例的类型化是对实践中因数据出境引发的合规争议、行政处罚与司法纠纷，按出境路径、数据类型与违法情形进行归类分析的方法。",
          "常见类型包括未申报安全评估即出境、以标准合同规避评估、境外接收方超范围使用数据、重要数据识别错误等，反映合规落地难点。",
          ["src-law-personal-info-2", "src-law-data-security", "src-zgbk"], related=["data-cross-border", "data-cross-border-cases", "data-export-assessment"],
          pending="公开的数据出境执法与司法案例有限，类型化结论需随监管实践更新。", needs_verification=True),
    ],
    "u08": [
        E("intl-investment-appeal-reform", "国际投资仲裁的上诉机制改革", "concept", "补充", "国际", "国际经济法·投资仲裁改革",
          "国际投资仲裁的上诉机制改革是针对现行投资仲裁缺乏上诉审查、裁决一致性不足等问题，推动建立多边上诉机制或常设投资法院的改革议题。",
          "相关改革包括联合国国际贸易法委员会第三工作组关于投资者与国家间争端解决改革的讨论，以及欧盟倡导的多边投资法院方案。",
          ["src-un-treaty", "src-icsid", "src-zgbk"], related=["intl-investment-arbitration", "intl-treaty-interpretation-investment", "intl-commercial-arbitration"],
          pending="UNCITRAL 第三工作组改革进程与各国立场需按联合国官方文件核对。", needs_verification=True),
    ],
}