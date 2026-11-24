# -*- coding: utf-8 -*-
"""R10 案例案号复核记录：列出待核实案例，记录复核结论（无公开可访问文书时保留待核实）。"""
import glob
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def main():
    metrics = json.load(open(os.path.join(ROOT, "METRICS.json"), encoding="utf-8"))
    rnd = metrics["rounds"][-1]["round"] + 1
    out_name = f"CASE_REVIEW_R{rnd:02d}.md"
    units = []
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "units", "*.json"))):
        units.append(json.load(open(p, encoding="utf-8")))
    cases = [e for u in units for e in u["entries"] if e["type"] == "case"]
    pending = [e for e in cases if (e.get("case") or {}).get("case_no") in ("待核实", "待核实（再审案号）", "") or "待核实" in (e.get("case") or {}).get("case_no", "")]
    lines = [f"# CASE_REVIEW — R{rnd:02d} 案例案号复核\n", f"> 日期：2026-11-24；案例条目 {len(cases)} 条，列入复核 {len(pending[:10])} 条。\n",
             "| 条目 | 法院 | 案号状态 | 复核结论 |", "|---|---|---|---|"]
    for e in pending[:10]:
        c = e.get("case") or {}
        lines.append(f"| {e['id']} | {c.get('court','')} | {c.get('case_no','')} | 公开检索受限，保留“待核实”；不得凭记忆补全 |")
    lines.append("")
    lines.append("说明：本轮仅做记录与合规复核；案号、裁判日期需在最高人民法院公报、中国裁判文书网或官方发布中实际打开后回填。")
    open(os.path.join(ROOT, out_name), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("case review written", len(pending[:10]))


if __name__ == "__main__":
    main()
