---
title: 过程文档区说明（接手指南）
id: WL-0900
type: process
source_env: template
source_agent: "{{ASSISTANT_NAME}}"
origin: 本模板框架
created_at: "{{DATE}}"
updated_at: "{{DATE}}"
timezone: Asia/Shanghai
version: 1
supersedes: 
tags: [process]
status: active
visibility: private
---

# 过程文档区（process/）

存放各环境在具体目标执行中产生的过程文档：草稿、基线快照、分析工作稿、执行清单、目标说明。目的是让任何环境随时能接手另一个环境进行中的任务。

## 隔离规则

- 路径固定为 `process/<env-id>/<目标或主题>/<原文件名>`，每个环境只写自己的目录，互不编辑。
- 每份文档头部带 frontmatter 标注：来源环境、原本地出处、同步时间；正文与原件一致（仅剥离原有头部元信息）。
- 过程文档默认是「快照」：原件在本环境继续演进时，按维护节奏增量更新本区（version+1），以 origin 路径为准对账。

## 接手办法

1. 先读 registry/ENVIRONMENTS.md 确认原环境与归属。
2. 在本区按目标找该任务的过程文档，结合 registry 里的目标/追踪总表看当前状态。
3. 接手后在本环境目录新建自己的续作文件（标注承接自哪份、哪个环境），不直接改原环境文件；需要合并时走提案/清单流程。
