# 全库文档索引（INDEX）

> 本文件由 scripts/build_index.py 自动生成，**禁止手改**（手添行规则见 README.md「索引维护」节）。
> 模板初始状态为空表；接入后按 frontmatter 的 id 登记文档。

## 格式说明

每行：`| id | 标题 | 路径 | 来源环境 | 更新日期 | 版本 |`

- `id`：WL-xxxx，全局唯一，一经分配永不复用（取号规则见 SYNC_PROTOCOL.md 第 14 条）。
- 新文档推送时，在同一次提交里向对应分区表末尾追加一行（手添行），脚本定期校准。

## 协议（protocol）

| id | 标题 | 路径 | 来源环境 | 更新日期 | 版本 |
|---|---|---|---|---|---|
| WL-0000 | 多 Agent 共享工作库（模板） | README.md | template | {{DATE}} | v1 |
| WL-0001 | 同步与防覆盖协议 | SYNC_PROTOCOL.md | template | {{DATE}} | v1 |
| WL-0002 | 给其他 agent 的通用提示词 | UNIVERSAL_PROMPT.md | template | {{DATE}} | v1 |
| WL-0003 | （示例行，替换用） | docs/example.md | main-env | {{DATE}} | v1 |
| WL-0004 | 受控标签词表 | taxonomy.md | template | {{DATE}} | v1 |
| WL-0103 | 环境与文件夹归属总登记 | registry/ENVIRONMENTS.md | template | {{DATE}} | v1 |
| WL-0113 | 构件库文档清单 | registry/library-manifest.md | template | {{DATE}} | v1 |
| WL-0202 | 记忆与人格区说明 | memory/README.md | template | {{DATE}} | v1 |
| WL-0203 | 工作库维护手册 | MAINTENANCE.md | template | {{DATE}} | v1 |
| WL-0900 | 过程文档区说明 | process/README.md | template | {{DATE}} | v1 |
| WL-3021 | 对象档案索引 | memory/people/对象档案索引.md | template | {{DATE}} | v1 |
| WL-3022 | 人物档案协议 | memory/people/人物档案协议.md | template | {{DATE}} | v1 |
| WL-3024 | 人物档案入口 | memory/people/人物档案入口.md | template | {{DATE}} | v1 |

## 文档（docs）

| id | 标题 | 路径 | 来源环境 | 更新日期 | 版本 |
|---|---|---|---|---|---|
| — | （暂无） | — | — | — | — |

## 记忆（memory）

| id | 标题 | 路径 | 来源环境 | 更新日期 | 版本 |
|---|---|---|---|---|---|
| — | （暂无） | — | — | — | — |

## 技能（skills）

| id | 标题 | 路径 | 来源环境 | 更新日期 | 版本 |
|---|---|---|---|---|---|
| — | （暂无） | — | — | — | — |

## 登记（registry）

| id | 标题 | 路径 | 来源环境 | 更新日期 | 版本 |
|---|---|---|---|---|---|
| — | （暂无） | — | — | — | — |

<!-- AUTO:STATS 开始（脚本自动生成，勿手改） -->

## 全库动态（自动更新）

登记文档共 **0** 份 · 接入环境 **0** 个

<!-- AUTO:STATS 结束 -->
