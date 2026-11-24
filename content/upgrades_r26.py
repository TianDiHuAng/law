# -*- coding: utf-8 -*-
"""R26 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R26 = {
    "const-history": dict(
        definition_source="《中华人民共和国宪法》序言及历次修正案（版本：2018年修正，核对日期：2026-11-24）。",
        elements=["清末立宪", "民国宪法", "1954年宪法", "1982年宪法", "五次修正"],
        conditions=["历史阶段与政治体制变迁", "宪法制定或修改的法定程序"],
        effects=["确立不同时期的根本制度", "1982年宪法成为现行宪法", "修正案不断完善宪法制度"],
        exceptions=["宪法修正须依特别程序", "历史文件的性质与效力需具体分析"],
        cases=[],
        controversies=[dict(issue="宪法史的分期",
                            views=[dict(holder="革命史观", basis="以革命与政权更替为分期主线"),
                                   dict(holder="制度史观（部分学者）", basis="以宪制结构与权利保障演变为主线")])],
        distinctions=[D("宪法史", "宪法制度的历史演变"), D("法制史", "整体法律制度的历史")],
        misconceptions=[dict(claim="新中国只有1982年宪法", correction="1954年宪法是第一部，1982年宪法是现行宪法"),
                        dict(claim="宪法修正与普通法律相同", correction="宪法修改适用更严格的提议与表决程序")],
    ),
    "const-review": dict(
        definition_source="《中华人民共和国宪法》第五条、第六十二条、第六十七条及《立法法》相关规定（版本：2018年修正/2023年修正，核对日期：2026-11-24）。",
        elements=["审查主体", "审查对象", "审查程序", "审查结论"],
        conditions=["法律、法规、规范性文件可能同宪法相抵触", "有关主体依法提出审查要求或建议", "审查机关依法处理"],
        effects=["违宪的规范性文件可被纠正或撤销", "保障宪法统一实施", "维护法制统一"],
        exceptions=["宪法不直接作为具体案件裁判依据", "合宪性审查与合法性审查有分工"],
        cases=["case-qiyuling"],
        controversies=[dict(issue="合宪性审查的模式",
                            views=[dict(holder="立法机关审查说（现行制度）", basis="全国人大及其常委会行使宪法监督权"),
                                   dict(holder="司法审查说（部分学者）", basis="应建立法院合宪性审查机制")])],
        distinctions=[D("合宪性审查", "审查是否符合宪法"), D("合法性审查", "审查是否符合法律、法规")],
        misconceptions=[dict(claim="合宪性审查就是违宪审查", correction="合宪性审查包括事前与事后审查，不限于宣告违宪"),
                        dict(claim="所有规范性文件都可直接起诉", correction="合宪性审查有法定主体与程序")],
    ),
    "const-state-organs": dict(
        definition_source="《中华人民共和国宪法》第三章国家机构（版本：2018年修正，核对日期：2026-11-24）。",
        elements=["全国人大及其常委会", "国家主席", "国务院", "中央军委", "监察委员会", "人民法院", "人民检察院"],
        conditions=["依宪法与法律规定设置", "依法行使职权", "对人民负责、受人民监督"],
        effects=["国家权力依法运行", "国家机关相互配合、相互制约", "公民权利获得组织保障"],
        exceptions=["特别行政区实行不同制度", "民族自治地方自治机关依法行使自治权"],
        cases=[],
        controversies=[dict(issue="监察委员会的地位",
                            views=[dict(holder="独立监察机关说", basis="监察委员会由人大产生，独立行使监察权"),
                                   dict(holder="行政监察延续说（部分观点）", basis="监察权与行政权的关系需进一步厘清")])],
        distinctions=[D("国家机构", "行使国家权力的机关体系"), D("社会组织", "非国家权力主体")],
        misconceptions=[dict(claim="国家机构只有行政机关", correction="还包括权力机关、监察机关、审判机关、检察机关等"),
                        dict(claim="国家机关可以超越宪法行使权力", correction="一切国家机关都必须遵守宪法和法律")],
    ),
    "const-autonomy": dict(
        definition_source="《中华人民共和国宪法》第四条、第三章第六节及《民族区域自治法》（版本：2018年修正，核对日期：2026-11-24）。",
        elements=["自治地方", "自治机关", "自治权", "国家统一"],
        conditions=["少数民族聚居地方", "依法设立自治区、自治州、自治县", "自治机关依法产生"],
        effects=["自治机关行使自治权", "自治条例和单行条例依法制定", "国家统一与民族团结得到保障"],
        exceptions=["自治权不得违背宪法和法律", "特别行政区制度与民族区域自治不同"],
        cases=[],
        controversies=[dict(issue="自治权的范围",
                            views=[dict(holder="法定自治说", basis="自治权以宪法和民族区域自治法规定为限"),
                                   dict(holder="扩展自治说（部分观点）", basis="应进一步扩大自治地方在经济、文化等领域的自主权")])],
        distinctions=[D("民族区域自治", "少数民族聚居地方的区域自治"), D("特别行政区", "实行高度自治的特别制度")],
        misconceptions=[dict(claim="自治地方可以脱离国家统一", correction="民族区域自治以国家统一为前提"),
                        dict(claim="自治权等于完全自治", correction="自治权依法行使，不得违背宪法和法律")],
    ),
}
