# -*- coding: utf-8 -*-
"""R53 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R53 = {
    "u02": [
        E("admin-adjudication-remedy", "行政裁决的救济", "concept", "补充", "中国", "行政法学·行政裁决",
          "行政裁决是行政机关依职权对与行政管理活动密切相关的民事纠纷作出裁断的行为，如土地权属争议、知识产权侵权赔偿数额争议等。",
          "当事人对行政裁决不服的，一般可提起行政诉讼；行政裁决并不排除当事人就原民事争议另行通过民事诉讼解决，具体依法律规定确定。",
          ["src-law-admin-litigation", "src-zgbk"], related=["admin-act", "proc-admin-litigation", "admin-mediation"],
          pending="行政裁决的范围与救济途径分散于各部门法，需按具体领域规定核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-independent-guarantee", "独立保证", "concept", "补充", "中国", "民法·担保制度",
          "独立保证是保证人与债权人约定，其付款义务独立于主合同关系，仅依约定单据或条件履行的保证形式，常见于见索即付保函。",
          "独立保证突破从属性原则，但我国司法实践对独立担保的效力认定较为严格，国内交易中一般依从属性保证处理，涉外见索即付保函依约定与国际惯例。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-guarantee", "civil-joint-guarantee", "intl-commercial-arbitration"],
          pending="独立保证的效力认定与见索即付保函的司法态度需按最高人民法院裁判规则核对。", needs_verification=True),
    ],
    "u07": [
        E("data-classification-practice", "数据分类分级的行业实践", "concept", "补充", "中国", "数据法·数据治理",
          "数据分类分级的行业实践是各行业主管部门依数据安全法要求，结合行业特点制定数据分类分级规则并推动企业落地实施的实践。",
          "金融、电信、汽车、医疗等行业已出台分类分级指南，企业在行业目录基础上建立内部数据清单、定级与差异化保护措施。",
          ["src-law-data-security", "src-zgbk"], related=["data-classification", "data-security-standards", "data-important-data"],
          pending="各行业分类分级指南的现行版本需按行业主管部门官方文件核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-treaty-interpretation-investment", "国际投资条约的解释", "concept", "补充", "国际", "国际经济法·投资条约",
          "国际投资条约的解释是仲裁庭依《维也纳条约法公约》解释规则，对条约术语、保护标准与例外条款含义作出阐释的活动。",
          "解释争议常集中于公平公正待遇、间接征收、保护伞条款与根本安全例外；条约目的与宗旨、缔约方嗣后实践与准备资料均属解释要素。",
          ["src-un-treaty", "src-icsid", "src-zgbk"], related=["intl-investment-arbitration", "intl-treaty", "intl-treaty-domestic"],
          pending="投资条约解释的典型案例与缔约方联合解释实践需按 ICSID 与条约机构资料核对。", needs_verification=True),
    ],
}