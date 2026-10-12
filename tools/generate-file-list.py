#!/usr/bin/env python3
"""列出 GitHub 仓库某目录下全部文件清单（用于定位"应拉 N 个文件"的集合）。

用法:
  generate-file-list.py --repo-id 1403962207 --dir "docs" --out files.txt [--ref main]

输出每行一个仓库内相对路径，可直接喂给 github_pull.py --list。
依赖 dynamic_credentials（保险库 GitHub token，不进文件）。
"""
import argparse, json, sys
import urllib.request, urllib.error

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import dynamic_credential_entry, read_response_body  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-id", required=True)
    ap.add_argument("--dir", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--ref", default="main")
    ap.add_argument("--cred", default="custom.github")
    args = ap.parse_args()

    entry = dynamic_credential_entry(args.cred)
    auth = f"Bearer {entry['surrogate']}"
    headers = {"Authorization": auth, "Accept": "application/vnd.github+json"}

    import urllib.parse
    prefix = urllib.parse.quote(args.dir) if args.dir else ""
    url = f"https://api.github.com/repositories/{args.repo_id}/contents/{prefix}?ref={args.ref}"
    req = urllib.request.Request(url)
    for k, v in headers.items():
        req.add_header(k, v)
    tree = json.loads(read_response_body(urllib.request.urlopen(req, timeout=60)) or b"[]")

    paths = []

    def walk(items, base):
        for it in items:
            rel = f"{base}/{it['name']}".lstrip("/")
            if it["type"] == "file":
                paths.append(rel)
            elif it["type"] == "dir":
                sub_url = f"https://api.github.com/repositories/{args.repo_id}/contents/{urllib.parse.quote(rel)}?ref={args.ref}"
                r = urllib.request.Request(sub_url)
                for k, v in headers.items():
                    r.add_header(k, v)
                try:
                    sub = json.loads(read_response_body(urllib.request.urlopen(r, timeout=60)) or b"[]")
                except urllib.error.HTTPError as ex:
                    print(f"[warn] 目录读取失败 {rel}: {ex.code}", file=sys.stderr)
                    continue
                walk(sub, rel)

    walk(tree, args.dir.rstrip("/"))
    with open(args.out, "w", encoding="utf-8") as f:
        for p in sorted(paths):
            f.write(p + "\n")
    print(f"[list] 目录 '{args.dir or '/'}' 共 {len(paths)} 个文件 → {args.out}")


if __name__ == "__main__":
    main()
