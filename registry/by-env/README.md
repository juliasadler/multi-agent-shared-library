# 环境分片区（registry/by-env/）

每个环境两个分片，**只写自己的**：

- `<env-id>-goals.md`：本环境的目标清单（标题、状态、说明、时间线）。
- `<env-id>-tracking.md`：本环境的追踪事项（待办、提醒、进行中的任务）。

## 规则

- 总表（goals-master.md / tracking-master.md）由维护方聚合生成，**禁止手改**。
- 分片 frontmatter 带 source_env（自己的 env-id）、version、updated_at。
- 更新分片 = version+1；推送后回读验证。

## 分片模板（frontmatter）

```yaml
---
title: <env-id> 目标分片
id: WL-xxxx
type: registry
source_env: <你的env-id>
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
timezone: Asia/Shanghai
version: 1
tags: [registry, goals]
status: active
visibility: private
---
```
