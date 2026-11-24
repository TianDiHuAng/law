# BACKLOG — 待办队列

> 最后更新：2026-11-24 · 轮次 R83
> 状态：**已饱和（SATURATED=true）**，维护模式。

## R83 本轮已完成（维护）

| id | 内容 |
|---|---|
| R83-01 | 合同解除（civil-contract-termination）升级 L3 |
| R83-02 | 格式条款（civil-standard-terms）升级 L3 |
| R83-03 | 缺口复检：无新增权威覆盖缺口，维持饱和（连续 7 轮） |

## R84 待办（维护模式）

| id | 内容 |
|---|---|
| R84-01 | 升级 2 条 L3（正当防卫之外的刑法概念，如犯罪未遂/共同犯罪；或 U02 行政法核心概念如行政行为的效力） |
| R84-02 | 缺口复检并维持饱和 |

## R85–R86 待办（维护模式）

- 每轮 2 条 L3 深度化。

## R87 体检轮

- 常规体检 + 饱和状态维护检查。

## 当前统计

- 条目 379（L1 0 / L2 362 / L3 17）；来源 144，已核验 122；`CHECK_OK`。

## L3 已覆盖条目（17 条）

fa-concept、crim-defense、data-personal、law-civil-code、law-admin-litigation、law-criminal、law-civil-procedure、law-company、law-personal-info、law-constitution、law-labor-contract、law-environment、law-copyright、law-administrative-penalty、civil-contract、civil-contract-termination、civil-standard-terms。

## 维护原则

- 一旦发现新的权威覆盖缺口，立即退出饱和回到正常循环；不写 `ALL_DONE`。

## 约束

- 单轮新增 scope 条目不超过现有总条目数的 10%（379 条 → 每轮最多 37 条）。
- 每条新增必须有两个独立、已核验来源；不足则不得进入正文。