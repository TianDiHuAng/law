# -*- coding: utf-8 -*-
"""R47 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R47 = {
    "u02": [
        E("admin-investigation", "行政调查", "concept", "补充", "中国", "行政法学·行政程序",
          "行政调查是行政机关为查明事实、收集证据，依法向有关单位和个人了解情况、调取材料的活动，是作出行政决定的前置环节。",
          "行政调查应遵守法定权限与程序，不得以调查为名实施强制措施；当事人有配合义务，也有权要求调查人员出示证件与说明依据。",
          ["src-law-admin-penalty", "src-law-admin-license", "src-zgbk"],
          related=["admin-penalty", "admin-due-process", "admin-litigation"],
          pending="行政调查的统一程序规则分散于各部门法，缺乏统一行政程序法。", needs_verification=True),
    ],
    "u03": [
        E("civil-guarantee-period", "保证期间", "concept", "重要", "中国", "民法·保证合同",
          "保证期间是债权人应当向保证人主张保证责任的期间，属于除斥期间性质，不发生中止、中断与延长。",
          "保证期间没有约定或约定不明确的为主债务履行期限届满之日起六个月；一般保证中债权人须在保证期间内对债务人提起诉讼或仲裁，连带保证中须向保证人请求。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-guarantee", "civil-guarantee-modes", "civil-limitation"]),
    ],
    "u07": [
        E("data-export-assessment", "数据出境安全评估申报", "concept", "补充", "中国", "数据法·数据跨境",
          "数据出境安全评估申报是符合法定情形的数据处理者向国家网信部门提交材料，由其对数据出境风险进行评估的程序。",
          "申报情形包括关键信息基础设施运营者向境外提供个人信息或重要数据、处理个人信息达到规定数量等；评估结果有效期内可多次出境。",
          ["src-law-personal-info-2", "src-law-data-security", "src-zgbk"], related=["data-cross-border", "data-cross-border-whitelist", "data-important-data"],
          pending="数据出境安全评估办法的申报门槛与有效期需按国家网信办官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-treaty-abuse", "税收协定滥用与防止", "concept", "补充", "国际", "国际经济法·国际税法",
          "税收协定滥用是纳税人通过人为安排套用协定优惠待遇以减轻税负的行为，主要防止工具包括受益所有人规则、主要目的测试与穿透适用。",
          "BEPS 多边公约引入主要目的测试等反滥用规则，各国亦通过国内法一般反避税规则与协定条款应对。",
          ["src-un-treaty", "src-zgbk"], related=["intl-tax-cooperation", "intl-treaty", "intl-financial-law"],
          pending="BEPS 多边公约在中国的适用与主要目的测试实践需按国家税务总局官方资料核对。", needs_verification=True),
    ],
}