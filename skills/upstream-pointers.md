---
title: 上游 skill 指针登记
id: WL-0500
type: registry
source_env: template
source_agent: "{{ASSISTANT_NAME}}"
origin: 本模板框架
created_at: "{{DATE}}"
updated_at: "{{DATE}}"
timezone: Asia/Shanghai
version: 1
supersedes: 
tags: [registry, skill]
status: active
visibility: private
---

# 上游 skill 指针登记（upstream-pointers）

> 上游 skill（他人维护、你只使用）只登记指针，不存副本。模板初始为空表。

| skill 名 | 上游地址（示例） | 用途（示例） | 引入环境 | 引入日期 |
|---|---|---|---|---|
| example-skill | https://example.com/skill-repo | 示例：演示指针格式 | main-env | {{DATE}} |
