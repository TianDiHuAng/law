# -*- coding: utf-8 -*-
"""R23 新增条目。"""
from common import E


def D(w, d):
    return {"with": w, "difference": d}


EXTRAS_R23 = {
    "u06": [
        E("com-investor-protection", "投资者保护", "concept", "重要", "中国", "商法·证券法",
          "投资者保护是证券法为保护投资者合法权益而建立的适当性管理、信息披露、先行赔付、代表人诉讼与投资者保护机构等制度。",
          "证券法设专章规定投资者保护，区分普通投资者与专业投资者，强化证券公司适当性义务与上市公司现金分红、债券持有人保护。",
          ["src-law-securities", "src-zgbk"], related=["com-securities", "com-disclosure", "com-insider"]),
    ],
    "u07": [
        E("env-hazardous-waste", "危险废物管理", "concept", "补充", "中国", "环境法·固体废物",
          "危险废物管理是对列入国家危险废物名录或者根据危险废物鉴别标准认定的具有危险特性的固体废物，实行严格监管的制度。",
          "危险废物经营实行许可证制度，转移危险废物应填写转移联单；产生、收集、贮存、运输、利用、处置危险废物的单位应制定意外事故防范措施和应急预案。",
          ["src-law-environment", "src-zgbk"], related=["env-solid-waste", "env-pollution", "env-law"],
          pending="国家危险废物名录与危险废物经营许可办法需按生态环境部现行文本核对。", needs_verification=True),
        E("data-platform-economy", "平台经济治理", "concept", "补充", "中国", "数据法·平台治理",
          "平台经济治理是规范互联网平台经营者竞争行为、数据利用、消费者权益与平台责任的制度体系，涉及反垄断、反不正当竞争、电子商务、数据安全与算法治理。",
          "平台经营者不得利用数据、算法、技术、资本优势等从事垄断或不正当竞争行为，应履行平台内经营者管理、消费者权益保护与数据安全义务。",
          ["src-law-anti-unfair", "src-law-data-security", "src-zgbk"], related=["ip-anti-unfair", "data-algorithm", "data-cybercrime"],
          pending="平台经济反垄断指南与电子商务法配套规则需按市场监管总局官方文本核对。", needs_verification=True),
    ],
    "u08": [
        E("intl-state-responsibility", "国家责任", "concept", "补充", "国际", "国际公法·国家责任",
          "国家责任是国家因违反国际义务而应承担的国际法责任，包括停止不法行为、保证不重犯、赔偿、抵偿等后果。",
          "国家责任制度由《国家对国际不法行为的责任条款草案》等国际法文件体现，区分一般责任与严重违反强行法的责任。",
          ["src-un-charter", "src-icj", "src-zgbk"], related=["intl-sources", "intl-sovereignty", "intl-treaty"],
          pending="国家责任条款草案的条文与各国实践需按联合国国际法委员会资料核对。", needs_verification=True),
    ],
}
