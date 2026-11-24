# 法律知识库：体系、制度与经典案例

一个可离线打开的中文法律知识静态站点。覆盖法理与法律史、宪法与行政法、民法、刑法与刑事程序、民事与行政程序、商法与社会法、知识产权环境与数据法、比较法与国际法、经典案例、法律文本导读和程序流程。

**在线访问：** https://tiandihuang.github.io/law/

## 规模一览

| 项目 | 数量 |
| --- | --- |
| 条目总数 | 379 |
| 单元 | 11 |
| L2（标准）/ L3（深度研读） | 244 / 135 |
| 来源 | 146（其中 124 个已核验） |
| 站点页面 | 400（纯 HTML+CSS，零 JS） |

各单元条目数：

| 单元 | 条目 |
| --- | --- |
| u01 | 20 |
| u02 | 53 |
| u03 | 70 |
| u04 | 26 |
| u05 | 12 |
| u06 | 26 |
| u07 | 70 |
| u08 | 61 |
| u09 经典案例 | 20 |
| u10 法律文本导读 | 15 |
| u11 程序流程 | 6 |

> 数字随内容更新；以 `coverage.json` 和 `python tools/check.py` 的输出为准。各单元的具体名称见站点 `units.html`。

## 站点与可视化

打开 `site/index.html` 或根目录 `index.html`（自动跳转）即可离线浏览。

| 页面 | 说明 |
| --- | --- |
| `index.html` | 首页：统计、部门法地图、**规模一览图表**、核心条目 |
| `units.html` / `unit-*.html` | 11 个单元及各自条目列表 |
| `index-all.html` | 全部条目索引 |
| `cases.html` | 经典案例 |
| `laws.html` | 法律文本导读 |
| `flows.html` | 程序流程 |
| `timeline.html` | 时间线 |
| `coverage.html` | 覆盖矩阵与**深度分布图表** |
| `sources.html` | 来源库 |
| `about.html` | 方法与边界 |

可视化全部是自制内联 SVG，不依赖图片文件或脚本：

- **各单元条目数条形图**：按 L3 / L2 / L1 堆叠，见首页与覆盖页。
- **深度占比环形图**：L1 / L2 / L3 占比，见首页与覆盖页。
- **条目内图示**：概念结构图、分层图等，由 `check.py` 校验。

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

Windows 控制台输出中文时，请先设置 `PYTHONIOENCODING=utf-8`。

## 发布到 GitHub Pages

已部署在 https://tiandihuang.github.io/law/ 。站点是纯静态文件，可直接托管：在仓库 Settings → Pages 中选择 `main` 分支的根目录（根目录 `index.html` 会跳转到 `site/index.html`）。

## 目录结构

```
content/            条目源数据（按单元分文件，便于编辑）
data/units/         生成后的 JSON 数据层
sources.json        来源库（含 verified / checked_date / 链接状态）
scope.md            范围清单（四份权威大纲/目录取并集）
coverage.json       覆盖矩阵与逐条状态
site/               生成的静态站点（纯 HTML+CSS，零 JS）
tools/              build_data / check / gen_site / report 等脚本
PROGRESS.md         跨轮次续作锚点
REPORT.md           最终报告
```

## 内容边界

本站内容仅供学习参考，不构成法律意见；法律会修订，具体问题请咨询执业律师或查阅官方现行文本。

- 只讲制度、规则、理由与争议，不针对具体个案下结论。
- 无法核实的案号、日期、条文号统一标注“待核实”，不凭记忆补全。
- 所有图示为自制内联 SVG，不使用任何图片文件。
- 部分条目带 `needs_verification` 标记，表示需对照原始文献复核（如生态环境法典施行后的环境法条目）。
