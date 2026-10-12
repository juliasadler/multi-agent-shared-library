---
title: 多 Agent 共享工作库（模板）
id: WL-0000
type: protocol
source_env: template
source_agent: "{{ASSISTANT_NAME}}"
origin: 本模板框架
created_at: "{{DATE}}"
updated_at: "{{DATE}}"
timezone: Asia/Shanghai
version: 1
supersedes: 
tags: [protocol, onboarding]
status: active
visibility: private
---

<!-- 本仓库由 multi-agent-shared-library 模板生成。首次使用请先读 SETUP.md，完成 {{OWNER_NAME}} 替换与第一个环境登记。 -->

# 多 Agent 共享工作库

这是 {{OWNER_NAME}} 的多环境 agent 工作库：每个环境的 agent 把自己沉淀的文档、skill、记忆、清单以 Markdown 形式提交到本仓库，供其他环境拉取复用。

**本文件是全库唯一入口。** 新 agent 只读这一份，就应知道：自己是谁、先做什么、各类任务去哪读/去哪写、流程怎么走、红线在哪。细节规则在各专档里，本文件给出路径与摘要，冲突时以专档为准（同步事项以 SYNC_PROTOCOL.md 为最高规则）。

## 参与共享的环境（示例，需替换）

下表为示例环境，实际使用时替换成你自己的环境。完整登记见 registry/ENVIRONMENTS.md。

| 环境 ID | Agent | 运行位置 | 负责什么 |
|---|---|---|---|
| main-env | 主力 agent（维护方） | 云端 | 记忆正本维护、清单聚合、全库巡检（维护方） |
| desktop-env | 桌面 agent | 主机 | 本机文档库与知识库沉淀 |
| chat-env | 对话 agent | 主机 | 本机记忆快照与 skill 清单登记 |

## 提示词入口（你是怎么来到这里的）

你能读到这份 README，通常是因为用户把根目录 `UNIVERSAL_PROMPT.md` 的全文作为提示词发给了你。本文就是你的主操作手册：按「快速开始」完成登记后，日常工作查「按任务找入口」表即可，不必通读全库。规则冲突时以 `SYNC_PROTOCOL.md` 为准；不确定就停下来问用户。

## 快速开始（新 agent 五步）

0. （仅新环境，或用户明确指明要构建新环境时）先读你的上手指南：见 docs/ 下的各环境上手指南（模板初始为空，按需补充）。
1. 读 `SYNC_PROTOCOL.md`（同步与防覆盖协议，全库最高规则）。
2. 读 `INDEX.md`（全库文档索引，脚本生成禁手改）摸清已有沉淀，避免重复造文档。
3. 认领身份：先在 `registry/ENVIRONMENTS.md` 按「主机标识+agent」查重，已有自己的 env-id 就沿用（防重复新建，细则见登记表身份延续规则）；确实是新环境才在环境表加一行，并新建 `environments/<你的env-id>.md` 登记卡（环境名、平台、agent、时区、可访问路径、部署类型与主机标识：云端环境写云平台/实例，主机环境必须写具体机型与操作系统，规范见 registry/ENVIRONMENTS.md）。env-id 用小写短横线，如 chat-env、agent-local。
4. 建自己的地盘：`registry/by-env/<env-id>-goals.md` 与 `<env-id>-tracking.md` 分片、`process/<env-id>/` 过程区、`environments/<env-id>/` 人格目录（需要时）。
5. 开工：按下文「按任务找入口」表执行；每次写入走「写入八步」；推送后向用户汇报。

## 索引维护（每个环境都能自己更新）

INDEX.md 由 scripts/build_index.py 生成，但**不要求每个环境都跑脚本**，分两档：

1. **手添行（默认，人人可做）**：推送新文档时，在同一次提交里往 INDEX.md 对应分区表格末尾追加一行，格式与脚本输出一致：`| WL-xxxx | 标题 | docs/路径.md | env-id | YYYY-MM-DD | v1 |`（列序以 INDEX.md 现表为准）。改已有文档则更新该行的日期与版本。手添行必须与文档 frontmatter 一致。
2. **脚本全量重建（维护方）**：维护方在每周巡检时跑 build_index.py 做全量重排与校验，手添行会被脚本接管校准；发现行与 frontmatter 对不上时以 frontmatter 为准修正，并记入对账说明。

这样任何环境（哪怕不能跑 Python）推送文档时自带索引行，索引永远不缺新文档；脚本只负责定期校准，不再成为接入门槛。

## 按任务找入口（最常用）

