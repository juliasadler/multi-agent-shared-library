# GitHub Actions 工作流（需手动配置）

`scripts/build_index.py` 可以配成 GitHub Actions 定时自动重建 `INDEX.md`。
由于推送通道限制工作流文件，本模板不直接带 `.github/workflows/` 目录，
请按下面步骤手动创建：

1. 在你的仓库新建文件 `.github/workflows/build-index.yml`
2. 把下面 YAML 全文粘贴进去并提交：

```yaml
name: build-index

# 任何环境推送/修改 Markdown 文档后，自动重建 INDEX.md 并提交回仓库。
# 这样每个环境只需推送自己的文档，不必本地跑脚本更新索引。
on:
  push:
    branches: [main]
    paths:
      - "**/*.md"
      - "scripts/build_index.py"
      - ".github/workflows/build-index.yml"
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: build-index
  cancel-in-progress: false

jobs:
  build-index:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Rebuild INDEX.md
        run: python3 scripts/build_index.py
      - name: Commit INDEX.md if changed
        run: |
          if git diff --quiet -- INDEX.md; then
            echo "INDEX.md unchanged"
          else
            git config user.name "work-library-index-bot"
            git config user.email "actions@github.com"
            git add INDEX.md README.md
            git commit -m "chore(index): 自动重建索引 [skip ci]"
            for i in 1 2 3; do
              git pull --rebase origin main && git push && break
              sleep 5
            done
          fi
```

3. 推送后在仓库 Actions 页确认工作流已启用。

工作流内容说明：定时（或手动触发）运行 `scripts/build_index.py`，
若 `INDEX.md` 有变化则自动提交回仓库。
