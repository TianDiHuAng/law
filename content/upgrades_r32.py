# -*- coding: utf-8 -*-
"""R32 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R32 = {
    "fa-validity": dict(
        definition_source="法理学通说；《中华人民共和国立法法》关于法律效力与适用规则的规定（版本：2023年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["对人效力", "时间效力", "空间效力", "事项效力"],
        conditions=["法律依法制定并公布", "在生效期间内", "在法定管辖范围内"],
        effects=["法律对主体产生约束力", "新法原则上不溯及既往（有利溯及除外）", "特别法优于一般法、上位法优于下位法"],
        exceptions=["从旧兼从轻原则", "法的溯及力例外规定", "自治条例、经济特区法规的变通规定"],
        cases=[],
        controversies=[dict(issue="法律效力与法律实效的关系",
                            views=[dict(holder="分离说（通说）", basis="效力是规范上的约束力，实效是事实上的被遵守程度，二者可分离"),
                                   dict(holder="结合说（部分学者）", basis="长期无实效的规范其效力基础值得反思")])],
        distinctions=[D("法律效力", "规范的约束力"), D("法律实效", "规范在现实中被遵守的程度")],
        misconceptions=[dict(claim="法律公布即生效", correction="部分法律公布后另定施行日期"),
                        dict(claim="新法一律溯及既往", correction="原则上不溯及既往，从旧兼从轻是刑法等的例外规则")],
    ),
    "fa-relationship": dict(
        definition_source="法理学通说；《中华人民共和国民法典》关于民事法律关系的规定（核对日期：2026-11-24）。",
        elements=["法律关系主体", "法律关系客体", "法律关系内容（权利义务）", "法律事实"],
        conditions=["存在相应的法律规范", "出现法律事实", "主体具有相应资格"],
        effects=["主体之间形成权利义务关系", "权利受侵害可请求法律保护", "法律关系可因法律事实而变更或消灭"],
        exceptions=["事实关系的法律保护有限", "某些关系不受法律调整（如纯粹情谊行为）"],
        cases=[],
        controversies=[dict(issue="法律关系的本质",
                            views=[dict(holder="意志关系说（传统）", basis="法律关系是体现国家意志与当事人意志的思想社会关系"),
                                   dict(holder="规范关系说（部分学者）", basis="法律关系是法律规范对生活关系的规范化重构")])],
        distinctions=[D("法律关系", "经法律规范调整的社会关系"), D("事实关系", "未经法律调整的社会关系")],
        misconceptions=[dict(claim="所有社会关系都是法律关系", correction="只有受法律规范调整的才是法律关系"),
                        dict(claim="法律关系一旦形成不可变更", correction="法律事实可引起法律关系的变更与消灭")],
    ),
    "fa-system": dict(
        definition_source="法理学通说及国家法律法规数据库的法律部门分类（核对日期：2026-11-24）。",
        elements=["宪法及宪法相关法", "民法商法", "行政法", "经济法", "社会法", "刑法", "诉讼与非诉讼程序法"],
        conditions=["以现行有效的法律规范为范围", "按调整对象与调整方法划分"],
        effects=["形成门类齐全的法律体系", "便于法律适用与法学研究", "部门法之间相互衔接"],
        exceptions=["部门法划分具有相对性", "新兴领域（数据、人工智能）可能跨越多个部门"],
        cases=[],
        controversies=[dict(issue="经济法是否独立部门法",
                            views=[dict(holder="独立部门说（通说）", basis="经济法有独特调整对象即国家干预经济关系"),
                                   dict(holder="综合说（部分学者）", basis="经济法可由行政法与商法共同涵盖")])],
        distinctions=[D("法律体系", "现行法的部门划分"), D("法学体系", "法学学科的分类")],
        misconceptions=[dict(claim="法律体系等于立法规划", correction="法律体系是现行规范的客观结构，不是计划清单"),
                        dict(claim="部门法划分绝对固定", correction="部门法划分随经济社会发展而调整")],
    ),
    "fa-interpretation": dict(
        definition_source="《中华人民共和国立法法》关于法律解释的规定及法理学通说（版本：2023年修正，核对日期：2026-11-24）。",
        elements=["文义解释", "体系解释", "目的解释", "历史解释", "解释主体"],
        conditions=["存在需要阐明含义的法律规定", "由法定主体或裁判者作出", "遵循解释规则与位阶"],
        effects=["明确规范含义", "指导法律适用", "统一裁判尺度"],
        exceptions=["立法解释权属于全国人大常委会", "司法解释不得与法律相抵触"],
        cases=[],
        controversies=[dict(issue="解释方法的优先顺序",
                            views=[dict(holder="文义优先说", basis="解释应从文义出发，文义清晰时不得背离"),
                                   dict(holder="目的优先说（部分学者）", basis="当文义导致明显不公时，应以规范目的为准")])],
        distinctions=[D("法律解释", "阐明规范含义"), D("法律推理", "由规范与事实推出结论")],
        misconceptions=[dict(claim="解释就是随意理解", correction="解释须遵循法定方法与位阶，受合法性约束"),
                        dict(claim="只有法官需要解释法律", correction="行政机关、律师与学者同样进行法律解释")],
    ),
}