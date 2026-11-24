# -*- coding: utf-8 -*-
"""条目构造函数：统一字段，减少各单元文件的重复。"""


def E(id, title, type, importance, jurisdiction, era, definition, summary, sources,
      related=None, l2=None, case=None, law=None, flow=None, pending="",
      needs_verification=False, l3=None, year=None):
    return {
        "id": id,
        "title": title,
        "type": type,                 # concept | case | law | flow
        "importance": importance,     # 核心 | 重要 | 补充
        "jurisdiction": jurisdiction,
        "era": era,
        "definition": definition,
        "summary": summary,
        "related": related or [],
        "sources": sources,
        "needs_verification": needs_verification,
        "pending_notes": pending,
        "l2": l2,
        "l3": l3,
        "case": case,
        "law": law,
        "flow": flow,
        "year": year,
    }


def UNIT(uid, title, subtitle, order, entries):
    return {"unit_id": uid, "title": title, "subtitle": subtitle, "order": order, "entries": entries}
