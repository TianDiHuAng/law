# -*- coding: utf-8 -*-
"""R22 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R22 = {
    "u02": [
        E("admin-public-health-emergency", "突发公共卫生事件应急", "concept", "重要", "中国", "行政法学·应急管理",
          "突发公共卫生事件应急是政府为预防、控制和消除突发公共卫生事件危害，保障公众健康与生命安全而建立的监测预警、应急处置与恢复重建制度。",
          "应急管理遵循预防为主、常备不懈、统一领导、分级负责、依法规范、依靠科学、依靠群众的原则；必要时可依法采取隔离、封锁、征用等措施。",
          ["src-gov-cn", "src-zgbk"], related=["admin-act", "admin-coercion", "const-rights"],
          pending="突发事件应对法、突发公共卫生事件应急条例的具体条文与最新修订需按官方文本核对。", needs_verification=True),
    ],
    "u07": [
        E("env-nuclear-safety", "核安全", "concept", "补充", "中国", "环境法·核安全",
          "核安全是核设施、核材料与放射性废物管理中，为保护公众健康和环境，防止核事故与辐射危害而建立的许可、监督、应急与责任制度。",
          "核安全法确立核设施营运单位主体责任、核安全许可、核安全监督、核事故应急与信息公开等制度。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-pollution", "env-eia"],
          pending="核安全法及配套核安全规章需按国家核安全局官方文本核对。", needs_verification=True),
        E("data-cybercrime", "网络犯罪", "concept", "重要", "中国", "数据法·网络犯罪",
          "网络犯罪是利用计算机网络实施的犯罪，包括非法侵入计算机信息系统、破坏计算机信息系统、网络诈骗、侵犯公民个人信息、帮助信息网络犯罪活动等。",
          "中国刑法与网络安全法、数据安全法、个人信息保护法共同构成网络犯罪治理的法律框架；网络服务提供者负有安全管理义务。",
          ["src-law-network-security-2", "src-law-criminal", "src-zgbk"], related=["data-network", "crim-constitution", "data-personal"],
          pending="网络犯罪罪名与司法解释的最新变化需按刑法修正案及两高解释核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-humanitarian-law", "国际人道法", "concept", "补充", "国际", "国际公法·国际人道法",
          "国际人道法是武装冲突期间保护不参加或不再参加敌对行动的人员及限制作战手段和方法的国际法规则，核心渊源为1949年日内瓦四公约及其附加议定书。",
          "国际人道法确立区分原则、比例原则、军事必要原则与预防措施义务，禁止攻击平民、虐待战俘和使用某些武器。",
          ["src-un-charter", "src-icj", "src-zgbk"], related=["intl-human-rights", "intl-international-criminal", "intl-sources"],
          pending="日内瓦四公约及附加议定书的具体条文与批准情况需按红十字国际委员会官方资料核对。", needs_verification=True),
    ],
}
