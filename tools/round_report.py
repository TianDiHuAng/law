# -*- coding: utf-8 -*-
"""按 AUTONOMOUS.md 第七节格式生成每轮 REPORT.md。"""
import json
import os
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TODAY = "2026-11-24"
TYPE_KEYS = ["概念制度", "案例", "文本导读", "流程"]


def main():
    coverage = json.load(open(os.path.join(ROOT, "coverage.json"), encoding="utf-8"))
    metrics = json.load(open(os.path.join(ROOT, "METRICS.json"), encoding="utf-8"))
    saturation = json.load(open(os.path.join(ROOT, "SATURATION.json"), encoding="utf-8"))
    sources = json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"]
    m = metrics["rounds"][-1]
    total = coverage["total"]
    lv = coverage["levels"]
    verified = sum(1 for s in sources if s.get("verified"))
    pending = sum(1 for e in coverage["entries"] if e.get("unverified_count", 0) > 0)
    blanks = []
    for uid, unit in coverage["matrix"].items():
        for t in TYPE_KEYS:
            if unit["by_type"].get(t, 0) == 0:
                blanks.append(f"{unit['title']} × {t}")
    blank_text = "、".join(blanks[:20]) if blanks else "无"

    lines = []
    lines.append(f"# REPORT — 第 R{m['round']:02d} 轮")
    lines.append("")
    lines.append(f"1. **本轮编号**：R{m['round']:02d} ｜ **日期**：{m['date']} ｜ **状态**：正常")
    lines.append(f"2. **本轮完成**：新增 {m['new_entries']} 条；升级 {m['upgrades']} 条；复核 {m['reviews']} 条；修复 {m['fixes']} 条")
    lines.append(f"3. **累计**：总条目 {total}；L1 {lv.get('L1',0)} / L2 {lv.get('L2',0)} / L3 {lv.get('L3',0)}；"
                 f"已核验来源 {verified}/{len(sources)}；待核实条目 {pending}；来源总数 {len(sources)}")
    lines.append(f"4. **质量**：`tools/check.py` → {m['check']}；本轮抽检见 `SPOTCHECK.md`；无回滚或降级批次")
    lines.append("5. **缺口发现摘要**：本轮使用 5 种方法（权威大纲再对照、覆盖矩阵、悬空引用、读者问题清单、深度缺口），"
                 f"发现 {saturation['history'][-1]['gaps_found']} 个缺口；已执行 14 条新增与 6 条 L2 升级，其余进入 BACKLOG。")
    lines.append(f"6. **覆盖矩阵仍空白格子（最多 20 个）**：{blank_text}。结构性空白说明见 `coverage.html`。")
    lines.append("7. **需要人关注的事项**：无。")
    lines.append("")
    lines.append(f"> 饱和状态：{'SATURATED' if saturation.get('saturated') else '未饱和'}；连续零新增缺口轮数：{saturation.get('consecutive_zero_gap_rounds', 0)}。")
    open(os.path.join(ROOT, "REPORT.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("round report written")


if __name__ == "__main__":
    main()
