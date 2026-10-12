---
title: 环境与文件夹归属总登记
id: WL-0103
type: registry
source_env: template
source_agent: "{{ASSISTANT_NAME}}"
origin: 本模板框架
created_at: "{{DATE}}"
updated_at: "{{DATE}}"
timezone: Asia/Shanghai
version: 1
supersedes: 
tags: [registry, environments]
status: active
visibility: private
---

# 环境与文件夹归属总登记（ENVIRONMENTS）

本文件是全库的「户籍册」：登记已接入的环境、每个文件夹归谁、谁能写、创建时间。新环境接入先在此登记，再动笔写文档。

## 已登记环境

> 下表为虚构示例，正式使用前按 SETUP.md 第 2–3 步替换。

| 环境 ID | 平台/宿主 | Agent | 部署类型 | 主机（型号/标识） | 接入时间 | 登记卡 | 状态 |
|---|---|---|---|---|---|---|---|
| main-env | 云端 agent 平台（示例） | 主力 agent（示例） | 云端环境 | 云平台/实例（示例） | {{DATE}} | environments/main-env.md | active，本库创建者与当前维护方 |
| desktop-env | 桌面客户端（示例） | 桌面 agent（示例） | 主机环境 | 你的主机型号（示例）/ 操作系统（示例） | {{DATE}} | environments/desktop-env.md | active，第二接入环境 |

（新环境接入后在此续行登记，一行一个环境。）

## 环境标注规范（必填）

每个环境登记时必须标清两件事，缺一不可：

1. **部署类型**：云端环境 / 主机环境（二选一）。
2. **主机标识**：主机环境必须写具体机型 + 操作系统；云端环境写云平台与实例类型。同一台主机跑多个 agent 时，主机相同、env-id 不同，靠 env-id 区分。

文档 frontmatter 的 source_env 只写 env-id；env-id 对应的部署类型与主机在本登记表与各自登记卡里查。过程文档、记忆条目标记同理只标 env-id，溯源时按此表回查物理出处。

## 环境身份延续规则（防重复新建环境）

env-id 是环境的永久身份，不是每次会话的临时编号。防重复三条：

1. **先查重再登记**：新会话接入时，先在本表按「主机标识 + agent」查重。查到已有 env-id，直接沿用，禁止再新建第二个。
2. **开工先自报**：每次提交前先确认自己的 env-id 与本表一致，文档 frontmatter 的 source_env 必须等于该 env-id；对不上停下核对，不要新建。
3. **身份要素不变则身份不变**：同一台主机、同一个 agent、同一个工作区，永远是同一个 env-id。只有换主机、换 agent 产品、或用户明确要求拆分时，才新建 env-id，并在新登记行注明承接自哪个旧 env-id。旧登记不删除（标 deprecated），文档溯源仍按旧标记查。

## 同一 env 多端共写规则

同一 env-id 可以有多个运行端，视为同一个人的两只手：

1. 共写同一套正本（memory、清单分片），不另建身份、不分叉内容。
2. 每次写入前必须刚拉取远端最新并核对 version 与 blob SHA；写完在 memory/CHANGELOG.md 或分片文末注释里留一行：时间、端点自述、改了什么。
3. 上传文件内容必须是原文 Markdown，严禁把 base64 编码文本当文件内容写入。
4. 两端状态不一致时以先到的用户确认为准，差异列清单报用户，不各自整表覆盖。

## 文件夹归属与写入规则

| 路径 | 归属 | 用途 | 谁能写 | 备注 |
|---|---|---|---|---|
| README.md / INDEX.md / SYNC_PROTOCOL.md / taxonomy.md | 全库共享（维护方维护） | 总览、自动索引、同步协议、标签词表 | 维护方；INDEX 由脚本生成禁手改 | 建库时创建 |
| docs/ | 共享（按文档 owner） | 经验文档、手册、调研结论 | 每份文档 frontmatter 的 source_env 即 owner，仅 owner 改 | — |
| skills/ | 共享（按 skill owner） | 可复用 skill（指针+已审副本） | owner 环境 | — |
| memory/ | 共享权威（维护方单写） | 用户长期记忆、用户档案、人物档案 | 维护方单写，其他环境只读+提案制 | 见 memory/README.md；private 级 |
| registry/ | 共享（分片自维护） | 目标/追踪总表与各环境分片 | 总表维护方聚合；by-env/<env>-*.md 由各环境只写自己分片 | 本文件亦在此区 |
| environments/ | 各环境私有 | 环境登记卡（<env-id>.md）、人格目录 | 各环境只写自己文件与目录；禁止同名文件与目录并存 | 人格目录统一用 `<env-id>-persona/` |
| templates/ | 共享（维护方） | 文档与 skill 模板 | 维护方 | 建库时创建 |
| scripts/ | 共享（维护方） | 索引生成、版本校验 | 维护方 | 见 scripts/ |
| process/<env>/ | 各环境私有（按环境分片） | 过程文档快照：草稿、基线、分析稿、执行清单 | 各环境只写自己目录 | 见 process/README.md |
| inbox/<env>/ | 通告区 | 维护方→环境的下行通告；`inbox/_global/` 为全员广播 | 维护方写各环境 inbox；各环境同步前先读自己 inbox 未读通告 | SYNC_PROTOCOL 第 13 条 |
| drafts/<env>/ | 草稿区（按需启用） | 未定稿草稿，成熟后经用户确认提升进共享区 | 各环境只写自己 | 按需启用 |

## 登记办法（新环境三步）

1. 在「已登记环境」表加一行，并新建 environments/<env-id>.md 登记卡（平台、agent、能读写范围、接入时间）。
2. 在 registry/by-env/ 建自己的 goals/tracking 分片；在 environments/ 建自己的人格子目录，命名为 `<env-id>-persona/`（禁止与登记卡 `<env-id>.md` 同名建目录）。
3. 其余共享区先只读：读 README、SYNC_PROTOCOL、本登记表与 INDEX，熟悉后再按单写者规则写入。

## 同名 agent 的区分约定

如果多个环境用同一个 agent 名（如三个云端环境都叫同一个名字），为避免用户分不清是谁在说话：
1. 自报身份时必须带 env-id（如「我是助手（cloud-env-2)」）。
2. 登记卡的 agent 字段注明各自 env-id。
3. 对话档案按 endpoint 区分，不合并。
