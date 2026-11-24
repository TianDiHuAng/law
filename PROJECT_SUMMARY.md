# PROJECT_SUMMARY — 项目总结

> 生成日期：2026-11-24。数字均来自当轮 `tools/check.py` 实测输出与仓库文件，不是估计值。

## 一、项目是什么

**《法律知识库：体系、制度与经典案例》**——一个可离线打开、可公开访问的中文法律知识静态站点：

- **在线地址**：https://tiandihuang.github.io/law/ （GitHub Pages，已部署并实测 HTTP 200）
- **仓库**：git@github.com:TianDiHuAng/law.git（main 分支，本地与远程同步）
- **本地入口**：根目录 `index.html`（跳转）或直接打开 `site/index.html`

## 二、最终规模（实测）

| 指标 | 数值 |
|---|---|
| 条目总数 | 379（11 个单元） |
| 层级分布 | L1 0 / L2 244 / L3 135 —— L1 已清零 |
| 页面类型 | 概念制度 338 / 案例 20 / 文本导读 15 / 流程 6 |
| 来源库 | 146 条，其中已核验 124 条 |
| 待核实条目 | 186 条（全部附具体说明，如引文页码、新法施行） |
| 站点页面 | 400 个 HTML + style.css，纯 HTML/CSS，零 JS |
| 校验结果 | `python tools/check.py` → CHECK_OK（errors=0 warnings=0） |
| 核心覆盖 | 10/10 个含核心条目的单元全部达到 L2 及以上 |
| 执行轮次 | R01–R142（含 5 次全面体检轮） |

各单元条目数：u01 法理与法律史 20、u02 宪法与行政法 53、u03 民法 70、u04 刑法与刑事程序 26、u05 民事与行政程序 12、u06 商法与社会法 26、u07 知识产权环境与数据法 70、u08 比较法与国际法 61、u09 经典案例 20、u10 法律文本导读 15、u11 程序流程 6。

## 三、做了什么（时间线摘要）

1. **阶段 0–5 建库**：对照四份权威大纲（教学质量国家标准、法考大纲、中国大百科·法学、国家法律法规数据库分类）取并集，生成 scope.md（379 条）与 coverage.json；建立 sources.json；实现 check.py 全量校验器；以 2 个 L2 样板条目起步；全量写作至 L1 清零、核心条目全部 L2+；生成总览、索引、时间线、导航与报告。
2. **R06 起自主扩充**：按轮推进新增条目与 L2/L3 升级，每轮配额 40 条以内，每轮更新 coverage.json / METRICS.json / PROGRESS.md。
3. **R76 里程碑**：L1 清零。
4. **R79 达成饱和**：连续 3 轮零新增覆盖缺口后进入「饱和/维护模式」——不再扩 scope，每轮做 2 条 L3 深度化与定期体检。
5. **R77–R142 维护期**：每 5 轮一次全面体检（死链、过期、重复、矛盾、孤儿页、来源重合度），体检轮另做 41 条抽查复核；期间 R140/R141/R142 各完成 2 条 L3 升级。
6. **R142 体检轮（本收尾轮）**：
   - `com-company`（公司法）、`com-bill`（票据）升 L3；
   - 依据法释〔2026〕15号（生态环境法典 2026-08-15 施行，已在最高法官网实际打开核对），将 6 个环境法条目标记待复核；
   - 新增 2 个已核验的最高法官网来源；
   - README 扩写；首页与覆盖页新增纯 SVG 条形图与环形图；
   - 部署 GitHub Pages 并实测可访问；补入在线地址。
7. **全部改动均已提交并推送**：最终提交 `5639ec9`，工作区干净。

## 四、质量机制（仍在生效）

- **机器校验**：check.py 覆盖必填字段、日期/数字合法性、来源 verified、双源规则、重复、内部链接 404、SVG 边界、跨页一致性、辖区标注、条文版本与核对日期、案号来源、页脚声明、禁用措辞。
- **诚实标注**：查不到的一律写「待核实」，不凭记忆补全；五类信息（法条/司法解释/指导性案例/学说/实务）分层标注。
- **体检与抽检**：每轮抽检 10%，每 5 轮全面体检；报告落在 HEALTH_R*.md、CASE_REVIEW_R*.md、SPOTCHECK.md。

## 五、遗留事项（接手人须知）

1. **6 个环境法条目待改写**：`env-law`、`env-air-pollution`、`env-water-pollution`、`env-soil-pollution`、`env-solid-waste`、`law-environment`。生态环境法典已施行，正文仍基于旧环境保护法体系，需对照法典官方文本逐条核对改写。当前只加了待复核标记。
2. **186 条 needs_verification**：全部附有具体说明。清零需人工查原始文献（引文页码、案号、条文号、外文资料），不是继续生成内容能解决的。
3. **外文官网反爬**：BAILII、Justia、Legifrance 等部分页面 403/SSL 失败，已用可访问替代源并在 sources.json 保留原链接（verified=false），见 BLOCKERS.md。
4. **控制台乱码**：Windows 下运行脚本请先 `PYTHONIOENCODING=utf-8`，数据文件本身为 UTF-8 无损坏。
5. **README 换行符**：`5639ec9` 一次提交显示整文件重写，是 CRLF→LF 变化，内容未变；如介意可统一 .gitattributes。

## 六、快速上手命令

```bash
PYTHONIOENCODING=utf-8 python tools/build_data.py   # 重建数据层
PYTHONIOENCODING=utf-8 python tools/check.py        # 全量校验（必须 CHECK_OK）
PYTHONIOENCODING=utf-8 python tools/gen_site.py     # 重新生成站点
PYTHONIOENCODING=utf-8 python tools/report.py       # 重新生成报告
```

改动流程：改 `content/*.py` → build → check → gen_site → git commit → git push。Pages 自动重新部署。
