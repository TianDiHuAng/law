# -*- coding: utf-8 -*-
"""R42 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R42 = {
    "u02": [
        E("admin-mediation", "行政调解", "concept", "补充", "中国", "行政法学·行政调解",
          "行政调解是行政机关依据职权或当事人申请，对与其行政管理职责相关的民事纠纷或行政争议，通过说服疏导促使当事人自愿达成协议的活动。",
          "行政调解不具有强制执行力，调解协议主要依靠当事人自愿履行；涉及民事权利义务的调解协议可依法申请司法确认。",
          ["src-law-admin-litigation", "src-zgbk"], related=["admin-act", "proc-civil-mediation", "admin-litigation"],
          pending="行政调解的适用范围与程序缺乏统一立法，需按各部门法规定核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-confusion", "混同", "concept", "补充", "中国", "民法·债的消灭",
          "混同是债权与债务同归于一人，致使债的关系消灭的事实；混同多见于企业合并、继承等情形。",
          "混同导致债权债务终止，但债权为他人权利标的时，债的关系不消灭，以保护第三人利益。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-obligation-extinction", "civil-offset", "com-company"]),
    ],
    "u07": [
        E("data-asset-recognition", "数据资产入表", "concept", "补充", "中国", "数据法·数据要素市场",
          "数据资产入表是企业将符合条件的数据资源确认为资产并纳入财务报表的会计处理实践，涉及数据资源确认为无形资产或存货等科目。",
          "入表需满足会计确认条件，包括可辨认性、控制与经济利益很可能流入；具体规则以财政部相关会计准则与暂行规定为准。",
          ["src-law-data-security", "src-zgbk"], related=["data-data-governance", "data-public-data-open", "data-data-trust"],
          pending="财政部《企业数据资源相关会计处理暂行规定》的具体适用需按官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-development-finance", "国际发展融资", "concept", "补充", "国际", "国际经济法·发展融资",
          "国际发展融资是通过多边开发银行、双边援助与开发性金融机构为发展中国家提供资金与技术支持的国际合作机制。",
          "国际发展融资涉及贷款条件、主权担保、环境与社会保障标准以及债务可持续性等问题，规则以各开发机构章程与政策为准。",
          ["src-un-treaty", "src-icsid", "src-zgbk"], related=["intl-development-law", "intl-financial-law", "intl-investment"],
          pending="世界银行与亚投行等机构的具体融资政策需按各机构官方文本核对。", needs_verification=True),
    ],
}