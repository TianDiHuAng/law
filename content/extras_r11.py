# -*- coding: utf-8 -*-
"""R11 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R11 = {
    "u02": [
        E("admin-administrative-adjudication", "行政裁决", "concept", "补充", "中国", "行政法学·行政司法",
          "行政裁决是行政机关依法对平等主体之间发生的、与行政管理活动密切相关的民事纠纷进行审查并作出裁决的行为。",
          "行政裁决范围包括土地、林木、林地权属争议、知识产权侵权赔偿争议等；当事人不服行政裁决可依法申请复议或提起行政诉讼。",
          ["src-law-admin-litigation", "src-zgbk"], related=["admin-act", "admin-litigation", "proc-admin-litigation"],
          pending="行政裁决的具体范围与程序需按各专门法律、法规核对。", needs_verification=True),
    ],
    "u03": [
        E("civil-legacy-support", "遗赠扶养协议", "concept", "重要", "中国", "民法·继承",
          "遗赠扶养协议是自然人与继承人以外的组织或者个人签订的，由该组织或者个人承担该自然人生养死葬的义务，享有受遗赠权利的协议。",
          "遗赠扶养协议优先于遗嘱继承和法定继承；扶养人无正当理由不履行扶养义务的，可能丧失受遗赠权。",
          ["src-law-civil-code", "src-jd-civil-inheritance", "src-zgbk"], related=["civil-inheritance", "civil-testate", "civil-marriage"]),
    ],
    "u07": [
        E("data-classification", "数据分类分级", "concept", "重要", "中国", "数据法·数据安全",
          "数据分类分级是国家根据数据在经济社会发展中的重要程度，以及一旦遭到篡改、破坏、泄露或者非法获取、非法利用，对国家安全、公共利益或者个人、组织合法权益造成的危害程度，对数据实行分类分级保护的制度。",
          "数据分类分级是数据安全治理的基础；重要数据目录、核心数据认定与分级保护要求以国家网信部门及行业主管部门规定为准。",
          ["src-law-data-security", "src-zgbk"], related=["data-security", "data-personal", "data-cross-border"],
          pending="重要数据目录与行业分级规则需按国家网信部门及行业主管部门官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-human-rights-treaties", "国际人权公约体系", "concept", "重要", "国际", "国际公法·人权法",
          "国际人权公约体系以《世界人权宣言》为基础，包括《公民权利和政治权利国际公约》《经济、社会及文化权利国际公约》及禁止酷刑、消除种族歧视、儿童权利、妇女权利等专门公约。",
          "国际人权公约通过缔约国报告、个人来文、调查与友好解决等机制实施；各公约的批准状态与保留以联合国条约集为准。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["intl-human-rights", "intl-sources", "const-rights"],
          pending="各人权公约的批准、保留与任择议定书状态需按联合国条约集核对。", needs_verification=True),
    ],
    "u10": [
        E("law-environment", "《中华人民共和国环境保护法》导读", "law", "重要", "中国", "2014年修订，2015年1月1日施行",
          "《中华人民共和国环境保护法》是环境保护领域的基础性法律，2014年修订后共七章，规定监督管理、保护和改善环境、防治污染和其他公害、信息公开与公众参与、法律责任。",
          "该法确立保护优先、预防为主、综合治理、公众参与、损害担责原则，被称为“史上最严环保法”；具体条文以2015年1月1日施行的文本为准。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-pollution", "env-eia"],
          law=dict(status="现行有效", version="2014年修订", effective_date="2015-01-01", checked_date="2026-11-24",
                   background="环境保护法1989年制定，2014年修订适应生态文明建设与环境污染治理需要，强化政府责任、企业义务与公众参与。",
                   structure=[dict(name="第一章 总则", content="立法目的、保护优先、预防为主、公众参与、损害担责"),
                              dict(name="第二章 监督管理", content="环境规划、标准、监测、环评、排污许可"),
                              dict(name="第三章 保护和改善环境", content="生态保护、生态补偿、环境质量"),
                              dict(name="第四章 防治污染和其他公害", content="污染防治、清洁生产、农业与农村环境保护"),
                              dict(name="第五章 信息公开和公众参与", content="环境信息公开、公众参与、公益诉讼"),
                              dict(name="第六章 法律责任", content="按日连续处罚、查封扣押、限产停产、行政拘留"),
                              dict(name="第七章 附则", content="施行日期")],
                   key_articles=[dict(article="第六条", content="一切单位和个人都有保护环境的义务。地方各级人民政府应当对本行政区域的环境质量负责。"),
                                 dict(article="第四十一条", content="建设项目中防治污染的设施，应当与主体工程同时设计、同时施工、同时投产使用。防治污染的设施应当符合经批准的环境影响评价文件的要求，不得擅自拆除或者闲置。"),
                                 dict(article="第四十二条", content="排放污染物的企业事业单位和其他生产经营者，应当采取措施，防治在生产建设或者其他活动中产生的废气、废水、废渣、医疗废物、粉尘、恶臭气体、放射性物质以及噪声、振动、光辐射、电磁辐射等对环境的污染和危害。")],
                   amendments=["1989年制定", "2014年修订：按日连续处罚、公众参与、公益诉讼"],
                   interpretations=["环境保护法配套办法与生态环境损害赔偿制度改革文件，具体以官方现行文本为准。"]),
          pending="2014年修订后条文序号与配套办法需按官方文本核对。", needs_verification=False),
    ],
}
