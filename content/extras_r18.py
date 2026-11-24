# -*- coding: utf-8 -*-
"""R18 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R18 = {
    "u03": [
        E("civil-good-faith", "诚信原则", "concept", "重要", "中国", "民法·基本原则",
          "诚信原则是民事主体从事民事活动应当秉持诚实、恪守承诺的原则，要求当事人善意行使权利、履行义务。",
          "诚信原则贯穿民事活动的全过程，可用于解释法律行为、补充合同漏洞、限制权利滥用，是民法典的基本原则之一。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-general", "civil-act", "civil-contract"]),
    ],
    "u07": [
        E("data-data-breach", "数据泄露通知", "concept", "重要", "中国", "数据法·个人信息保护",
          "数据泄露通知是个人信息处理者在发生或者可能发生个人信息泄露、篡改、丢失时，应当立即采取补救措施并通知履行个人信息保护职责的部门和个人。",
          "通知应说明泄露信息的种类、原因、可能造成的危害、已采取的补救措施以及个人可采取的减轻危害的措施；无法逐一通知的应公告。",
          ["src-law-personal-info-2", "src-law-data-security", "src-zgbk"], related=["data-personal", "data-security", "data-important-data"],
          pending="数据泄露通知的具体时限与报告格式需按国家网信部门官方文本核对。", needs_verification=True),
        E("env-carbon-market", "碳排放权交易", "concept", "补充", "中国", "环境法·碳市场",
          "碳排放权交易是通过市场机制配置碳排放配额，促使企业减排的制度；政府确定排放总量与配额分配，重点排放单位在碳市场买卖配额。",
          "中国已建立全国碳排放权交易市场，覆盖发电等重点行业，并逐步扩大行业范围；碳市场监管规则以生态环境部官方文本为准。",
          ["src-law-environment", "src-zgbk"], related=["env-climate", "env-law", "env-ecological"],
          pending="全国碳市场扩围与交易规则需按生态环境部最新文件核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-commercial-arbitration", "国际商事仲裁", "concept", "补充", "国际", "国际私法·国际商事仲裁",
          "国际商事仲裁是当事人依仲裁协议将具有涉外因素的商事争议提交仲裁机构或临时仲裁庭审理并作出裁决的制度。",
          "国际商事仲裁以《纽约公约》为承认与执行的核心框架，具有一裁终局、程序灵活、保密性强等特点。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["proc-arbitration", "intl-private", "intl-investment"],
          pending="《纽约公约》适用与主要仲裁机构规则需按联合国及仲裁机构官方文本核对。", needs_verification=True),
    ],
}
