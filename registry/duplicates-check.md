---
title: 同名文档对账报告
id: WL-0104
type: registry
source_env: template
source_agent: "{{ASSISTANT_NAME}}"
origin: 本模板框架
created_at: "{{DATE}}"
updated_at: "{{DATE}}"
timezone: Asia/Shanghai
version: 1
supersedes: 
tags: [registry]
status: active
visibility: private
---

# 同名文档对账报告（duplicates-check）

> 由 scripts/check_duplicates.py 按 origin（同源路径）分组扫描全库生成。
> 维护方在每周巡检时重跑；发现冲突组时停下汇报用户，不自动合并。
> 判定规则见 SYNC_PROTOCOL.md「同一文档多环境并存时的最新判定」：
> registry 总表 > 共享区正本 docs/memory > 各环境 process 快照；同层比 version → updated_at → 原文件时间。
>
> 模板初始为空；首次运行脚本后填充。
