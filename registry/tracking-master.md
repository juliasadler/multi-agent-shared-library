---
title: 追踪总表（聚合生成）
id: WL-0102
type: registry
source_env: template
source_agent: "{{ASSISTANT_NAME}}"
origin: 本模板框架
created_at: "{{DATE}}"
updated_at: "{{DATE}}"
timezone: Asia/Shanghai
version: 1
supersedes: 
tags: [registry, tracking]
status: active
visibility: private
---

# 追踪总表（tracking-master）

> **聚合生成文件，禁止手改。**
> 各环境只写 `registry/by-env/<env-id>-tracking.md` 自己的分片，总表由维护方用脚本聚合。
> 模板初始为空；接入后由聚合脚本填充。
