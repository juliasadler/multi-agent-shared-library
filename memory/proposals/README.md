# 提案区（memory/proposals/）

环境 → 维护方的**上行提案通道**（与 `inbox/` 下行通告配对）。

## 规则

- 非维护方环境对 memory/ 正本只有读权限和提案权：发现记忆需要新增/修正时，在此新建提案文档，**绝不直接改正本**。
- 文件命名：`提案-<你的env>-<YYYYMMDD>-<序号>.md`（只新建、从不改别人的提案）。
- 提案写清：针对哪个文件、新增/修正的事实与出处、建议回写到哪一节。
- 维护方定期审阅，确认后以增量补丁方式并入正本；提案文件保留归档，不删除。

## 提案模板（frontmatter）

```yaml
---
title: 提案-<env>-<YYYYMMDD>-<序号>
type: proposal
source_env: <你的env-id>
target: <目标文件路径>
status: pending   # pending / accepted / rejected
created_at: YYYY-MM-DD
---
```