| 你要做的事 | 先读 | 写到哪 | 关键规则 |
|---|---|---|---|
| 查已有经验/文档 | INDEX.md 按标签找 | 只读 | 引用注明出处 id |
| 写新经验文档 | templates/doc-template.md | docs/ | frontmatter 必填（见下）；id 查 INDEX 最大号顺延 |
| 更新已有文档 | 该文档 frontmatter 确认 owner | 原文件 | 仅 owner 可改；version+1；带 blob SHA 写 |
| 改别人的文档 | — | inbox/<对方env>/ 新建意见文档 | 绝不直接改他人正文 |
| 接手/更新人物档案 | memory/people/人物档案入口.md → 对象档案索引 | 维护方写 memory/people/<person-id>/ 三件套；非维护方走 memory/proposals/ 提案 | 正本单写者；一次只读一个对象；分析完必回写三件套 |
| 追加/修正用户记忆 | memory/README.md | memory/proposals/ 新建提案 | 记忆正本单写者，他人只提案 |
| 记录过程文档（草稿/基线/分析稿） | process/README.md | process/<自己env>/<目标>/ | 只写自己目录；标注原出处与原文件时间 |
| 接手别人的任务 | registry/ENVIRONMENTS.md + registry 总表 | 自己 process 目录新建续作 | 先对状态再动手；续作标注承接来源 |
| 更新目标/追踪 | registry/ENVIRONMENTS.md 归属表 | registry/by-env/ 自己分片 | 总表脚本聚合，禁手改 |
| 新增/更新 skill | templates/skill-template.md | skills/<name>/ | 上游 skill 只放指针不存副本 |
| 判断同名文档哪份新 | registry/duplicates-check.md | — | 总表>正本>快照；同层比 version→updated_at→原文件时间 |
| 冲突/写入被拒（409） | SYNC_PROTOCOL 冲突章 | 停写，列差异报用户 | 输方改名归档，不删除、不硬写 |
| 不知道该不该入库 | MAINTENANCE.md 第一节 | — | 满足任一入库条件即入；草稿先 drafts/，成熟再提升 |

## 目录地图

- `docs/` 共享经验文档（手册、调研、SOP；每份有 owner）
- `skills/` 可复用 skill 与上游指针
- `memory/` 用户长期记忆（共享权威，单写者）＋ `memory/proposals/` 提案区 ＋ `memory/CHANGELOG.md` 变更日志
- `registry/` 目标/追踪总表、环境归属总登记 ENVIRONMENTS、对账报告 duplicates-check、构件库清单
- `process/<env>/` 过程文档（按环境隔离，接手指南在其 README）
- `environments/<env>/` 各环境登记卡与人格目录
- `inbox/<env>/` 跨环境投递区（只投递，不直接改对方文件）
- `templates/` 文档与 skill 模板
- `scripts/` build_index.py（重建索引）、check_version.py（版本校验）、check_duplicates.py（同名对账）、check_integrity.py（完整性检查）、dedupe_note.py（去重）
- 根目录：`SYNC_PROTOCOL.md` 同步协议、`MAINTENANCE.md` 维护手册、`UNIVERSAL_PROMPT.md` 给新 agent 的接入提示词、`taxonomy.md` 标签受控词表、`SETUP.md` 新手搭建指南

## frontmatter 必填字段（每份文档头部）

title、id（WL-xxxx，查 INDEX 顺延分配）、type、source_env（你的 env-id）、source_agent、origin（出处：本地路径或来源说明）、created_at、updated_at、timezone、version（新建 1，修改 +1）、tags（从 taxonomy.md 受控词表选）、status、visibility。过程文档另加 source_file_time（原文件修改时间）。

## 写入八步（每次同步照做）

1. 拉取远端最新（读目标文件当前 blob SHA 与 version）。
2. 校验基线：version/SHA 对不上 → 停写报告，不覆盖。
3. 定归属：确认 owner 是自己、位置符合目录地图。
4. 备 frontmatter：新文档取新 id，旧文档 version+1、更新 updated_at。
5. 写入：API PUT 带当前 blob SHA（乐观锁）。
6. 重建索引：跑 scripts/build_index.py，连 INDEX.md 一起提交。
7. 回读验证：远端文件与内容抽查一致。
8. 汇报用户：改了哪些文件、版本、提交、验证结果（简体中文）。

## 长期维护节奏（细则见 MAINTENANCE.md）

- 事件驱动：产出重要文档当次同步，不攒批。
- 每周巡检：维护方每周日晚盘点补推遗漏并重跑对账。
- 月度盘点：索引完整性、失效引用、标签词表、仓库体积。
- 记忆变更：正本每次变更同步记 memory/CHANGELOG.md 一行。

## 红线

- 绝不整文件覆盖、绝不 force push；旧副本被 409 拒绝是正常防线，不要绕。
- 密码、密钥、token、验证码永不入库（哪怕私有仓），走保险库。
- 删除、改名、覆盖他人文档必须经用户确认；冲突最终由用户拍板。
- 记忆正本只有一个写手；目标/追踪总表禁止手改。
- 不确定就停下来问用户，不猜、不删、不覆盖。
