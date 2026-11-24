# -*- coding: utf-8 -*-
"""R141 收尾：向 METRICS.json / SATURATION.json 追加本轮记录。"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATE = "2026-11-24"
LEVELS = {"L1": 0, "L2": 246, "L3": 133}

metrics_path = os.path.join(ROOT, "METRICS.json")
metrics = json.load(open(metrics_path, encoding="utf-8"))
if metrics["rounds"][-1]["round"] < 141:
    metrics["rounds"].append({
        "round": 141,
        "date": DATE,
        "new_entries": 0,
        "upgrades": 0,
        "reviews": 0,
        "fixes": 0,
        "pending_total": 184,
        "check": "CHECK_OK (errors=0 warnings=0)",
        "new_sources": 0,
        "total_entries": 379,
        "levels": dict(LEVELS),
        "notes": "R141 维护模式：民族区域自治与突发公共卫生事件应急升 L3；L3 增至 133 条；缺口复检无新增，维持饱和。",
    })
    json.dump(metrics, open(metrics_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("METRICS appended 141")
else:
    print("METRICS already has 141")

sat_path = os.path.join(ROOT, "SATURATION.json")
sat = json.load(open(sat_path, encoding="utf-8"))
if sat["history"][-1]["round"] < 141:
    sat["history"].append({
        "round": 141,
        "date": DATE,
        "methods": ["维护：民族区域自治、突发公共卫生事件应急升 L3"],
        "gaps_found": 0,
        "new_entries": 0,
        "upgrades": 0,
        "l3_upgrades": 2,
        "saturated": True,
        "no_gap_streak": 65,
        "note": "维护保持，连续 65 轮零缺口。",
    })
    sat["consecutive_zero_gap_rounds"] = 65
    sat["totals"] = {"entries": 379, "levels": dict(LEVELS), "sources": 144, "verified": 122}
    json.dump(sat, open(sat_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("SATURATION appended 141")
else:
    print("SATURATION already has 141")
