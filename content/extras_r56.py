# -*- coding: utf-8 -*-
"""R56 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R56 = {
    "u02": [
        E("admin-administrative-reward", "行政奖励", "concept", "补充", "中国", "行政法学·行政奖励",
          "行政奖励是行政机关依法对作出突出贡献或模范遵守法律的主体给予物质或精神奖励的行为，属于激励性行政行为。",
          "行政奖励应依法定条件与程序实施，遵循公开、公平原则；对符合条件的相对人，行政机关不得无正当理由拒绝或差别对待。",
          ["src-law-admin-license", "src-zgbk"], related=["admin-act", "admin-administrative-guidance", "admin-principles"],
          pending="行政奖励缺乏统一立法，具体规定分散于各部门法与政策文件。", needs_verification=True),
    ],
    "u03": [
        E("civil-joint-debt", "连带债务", "concept", "重要", "中国", "民法·债法总论",
          "连带债务是数个债务人对同一债务各负全部给付义务，债权人可向任一债务人请求全部或部分履行，任一债务人履行后债务在相应范围内消灭。",
          "连带债务的成立须有法律规定或当事人约定；连带债务人内部按份额分担，实际承担超过自己份额的债务人有权向其他债务人追偿。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-guarantee", "civil-joint-guarantee", "civil-obligation-transfer"]),
    ],
    "u07": [
        E("data-trust-practice", "数据信托的实践形态", "concept", "补充", "中国", "数据法·数据治理",
          "数据信托的实践形态是数据信托理念在行业中的具体落地形式，包括数据受托运营、数据共享信托与个人数据代理等模式。",
          "实践形态多处于试点与探索阶段，需处理数据权属、受托人信义义务、收益分配与个人信息保护等难题，具体依约定与监管要求。",
          ["src-law-personal-info-2", "src-wiki-trust-law", "src-zgbk"], related=["data-data-trust", "data-trusted-circulation", "com-trust"],
          pending="数据信托试点案例与监管态度需持续跟踪官方与行业实践。", needs_verification=True),
    ],
    "u08": [
        E("intl-arbitrator-disclosure", "仲裁员的回避与披露", "concept", "补充", "国际", "国际私法·国际仲裁",
          "仲裁员的回避与披露是保障仲裁公正的程序制度：仲裁员应披露可能影响公正性的情形，当事人可依规则申请其回避。",
          "披露义务贯穿仲裁全过程；回避事由包括与当事人或案件存在利害关系等；回避决定由仲裁机构或仲裁庭依规则作出。",
          ["src-un-treaty", "src-zgbk"], related=["intl-commercial-arbitration", "proc-arbitration", "intl-tpf"],
          pending="各仲裁机构规则关于披露标准与回避程序的具体规定需按机构规则核对。", needs_verification=True),
    ],
}