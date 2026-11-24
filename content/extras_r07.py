# -*- coding: utf-8 -*-
"""R07 新增条目。"""
from common import E

EXTRAS_R07 = {
    "u02": [
        E("admin-government-info", "政府信息公开", "concept", "重要", "中国", "行政法学·政府信息公开",
          "政府信息公开是行政机关依法主动公开或者依申请向公民、法人和其他组织提供政府信息的制度。",
          "政府信息公开以公开为常态、不公开为例外，遵循公正、公平、合法、便民原则；涉及国家秘密、商业秘密、个人隐私等依法不予公开。",
          ["src-reg-government-info", "src-zgbk", "src-gov-cn"],
          related=["admin-act", "admin-litigation", "const-rights"]),
    ],
    "u03": [
        E("civil-guarantee", "保证合同", "concept", "重要", "中国", "民法·典型合同",
          "保证合同是为保障债权的实现，保证人和债权人约定，当债务人不履行到期债务或者发生当事人约定的情形时，保证人履行债务或者承担责任的合同。",
          "保证分为一般保证与连带责任保证；保证人承担保证责任后，有权向债务人追偿，但不得损害债权人的利益。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-security", "com-bankruptcy"]),
        E("civil-property-service", "物业服务合同", "concept", "重要", "中国", "民法·典型合同",
          "物业服务合同是物业服务人在物业服务区域内，为业主提供建筑物及其附属设施的维修养护、环境卫生和相关秩序的管理维护等物业服务，业主支付物业费的合同。",
          "物业服务合同对业主具有法律约束力；物业服务人不得采取停止供电、供水、供热、供燃气等方式催交物业费。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-ownership", "proc-civil-mediation"]),
    ],
    "u06": [
        E("com-partnership", "合伙企业法", "concept", "重要", "中国", "商法·合伙企业",
          "合伙企业是自然人、法人和其他组织依法设立的，由合伙人订立合伙协议，共同出资、合伙经营、共享收益、共担风险的企业组织形式。",
          "普通合伙人对合伙企业债务承担无限连带责任，有限合伙人以认缴出资额为限承担责任；合伙企业不具有法人资格。",
          ["src-npc", "src-zgbk", "src-wiki-partnership"], related=["com-company", "com-bankruptcy", "civil-legal-person"]),
        E("com-trust", "信托法", "concept", "重要", "中国", "商法·信托",
          "信托是委托人基于对受托人的信任，将其财产权委托给受托人，由受托人按委托人的意愿以自己的名义，为受益人的利益或者特定目的进行管理或者处分的行为。",
          "信托财产独立于委托人、受托人和受益人的固有财产；受托人负有忠实义务与谨慎义务。",
          ["src-wiki-trust-law", "src-zgbk", "src-npc"], related=["com-company", "civil-contract", "intl-investment"]),
    ],
    "u08": [
        E("intl-organization-law", "国际组织法", "concept", "补充", "国际", "国际公法·国际组织",
          "国际组织法是规范政府间国际组织的法律地位、组织机构、职权、决策程序及其与成员国关系的国际法分支。",
          "国际组织依条约设立，具有独立的国际法律人格与特权豁免；联合国是当今最具普遍性的政府间国际组织。",
          ["src-un-charter", "src-icj", "src-zgbk"], related=["intl-sources", "intl-treaty", "intl-human-rights"],
          pending="各国际组织的基本文件与特权豁免公约需按组织官方文本核对。", needs_verification=True),
    ],
}
