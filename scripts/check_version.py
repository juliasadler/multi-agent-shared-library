#!/usr/bin/env python3
"""写前版本校验：对比本地文件 frontmatter version 与预期基线版本。
用法: python3 scripts/check_version.py <文件> <预期version>
退出码 0=一致可写, 2=版本不一致（禁止写入，先拉取并报告冲突）"""
import re, sys
path, expected = sys.argv[1], int(sys.argv[2])
text = open(path, encoding="utf-8").read(3000)
m = re.search(r"^version:\s*(\d+)", text, re.M)
if not m:
    print("FAIL: no version field"); sys.exit(2)
cur = int(m.group(1))
if cur != expected:
    print(f"CONFLICT: file version={cur}, your baseline={expected}. STOP: pull latest and report diff.")
    sys.exit(2)
print(f"OK: version {cur} matches baseline, safe to write")
