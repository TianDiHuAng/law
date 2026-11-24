# -*- coding: utf-8 -*-
"""R08 新增条目。"""
from common import E

EXTRAS_R08 = {
    "u03": [
        E("civil-personality-injunction", "人格权侵害禁令", "concept", "重要", "中国", "民法·人格权保护",
          "人格权侵害禁令是民事主体有证据证明行为人正在实施或者即将实施侵害其人格权的违法行为，不及时制止将使其合法权益受到难以弥补的损害时，依法请求人民法院责令行为人停止有关行为的措施。",
          "人格权侵害禁令是民法典人格权编的重要救济方式，适用于名誉、隐私、个人信息等人格权益受侵害或有受侵害之虞的情形。",
          ["src-law-civil-code", "src-zgbk", "src-wiki-civil-code"],
          related=["civil-personality", "civil-privacy", "civil-tort"],
          pending="人格权侵害禁令的司法解释与典型案例需按最高人民法院现行文本核对。", needs_verification=True),
        E("civil-construction-contract", "建设工程合同", "concept", "重要", "中国", "民法·典型合同",
          "建设工程合同是承包人进行工程建设，发包人支付价款的合同，包括工程勘察、设计、施工合同。",
          "建设工程合同应当采用书面形式；承包人应具备相应资质，违法转包、分包可能影响合同效力并产生行政责任。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-contract", "civil-contract-liability", "civil-property"]),
    ],
    "u06": [
        E("com-bill-defense", "票据抗辩与追索", "concept", "重要", "中国", "商法·票据法",
          "票据抗辩是票据债务人根据法定事由对票据债权人拒绝履行义务的行为；票据追索权是持票人在票据到期不获付款或期前不获承兑等法定情形下，向背书人、出票人等前手请求偿还票据金额及费用的权利。",
          "票据抗辩分为对物抗辩与对人抗辩；票据追索须在法定期间内作成拒绝证明并向前手发出追索通知，否则可能丧失对前手的追索权。",
          ["src-npc", "src-zgbk", "src-wiki-bill-law"], related=["com-bill", "com-securities", "civil-contract"]),
        E("com-bankruptcy-avoidance", "破产撤销权", "concept", "重要", "中国", "商法·破产法",
          "破产撤销权是管理人对债务人在人民法院受理破产申请前法定期间内实施的、损害债权人利益的行为，请求人民法院予以撤销的权利。",
          "可撤销行为包括无偿转让财产、以明显不合理价格交易、对个别债权人清偿、放弃债权等；撤销后取得的财产归入债务人财产。",
          ["src-law-bankruptcy", "src-zgbk"], related=["com-bankruptcy", "com-restructuring", "civil-security"]),
    ],
    "u08": [
        E("intl-sea-dispute", "国际海洋争端解决", "concept", "补充", "国际", "国际公法·海洋法",
          "国际海洋争端解决是依据《联合国海洋法公约》第十五部分等机制，通过谈判、调解、仲裁、国际法院或国际海洋法法庭解决海洋权益争端的制度。",
          "公约设置强制争端解决程序，但允许缔约国对特定争端作出保留或选择例外；中国已依法作出相关声明，具体范围以官方文本为准。",
          ["src-un-charter", "src-icj", "src-zgbk"], related=["intl-law-of-sea", "intl-sources", "intl-treaty"],
          pending="《联合国海洋法公约》争端解决条款与中国相关声明需按联合国及外交部官方文本核对。", needs_verification=True),
    ],
}
