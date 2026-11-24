# 法律知识库：体系、制度与经典案例

一个可离线打开的中文法律知识静态站点。覆盖法理与法律史、宪法与行政法、民法、刑法与刑事程序、民事与行政程序、商法与社会法、知识产权环境与数据法、比较法与国际法、经典案例、法律文本导读和程序流程。

## 快速开始

```bash
# 1. 重建数据（content/*.py -> data/units/*.json + coverage.json + scope.md）
python tools/build_data.py

# 2. 全量校验（字段、来源、日期、链接、SVG、页脚声明、禁用措辞）
python tools/check.py

# 3. 生成静态站点（site/）
python tools/gen_site.py

# 4. 生成报告
python tools/report.py
```

打开 `site/index.html` 或根目录 `index.html`（自动跳转）。

## 目录结构

```
content/            条目源数据（按单元分文件，便于编辑）
data/units/         生成后的 JSON 数据层
sources.json        来源库（含 verified / checked_date / 链接状态）
scope.md            范围清单（四份权威大纲/目录取并集）
coverage.json       覆盖矩阵与逐条状态
site/               生成的静态站点（纯 HTML+CSS，零 JS）
tools/              build_data / check / gen_site / report
PROGRESS.md         跨轮次续作锚点
REPORT.md           最终报告
```

## 内容边界

本站内容仅供学习参考，不构成法律意见；法律会修订，具体问题请咨询执业律师或查阅官方现行文本。

- 只讲制度、规则、理由与争议，不针对具体个案下结论。
- 无法核实的案号、日期、条文号统一标注“待核实”，不凭记忆补全。
- 所有图示为自制内联 SVG，不使用任何图片文件。
