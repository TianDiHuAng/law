# HANDOVER — 交接文档

> 交接日期：2026-11-24。面向接手本项目的人类或 AI 协作者。目标：10 分钟内能够安全地继续维护和扩充本项目。

## 1. 一句话交接

数据驱动的中文法律知识静态站（379 条、11 单元、146 来源），改 `content/` 里的 Python 数据文件，跑 build→check→gen_site 三个脚本，推送到 GitHub 即自动发布到 https://tiandihuang.github.io/law/ 。**任何改动必须通过 `tools/check.py`（CHECK_OK）才能提交。**

## 2. 仓库与入口

| 项 | 值 |
|---|---|
| 仓库 | git@github.com:TianDiHuAng/law.git，main 分支 |
| 最新提交 | `5639ec9`（README 补在线地址），工作区干净 |
| 在线站点 | https://tiandihuang.github.io/law/ （Pages，已实测） |
| 本地预览 | 打开 `site/index.html` 或根目录 `index.html` |
| 详细总结 | 见 [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) |

## 3. 目录地图（哪些能改、哪些别手改）

```
content/          ✍️ 条目源数据（Python），所有内容改动都在这里
  u01.py–u11.py     各单元基础条目
  extras_r*.py      各轮新增条目（历史轮次，别改旧文件）
  upgrades_r*.py    各轮 L2/L3 升级内容（同样只增不改）
  sources_data.py   来源库源数据
data/units/*.json ⚙️ 生成物（build_data.py 产出，别手改）
coverage.json     ⚙️ 生成物
scope.md          范围清单（379 条的权威清单；扩 scope 前先读）
sources.json      来源库（运行态；加来源用 tools/add_sources_*.py 模式）
site/             ⚙️ 生成物（gen_site.py 产出，别手改）
tools/            ✍️ 脚本（见第 5 节）
*.md              项目管理文件（PROGRESS / BACKLOG / HEALTH_* / CASE_REVIEW_* 等）
prompts/unit-task.md  单条目写作任务模板
```

**核心原则：源在 content/，其余都是产物。** 手改生成物会在下次 build 时被覆盖。

## 4. 常规工作流（每轮照抄）

1. 读 `PROGRESS.md` 的「下轮起点」，读 `BACKLOG.md` 的当轮待办。
2. 改/加 `content/` 中的条目（新条目必须 ≥2 个 verified 来源；查不到的写「待核实」）。
3. `PYTHONIOENCODING=utf-8 python tools/build_data.py`
4. `PYTHONIOENCODING=utf-8 python tools/check.py` → **必须 CHECK_OK**，有错先修。
5. `PYTHONIOENCODING=utf-8 python tools/gen_site.py`
6. 更新 `coverage.json` 统计（build 会自动做）、`PROGRESS.md` 轮次记录、`BACKLOG.md`。
7. `git add -A && git commit -m "R<编号>：<做了什么>" && git push origin main`

轮次编号规则：R+三位数，接在最后一轮之后（当前下一轮是 **R143，体检轮**）。体检轮跑 `tools/health_check.py`、`tools/case_review.py`、`tools/spotcheck_round.py`，产出 HEALTH_R*.md / CASE_REVIEW_R*.md / SPOTCHECK.md。

## 5. 工具速查（tools/）

| 脚本 | 作用 | 什么时候跑 |
|---|---|---|
| build_data.py | content/*.py → data/units/*.json + coverage.json | 内容改动后 |
| check.py | 全量机器校验（13+ 类规则） | 每次 build 后，**提交前必须** |
| gen_site.py | 生成 site/（400 页 + style.css + SVG 图表） | 每次 build 后 |
| report.py / round_report.py | 生成 REPORT_FULL.md / REPORT.md | 轮末 |
| health_check.py | 死链、过期、重复、孤儿页、近重复体检 | 体检轮（每 5 轮） |
| case_review.py | 案例案号复核清单 | 体检轮 |
| spotcheck_round.py | 本轮改动 10% 抽检 | 体检轮 |
| verify_sources.py | 来源核验辅助 | 加新来源时 |
| add_sources_r142.py | R142 加来源的样例（新来源照抄此模式） | 参考 |

## 6. 加新条目的硬规则

1. **先查 scope.md**：不新增超出范围边界的条目；每轮新增 ≤ 现有条目数的 10%（379 → ≤37）。
2. **两个独立 verified 来源**，缺一个就写「待核实」+ `needs_verification=True` + `pending_notes` 说明缺什么。
3. 条目必填字段：`id, title, type(concept/case/law/flow), importance(核心/重要/补充), jurisdiction, era, definition, summary, sources, related, status, legal_status, checked_date`。L2 还要 `l2` 完整结构（definition_source/elements/conditions/effects/exceptions/controversies/distinctions/misconceptions 等）。
4. **禁止**：编造案号/日期/条文号；把学说当法条；「建议您起诉」「可以规避」等措辞（check.py 会拦）；沿用已废止法律的旧条文号。
5. 法律文本类条目（type=law）另需 `law` 字典：status(现行有效/已修订/已废止/待复核)、version、effective_date、checked_date、background、structure、key_articles、amendments、interpretations。

## 7. 当前状态与最近改动背景

- **模式**：饱和/维护（连续 60+ 轮零新增缺口），不写 ALL_DONE，没有终态。
- **最近一轮 R142 做了什么、为什么**：公司法/票据升 L3；因**生态环境法典 2026-08-15 施行**（法释〔2026〕15号，已实测核对），把 6 个环境法条目标了待复核——这是接手后**第一优先级**：按法典官方文本改写这 6 条。
- **关键决策与理由**：全部在 `DECISIONS.md`（技术路线、配色、层级定义、来源口径等 9+ 条），读它避免重复踩坑。
- **阻塞与处置**：`BLOCKERS.md`（外文官网反爬的替代源方案）。

## 8. 已知坑（都是实际踩过的）

1. **Windows 控制台乱码**：不是数据坏了，是 GBK 输出。所有 python 命令前面加 `PYTHONIOENCODING=utf-8`。
2. **update_goal 等工具参数名**：参数是 `goal_id`/`action`/`revision`，写错会报 missing property——照报错补即可。
3. **check.py 的 R16 规则**：sources.html 和 index.html 里的来源计数是生成时写死的，改了 sources.json 后**必须重新 gen_site**，否则校验失败。
4. **新增 L3 升级轮**要同时改 4 处：content/upgrades_rXXX.py（数据）、tools/build_data.py（import + 应用块）、tools/spotcheck_round.py（import + ROUND_DATA）、然后 build→check→gen_site。漏一处会导致数据与站点不一致。
5. **content/ 历史文件只增不改**：spotcheck_round.py 按轮次 import 历史 upgrades 文件，改名/删除会直接炸校验链。
6. **CRLF/LF**：本仓库文件现在是 LF；如见整文件 diff，先查换行符再怀疑内容。

## 9. 验收清单（接手后第一次跑）

```bash
git pull                                          # 确认拿到 5639ec9
PYTHONIOENCODING=utf-8 python tools/check.py      # 应输出 CHECK_OK, errors=0 warnings=0
PYTHONIOENCODING=utf-8 python tools/build_data.py # 应输出 build ok: 379 entries
PYTHONIOENCODING=utf-8 python tools/gen_site.py   # 应输出 generated 400 pages
```

三条都通过 = 环境正常，可以开始 R143。打开 https://tiandihuang.github.io/law/ 确认线上与本地 `site/index.html` 一致。
