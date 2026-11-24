# -*- coding: utf-8 -*-
"""R13 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R13 = {
    "u03": [
        E("civil-name", "姓名权", "concept", "重要", "中国", "民法·人格权",
          "姓名权是自然人依法决定、使用、变更或者许可他人使用自己姓名的权利，禁止他人干涉、盗用、假冒。",
          "姓名权是人格权的重要组成部分；自然人选取姓氏应依法进行，具有正当理由的可选取其他姓氏。",
          ["src-law-civil-code", "src-zgbk"], related=["civil-personality", "civil-privacy", "ip-trademark"]),
    ],
    "u07": [
        E("data-sensitive-personal", "敏感个人信息", "concept", "重要", "中国", "数据法·个人信息保护",
          "敏感个人信息是一旦泄露或者非法使用，容易导致自然人的人格尊严受到侵害或者人身、财产安全受到危害的个人信息，包括生物识别、宗教信仰、特定身份、医疗健康、金融账户、行踪轨迹等信息，以及不满十四周岁未成年人的个人信息。",
          "处理敏感个人信息应具有特定目的和充分必要性，取得个人单独同意，并履行告知与保护义务；法律、行政法规另有规定的除外。",
          ["src-law-personal-info-2", "src-zgbk"], related=["data-personal", "data-automated-decision", "civil-privacy"],
          pending="敏感个人信息的具体范围与单独同意规则需按个人信息保护法及配套规定核对。", needs_verification=True),
        E("env-solid-waste", "固体废物污染环境防治", "concept", "补充", "中国", "环境法·固体废物",
          "固体废物污染环境防治是规范固体废物产生、收集、贮存、运输、利用、处置，防止其污染环境的制度，坚持减量化、资源化、无害化原则。",
          "固体废物包括工业固体废物、生活垃圾、建筑垃圾、农业固体废物、危险废物等；危险废物实行经营许可与转移联单制度。",
          ["src-law-environment", "src-zgbk"], related=["env-law", "env-pollution", "env-soil-pollution"],
          pending="固体废物污染环境防治法及危险废物名录需按生态环境部现行文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-icc", "国际刑事法院", "concept", "补充", "国际", "国际公法·国际刑法",
          "国际刑事法院是依《罗马规约》设立的常设国际刑事司法机构，对灭绝种族罪、危害人类罪、战争罪和侵略罪行使补充管辖权。",
          "国际刑事法院仅在缔约国或安理会提交情势、检察官自行调查且符合补充性原则时行使管辖权；非缔约国国民的管辖权须依规约规定。",
          ["src-un-treaty", "src-icj", "src-zgbk"], related=["intl-international-criminal", "intl-human-rights", "intl-sources"],
          pending="《罗马规约》缔约国范围、补充性原则与法院案例需按国际刑事法院官方资料核对。", needs_verification=True),
    ],
}
