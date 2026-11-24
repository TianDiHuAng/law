# -*- coding: utf-8 -*-
"""R57 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R57 = {
    "u02": [
        E("admin-administrative-plan", "行政计划", "concept", "补充", "中国", "行政法学·行政计划",
          "行政计划是行政机关为达成特定行政目标，就未来一定时期内的方法、步骤与资源配置作出的规划性安排，如经济社会发展规划、国土空间规划。",
          "行政计划多具指导性与政策性，部分规划经法定程序后具有约束力；计划制定应履行公众参与、专家论证与合法性审查等程序。",
          ["src-law-admin-license", "src-zgbk"], related=["admin-act", "admin-principles", "admin-administrative-guidance"],
          pending="行政计划的统一程序规则缺乏专门立法，需按各领域规划法规核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-alternative-obligation", "选择之债与任意之债", "concept", "重要", "中国", "民法·债法总论",
          "选择之债是债的标的有多项，须经选择确定一项履行的债；任意之债是原则上以特定标的为给付，但债务人可用其他标的替代履行的债。",
          "选择之债的选择权原则上归债务人，行使后标的确定；选择权行使后不得随意撤回，选择权人怠于行使时可由对方或法院确定。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-obligation-extinction", "civil-contract", "civil-conditional-obligation"]),
    ],
    "u07": [
        E("data-space-governance", "数据空间治理规则", "concept", "补充", "中国", "数据法·数据基础设施",
          "数据空间治理规则是围绕数据空间的建设、接入、使用与安全形成的制度与标准，涵盖身份互认、数据目录、使用控制与审计追溯。",
          "治理规则强调数据主权与可控共享，需在互操作与安全之间取得平衡；我国相关规则以行业与地方试点为主，尚在完善之中。",
          ["src-law-data-security", "src-zgbk"], related=["data-data-space", "data-trusted-circulation", "data-security-standards"],
          pending="数据空间治理的国家标准与试点规则需按国家数据局等官方文件核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-cisg-application", "国际货物买卖合同的公约适用", "concept", "补充", "国际", "国际经济法·国际货物买卖",
          "《联合国国际货物销售合同公约》（CISG）适用于营业地在不同缔约国的当事人之间的货物销售合同，当事人可依意思自治排除其适用。",
          "CISG 就合同成立、货物相符、风险转移、违约救济等作出统一规定，但对合同效力、所有权转移等事项未作规定，依国内法补充。",
          ["src-un-treaty", "src-zgbk"], related=["intl-wto", "intl-commercial-arbitration", "civil-contract"],
          pending="CISG 在中国的保留声明与最新缔约国情况需按联合国国际贸易法委员会官方资料核对。", needs_verification=True),
    ],
}