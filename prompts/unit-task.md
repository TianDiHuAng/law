# 单元写作任务书（供后续代理或人工参考）

## 目标
按 `data/units/` 的 schema 为一个单元新增或升级条目，完成后必须通过 `python tools/check.py`。

## 必读
1. `scope.md`：本单元条目与层级。
2. `sources.json`：只能引用 `verified=true` 的来源；来源 id 不得拼写错误。
3. `DECISIONS.md`：写作边界与口径。
4. `tools/check.py`：字段、日期、来源、SVG 规则以校验器为准。

## 写作层级
- L1：`definition`、`era`、`summary`、`related`、`sources`，并保证有页面模板可渲染。
- L2：在 `l2` 中补齐 `definition_source / elements / conditions / effects / exceptions / cases / controversies / distinctions / misconceptions`。
- L3：在 `l3` 中增加 `title / paragraphs / data`，只用于少量核心条目。

## 硬性规则
- 不编造数字、日期、人名、引文、案号、条文号；查不到就写“待核实”，并在 `pending_notes` 说明。
- 关键事实至少两个独立来源；少于两个来源时必须 `needs_verification=true` 且 `pending_notes` 非空。
- 引用法律条文写明法律名称、版本、核对日期；外国法条文注明“自行翻译，仅供参考”。
- 争议观点列出各方理由，不替读者下结论；不用“显然”“必然”“一定”等绝对化措辞。
- 不使用图片；图示在 `gen_site.py` 中由条目字段生成内联 SVG。
- 页脚声明由生成器统一注入，不在条目里重复。

## 常见错误
| 错误 | 修复 |
|---|---|
| 引用未核验来源 | 改用 sources.json 中 verified=true 的 id |
| 案例案号无来源记录 | 保留“待核实”，或补充已核验判例来源 |
| 年份/日期格式不合法 | 用 `YYYY-MM-DD`，不确定写“待核实” |
| L2 缺字段 | 补齐 `l2` 的 7 个列表字段 |
| 条目 id 含大写/中文/空格 | 只允许 `a-z 0-9 -` |
| 图示文字出界 | 缩短条目文字或改用生成器的自动换行 |

## 完成流程
```bash
python tools/build_data.py     # 重建 data/units 与 coverage
python tools/check.py          # 必须 0 errors
python tools/gen_site.py       # 生成 site/
python tools/report.py         # 更新 REPORT.md / COVERAGE.md
```
