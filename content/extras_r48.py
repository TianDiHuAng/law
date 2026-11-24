# -*- coding: utf-8 -*-
"""R48 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R48 = {
    "u02": [
        E("admin-license-delegation", "行政许可的委托与代理", "concept", "补充", "中国", "行政法学·行政许可",
          "行政许可的委托是行政机关依法将许可实施权委托给其他行政机关行使；代理则是申请人委托他人代为办理许可申请手续。",
          "委托须有法律、法规、规章依据，委托机关对受委托机关的许可行为承担法律责任；申请代理须提交授权委托书与身份证明。",
          ["src-law-admin-license", "src-zgbk"], related=["admin-license", "admin-principles", "admin-license-renewal"]),
    ],
    "u03": [
        E("civil-assignment-notice", "债权让与通知", "concept", "重要", "中国", "民法·债的移转",
          "债权让与通知是债权人将其债权转让给第三人后，向债务人告知转让事实的行为；未经通知，该转让对债务人不发生效力。",
          "通知应由让与人作出，受让人持债权转让凭证通知的亦可；债务人收到通知后，可向受让人主张对让与人的抗辩。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-obligation-transfer", "civil-debt-joinder", "civil-contract"]),
    ],
    "u07": [
        E("data-revenue-sharing", "数据要素收益分配", "concept", "补充", "中国", "数据法·数据要素",
          "数据要素收益分配是数据价值链各参与方之间就数据开发利用所得收益进行分配的机制，涉及数据来源者、处理者与经营者之间的利益平衡。",
          "中国推进按贡献决定报酬的分配机制，强调保护数据来源者权益；具体规则以数据要素市场化配置改革文件为准。",
          ["src-law-data-security", "src-law-personal-info-2", "src-zgbk"], related=["data-factor-market", "data-asset-recognition", "data-data-governance"],
          pending="数据要素收益分配的具体规则尚在探索，需跟踪国家数据局官方文件。", needs_verification=True),
    ],
    "u08": [
        E("intl-tpf", "国际仲裁中的第三方资助", "concept", "补充", "国际", "国际私法·国际仲裁",
          "第三方资助是仲裁一方当事人之外的实体为其提供仲裁费用，并在胜诉时按约定分享裁决收益的安排。",
          "第三方资助引发利益冲突披露、费用担保与保密特权等争议；部分仲裁规则与投资条约已要求披露资助安排。",
          ["src-un-treaty", "src-zgbk"], related=["intl-commercial-arbitration", "intl-investment-arbitration", "intl-award-setting-aside"],
          pending="各仲裁机构规则关于第三方资助披露的具体要求需按机构规则核对。", needs_verification=True),
    ],
}