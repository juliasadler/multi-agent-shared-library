#!/usr/bin/env python3
"""同名/同源文档对账：扫描全库 frontmatter，按 title 与 origin 分组，
列出重复文档并给出哪份更新（version 高者胜，同版比 updated_at，再比 source_file_time）。"""
import os, re, sys, collections
root = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/workspace/work-library")
def fm_of(p):
    t = open(p, encoding="utf-8").read(3000)
    m = re.match(r"^---\n(.*?)\n---", t, re.S)
    d = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1); d[k.strip()] = v.strip()
    return d
groups = collections.defaultdict(list)
for dp, dns, fns in os.walk(root):
    if ".git" in dp: continue
    for n in fns:
        if not n.endswith(".md"): continue
        p = os.path.join(dp, n); fm = fm_of(p)
        if not fm.get("id", "").startswith("WL-"): continue
        key = fm.get("origin") or fm.get("title", n)
        groups[key].append((os.path.relpath(p, root), fm))
dups = {k: v for k, v in groups.items() if len(v) > 1}
print(f"# 同名文档对账报告\n\n共 {len(groups)} 个登记标题，重复 {len(dups)} 组。\n")
for k, v in sorted(dups.items()):
    def rank(x):
        fm = x[1]
        return (int(fm.get("version", "1") or 1), fm.get("updated_at", ""), fm.get("source_file_time", ""))
    v2 = sorted(v, key=rank, reverse=True)
    print(f"## {k}")
    for i, (path, fm) in enumerate(v2):
        mark = "← 最新（以此为准）" if i == 0 else "（旧副本，应标 superseded）"
        print(f"- {path} | env={fm.get('source_env')} v{fm.get('version')} updated={fm.get('updated_at')} src_time={fm.get('source_file_time','-')} {mark}")
    print()
if not dups:
    print("当前无跨环境同名冲突。")
