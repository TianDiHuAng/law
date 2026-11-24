# -*- coding: utf-8 -*-
"""R36 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R36 = {
    "u02": [
        E("admin-reconsideration-enforcement", "行政复议决定的执行", "concept", "补充", "中国", "行政法学·行政复议",
          "行政复议决定的执行是复议机关作出撤销、变更、责令履行等决定后，被申请行政机关依法履行，以及申请人、第三人依法履行复议决定的制度。",
          "被申请人不履行或无正当理由拖延履行复议决定的，复议机关或有关上级行政机关应责令限期履行；对拒不履行的直接责任人员依法追责。",
          ["src-law-admin-reconsideration", "src-law-admin-litigation", "src-zgbk"],
          related=["admin-reconsideration", "admin-reconsideration-prerequisite", "admin-litigation"],
          pending="行政复议法关于执行与督办的具体条文需按2023年修订文本核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-obligation-transfer", "债的移转", "concept", "重要", "中国", "民法·债法总论",
          "债的移转是债的内容不变而主体发生变更，包括债权让与、债务承担与债权债务概括移转。",
          "债权让与须通知债务人，未经通知不对债务人生效；债务承担须经债权人同意；概括移转须经对方同意并依法办理。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-obligation-extinction", "civil-privity"]),
    ],
    "u07": [
        E("data-mlps", "网络安全等级保护制度", "concept", "补充", "中国", "数据法·网络安全",
          "网络安全等级保护制度是对网络按其在国家安全、经济建设、社会生活中的重要程度划分为不同保护等级，并按等级落实安全保护义务的制度。",
          "网络运营者应履行等级保护义务，包括定级备案、安全建设整改、等级测评与监督检查；关键信息基础设施在等级保护基础上实行重点保护。",
          ["src-law-network-security-2", "src-zgbk"], related=["data-network", "data-critical-infrastructure", "data-security"],
          pending="网络安全等级保护条例与定级指南需按公安部现行文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-competition-law", "国际竞争法", "concept", "补充", "国际", "国际经济法·竞争法",
          "国际竞争法是协调各国竞争法域外适用、跨境并购审查与反垄断执法合作的国际规则与合作机制。",
          "国际竞争法目前以双边合作协定、区域竞争规则与软法性质的国际竞争网络（ICN）建议为主，尚缺乏统一的多边竞争法典。",
          ["src-un-treaty", "src-zgbk"], related=["ip-anti-unfair", "intl-wto", "intl-sources"],
          pending="主要辖区竞争执法合作协定与并购审查协调机制需按各执法机构官方文本核对。", needs_verification=True),
    ],
}