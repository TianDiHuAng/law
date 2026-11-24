# -*- coding: utf-8 -*-
"""R17 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R17 = {
    "u03": [
        E("civil-contract-preservation", "合同保全", "concept", "重要", "中国", "民法·合同保全",
          "合同保全是法律为防止债务人财产不当减少而损害债权人利益，允许债权人行使代位权与撤销权的制度。",
          "代位权针对债务人怠于行使其到期债权或与债权有关的从权利；撤销权针对债务人无偿处分财产、以明显不合理价格交易等损害债权的行为。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-contract-liability", "proc-civil-enforcement"]),
    ],
    "u07": [
        E("data-important-data", "重要数据", "concept", "重要", "中国", "数据法·数据安全",
          "重要数据是指一旦遭到篡改、破坏、泄露或者非法获取、非法利用，可能危害国家安全、公共利益的数据，其具体范围由行业主管部门依法确定。",
          "重要数据处理者应明确数据安全负责人与管理机构，开展风险评估，并向主管部门报送风险评估报告；重要数据出境须依法进行安全评估。",
          ["src-law-data-security", "src-zgbk"], related=["data-classification", "data-cross-border", "data-security"],
          pending="重要数据目录与识别指南需按国家网信部门及行业主管部门官方文本核对。", needs_verification=True),
        E("env-ecological-redline", "生态保护红线", "concept", "补充", "中国", "环境法·生态空间",
          "生态保护红线是在生态空间范围内具有特殊重要生态功能、必须强制性严格保护的区域，是保障国家生态安全的底线。",
          "生态保护红线划定后应严格保护，禁止不符合主体功能定位的各类开发建设活动；红线调整须依法定程序。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-ecological", "env-eia"],
          pending="生态保护红线划定与管控规则需按自然资源部、生态环境部官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-trade-services", "国际服务贸易", "concept", "补充", "国际", "国际经济法·服务贸易",
          "国际服务贸易是跨越国界提供服务的贸易活动，WTO《服务贸易总协定》（GATS）将其分为跨境交付、境外消费、商业存在与自然人流动四种模式。",
          "GATS确立最惠国待遇、国民待遇、市场准入与透明度等规则，具体承诺依各成员服务贸易减让表确定。",
          ["src-wto", "src-zgbk"], related=["intl-wto", "intl-wto-dispute", "intl-investment"],
          pending="GATS具体承诺与我国服务贸易开放措施需按WTO与商务部官方文本核对。", needs_verification=True),
    ],
}
