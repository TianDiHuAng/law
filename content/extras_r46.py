# -*- coding: utf-8 -*-
"""R46 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R46 = {
    "u02": [
        E("admin-duty-to-give-reasons", "行政决定中的说明理由", "concept", "补充", "中国", "行政法学·行政程序",
          "说明理由是行政机关在作出对相对人不利的决定时，应告知事实依据、法律依据与裁量考量的程序义务，属于正当程序的核心要素。",
          "行政处罚法、行政许可法等法律在听证、决定送达等环节规定了说明理由要求；理由不充分可能构成程序违法或裁量滥用。",
          ["src-law-admin-penalty", "src-law-admin-license", "src-zgbk"],
          related=["admin-due-process", "admin-hearing", "admin-litigation"],
          pending="说明理由在制定法中的具体要求分散，未形成统一程序法典条文。", needs_verification=True),
    ],
    "u03": [
        E("civil-debt-joinder", "债务加入", "concept", "重要", "中国", "民法·债的移转",
          "债务加入是第三人加入债的关系，与债务人共同向债权人承担债务，原债务人并不脱离债的关系。",
          "债务加入须经债权人同意或在合理期限内未表示拒绝；第三人与债务人承担连带债务，但可与债务人约定内部份额。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-obligation-transfer", "civil-guarantee", "civil-contract"]),
    ],
    "u07": [
        E("data-security-standards", "数据安全国家标准体系", "concept", "补充", "中国", "数据法·标准化",
          "数据安全国家标准体系是围绕数据分类分级、安全管理、安全技术、评估认证等形成的推荐性国家标准与行业标准集合。",
          "标准由全国网络安全标准化技术委员会等机构组织制定，企业可依标准落实法定安全义务，但标准本身不替代法律规定。",
          ["src-law-data-security", "src-zgbk"], related=["data-classification", "data-security", "data-pi-certification"],
          pending="具体国家标准编号与现行版本需按全国标准信息公共服务平台核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-river-navigation", "国际河流的航行权", "concept", "补充", "国际", "国际公法·国际水道",
          "国际河流的航行权是沿岸国及特定情形下非沿岸国在跨国河流上从事商业航行的权利，通常由条约确立并受沿岸国管理。",
          "历史上欧洲国际河流实行自由航行制度，现代实践以沿岸国主权为基础，通过双边或多边条约安排航行与管理合作。",
          ["src-un-charter", "src-icj", "src-zgbk"], related=["intl-international-watercourses", "intl-treaty", "env-water-pollution"],
          pending="各国际河流航行条约的具体安排需按相关条约与国际组织资料核对。", needs_verification=True),
    ],
}