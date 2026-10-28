---
title: 受控标签词表
id: WL-0004
type: protocol
source_env: template
source_agent: "{{ASSISTANT_NAME}}"
origin: 本模板框架
created_at: "{{DATE}}"
updated_at: 2026-10-28
timezone: Asia/Shanghai
version: 2
supersedes: 
tags: [protocol, taxonomy]
status: active
visibility: private
---

# 受控标签词表（新增加标签须先登记到这里）

## type/* 文档类型
playbook, research, skill, memory, registry, protocol, prompt, log, decision

## status/* 状态
active, draft, archived, superseded

## topic/* 主题（按需登记扩充，示例）
study, work, finance, health, social, ai-news

## frontmatter 可选字段：layer（模板框架同步）

- 用途：标注文档所属记忆层次，便于新环境接手时快速判断层次。
- 取值：L1（证据层：过程快照类）/ L2（时间线类）/ L3（规则/经验类）/ L4（跨项目画像子集）。
- 规则：可选字段，不强制；旧文档不动；不填时按 MAINTENANCE.md 六之二映射表归类；不得用 layer 字段改变文档 owner 与权威层级。

## 变更记录

- 2026-10-28：v1→v2，登记 frontmatter 可选字段 layer（L1/L2/L3/L4，模板框架同步）。
