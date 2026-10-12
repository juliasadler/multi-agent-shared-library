# 环境区（environments/）

每个环境两样东西（都只写自己的，不动别人的）：

1. **登记卡** `<env-id>.md`：环境名、平台、agent、时区、能访问的本地路径、部署类型与主机标识、接入时间。文件名即 env-id。
2. **人格目录** `<env-id>-persona/`（按需）：该环境 agent 的人设与操作手册（如 SOUL / IDENTITY / AGENTS 等），各环境自治、互不统一。

## 规则

- 禁止同名文件与目录并存（如 `main-env.md` 与 `main-env/` 不能同时存在）：人格目录统一用 `<env-id>-persona/` 后缀。
- 登记卡在 registry/ENVIRONMENTS.md 先查重再新建（防重复身份）。
