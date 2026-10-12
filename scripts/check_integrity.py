#!/usr/bin/env python3
"""work-library 完整性巡检：扫编码乱码、缺 frontmatter、重复 WL id。
用法：python3 scripts/check_integrity.py [repo_root]
输出 registry/integrity-report.md 并打印异常数。"""
import os, re, sys, datetime, collections
ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
issues = []
ids = collections.Counter()
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in (".git",)]
    for fn in files:
        if not fn.endswith(".md"): continue
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p, ROOT)
        try: text = open(p, encoding="utf-8", errors="replace").read()
        except Exception: continue
        lines = text.splitlines()
        body = "\n".join(lines)
        if len(body) > 300 and re.fullmatch(r"[A-Za-z0-9+/=\s]+", body.strip()[:400] or "x") and len(lines) <= 3:
            issues.append((rel, "疑似整文件 base64 乱码"))
        if rel not in ("INDEX.md",) and not text.startswith("---"):
            issues.append((rel, "缺 frontmatter 起始"))
        m = re.search(r"^id:\s*(WL-\d{4})", text, re.M)
        if m: ids[m.group(1)] += 1
for wid, n in ids.items():
    if n > 1: issues.append((wid, f"重复 WL id x{n}"))
out = ["# 完整性巡检报告", "", f"生成时间：{datetime.date.today()} · 异常 {len(issues)} 项", ""]
out += [f"- {a}：{b}" for a, b in issues] or ["- 无异常"]
os.makedirs(os.path.join(ROOT, "registry"), exist_ok=True)
open(os.path.join(ROOT, "registry/integrity-report.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"integrity issues: {len(issues)}")
for a, b in issues[:20]: print("-", a, b)
