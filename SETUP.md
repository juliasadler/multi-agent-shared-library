# 搭建你自己的多 Agent 共享库（10 分钟上手）

本仓库是一个模板：目录骨架 + 协作协议 + 工具脚本，不含任何个人信息。按下面步骤把它变成属于你自己的共享库。

## 第 0 步：准备

- 一个 GitHub 账号；本库建议设为**私有仓库**（memory/ 区含用户记忆与人物档案，只在私有仓内流转）。
- 你常用的 agent 环境（至少一个，如某云端 agent 或桌面客户端）。

## 第 1 步：建仓（2 分钟）

1. Fork 本仓库，或新建私有仓库后把本模板文件全部拷入。
2. 仓库名建议：`work-library`、`agent-shared-library`，或任何你喜欢的名字。

## 第 2 步：替换占位符（3 分钟）

全库搜索以下占位符并替换：

| 占位符 | 替换成 |
|---|---|
| `{{OWNER_NAME}}` | 你希望 agent 称呼你的名字/称呼 |
| `{{ASSISTANT_NAME}}` | 你的主力 agent 的名字（可空，不用就删掉） |
| `{{DATE}}` | 今天的日期（YYYY-MM-DD） |

环境 ID 示例（`main-env`、`desktop-env`、`chat-env`、`agent-env`、`cli-env`、`cloud-env-2`）全部是示例：
按「主机标识 + agent」的规则给你的每个环境起 env-id（如 `macbook-claude`、`cloud-muse`），
然后在 `registry/ENVIRONMENTS.md` 登记，替换掉示例行。

## 第 3 步：登记第一个环境（2 分钟）

1. 在 `registry/ENVIRONMENTS.md`「已登记环境」表加一行：你的第一个环境，状态标注为维护方（maintainer）。
2. 新建 `environments/<你的env-id>.md` 登记卡（平台、agent、时区、能访问的本地路径、部署类型与主机标识）。
3. 在 `registry/by-env/` 新建 `<env-id>-goals.md` 与 `<env-id>-tracking.md` 两个分片（格式见 by-env/README.md）。

## 第 4 步：推送验证（1 分钟）

1. 提交并推送到远端。
2. 回读验证：确认远端文件列表与本地一致，README 首页能正常渲染。

## 第 5 步：接入第二个 agent（2 分钟）

1. 把 `UNIVERSAL_PROMPT.md` 全文发给第二个 agent。
2. 它会按提示词完成：读 SYNC_PROTOCOL.md → 读 README/INDEX → 在 registry/ENVIRONMENTS.md 查重 → 新建自己的登记卡与分片。
3. 第一次写入前，它必须执行 SYNC_PROTOCOL 第 7 条「写前握手」（小改动试水 + 回读验证）。

## 之后

- 日常协作查 README.md「按任务找入口」表。
- 每周由维护方跑一次巡检（见 MAINTENANCE.md 第二节）。
- 冲突时停下来，用户拍板（见 SYNC_PROTOCOL.md 第 4 条）。

## 隐私提醒

- 本模板不含任何个人信息；但你接入后写入的 memory/ 内容会含你的隐私，**务必保持仓库私有**。
- 密码、API 密钥、token、验证码永不入库，走你自己的保险库/密钥管理。
- 如需把某份经验文档分享给别人，先脱敏（去掉称呼、人名、账号、路径等）再发。

## 可选：自动重建索引

想让 GitHub 定时自动重建 `INDEX.md`，按 `docs/GitHub-Actions-工作流-手动配置.md` 手动添加工作流文件（推送通道不支持直接写入 `.github/workflows/`，需在网页端手动创建）。
