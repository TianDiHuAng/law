# -*- coding: utf-8 -*-
"""R43 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R43 = {
    "u02": [
        E("admin-high-power-act", "行政协议中的高权行为", "concept", "补充", "中国", "行政法学·行政协议",
          "行政协议中的高权行为是行政机关在协议履行过程中，为公共利益需要依法单方变更或解除协议的权力，也称优益权。",
          "高权行为须有法律依据并遵守法定程序，给对方造成损失的应当依法给予补偿；相对人可对此提起行政诉讼。",
          ["src-law-admin-litigation", "src-zgbk"], related=["admin-administrative-agreement", "admin-agreement-rules", "admin-compensation"],
          pending="行政机关优益权的具体范围与补偿标准需按司法解释与实务案例核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-performance-appropriation", "清偿抵充", "concept", "补充", "中国", "民法·债的消灭",
          "清偿抵充是债务人对同一债权人负担数项同类债务，而给付不足以清偿全部债务时，确定该给付抵充哪一债务的规则。",
          "抵充顺序依次为：当事人约定、指定抵充、法定抵充；法定抵充中优先抵充已到期债务、对债权人利益较少的债务、先到期债务等。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-obligation-extinction", "civil-offset", "civil-contract"]),
    ],
    "u07": [
        E("data-factor-market", "数据要素市场", "concept", "补充", "中国", "数据法·数据要素",
          "数据要素市场是数据作为生产要素进行确权、定价、交易与流通的制度与市场体系，涵盖数据产权、流通交易、收益分配与安全治理。",
          "中国推进数据要素市场化配置改革，建立数据产权结构性分置、数据交易场所与数据要素登记等制度；具体规则以国家数据局等官方文件为准。",
          ["src-law-data-security", "src-zgbk"], related=["data-data-governance", "data-asset-recognition", "data-public-data-open"],
          pending="数据要素市场化配置改革文件与数据产权登记规则需按国家数据局官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-award-setting-aside", "国际仲裁裁决的撤销与不予执行", "concept", "补充", "国际", "国际私法·国际仲裁监督",
          "国际仲裁裁决的撤销与不予执行是法院依当事人申请，对存在法定瑕疵的仲裁裁决进行司法监督的制度。",
          "《纽约公约》确立不予承认与执行的有限事由，包括仲裁协议无效、程序不当、超裁、裁决未生效或被撤销等；撤销通常由仲裁地法院管辖。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["intl-commercial-arbitration", "proc-arbitration", "intl-investment-arbitration"],
          pending="《纽约公约》第五条各款的具体适用需按联合国与各国法院判例核对。", needs_verification=True),
    ],
}