#!/usr/bin/env python3
"""扫描 work-library 全部 .md 的 frontmatter，生成 INDEX.md。用法: python3 scripts/build_index.py"""
import os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
skip = {"INDEX.md"}
skip_dirs = {"templates", ".git"}
rows = []
for dirpath, _, names in os.walk(root):
    parts = set(os.path.relpath(dirpath, root).split(os.sep))
    if parts & skip_dirs:
        continue
    for n in sorted(names):
        if n.endswith(".md") and n not in skip:
            p = os.path.join(dirpath, n)
            text = open(p, encoding="utf-8").read(3000)
            m = re.match(r"^---\n(.*?)\n---", text, re.S)
            if not m:
                continue
            fm = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
            rel = os.path.relpath(p, root)
            if not fm.get("id","").startswith("WL-"):
                continue
            rows.append((fm.get("id","?"), fm.get("title","?"), fm.get("type","?"),
                         fm.get("source_env","?"), fm.get("version","?"), fm.get("updated_at","?"), rel))
rows.sort(key=lambda r: r[0])
out = ["# 全库总索引\n", "> 本文件由 scripts/build_index.py 自动生成，禁止手改。\n",
       "| id | 标题 | 类型 | 来源环境 | 版本 | 更新 | 文件 |", "|---|---|---|---|---|---|---|"]
out += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |" for r in rows]
open(os.path.join(root, "INDEX.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"INDEX.md regenerated: {len(rows)} docs")

# --- 同步刷新 README 的自动统计区（AUTO:STATS 标记之间），让仓库主页自动展示全库动态 ---
from collections import Counter
readme_path = os.path.join(root, "README.md")
if os.path.exists(readme_path):
    envs = sorted(set(r[3] for r in rows if r[3] and r[3] != "?"))
    counts = Counter(r[3] for r in rows)
    latest = sorted(rows, key=lambda r: r[5], reverse=True)[:10]
    lines = ["<!-- AUTO:STATS 开始（脚本自动生成，勿手改） -->", "",
             "## 全库动态（自动更新）", "",
             f"登记文档共 **{len(rows)}** 份 · 接入环境 **{len(envs)}** 个", "",
             "| 环境 | 文档数 |", "|---|---|"]
    lines += [f"| {e} | {counts[e]} |" for e in envs]
    lines += ["", "最近更新（前 10）：", "", "| id | 标题 | 来源环境 | 更新 |", "|---|---|---|---|"]
    lines += [f"| {r[0]} | {r[1]} | {r[3]} | {r[5]} |" for r in latest]
    lines += ["", "<!-- AUTO:STATS 结束 -->"]
    block = "\n".join(lines)
    txt = open(readme_path, encoding="utf-8").read()
    if "<!-- AUTO:STATS 开始" in txt:
        txt = re.sub(r"<!-- AUTO:STATS 开始.*?<!-- AUTO:STATS 结束 -->", block, txt, flags=re.S)
    else:
        txt = txt.rstrip() + "\n\n" + block + "\n"
    open(readme_path, "w", encoding="utf-8").write(txt)
    print("README AUTO:STATS refreshed")
