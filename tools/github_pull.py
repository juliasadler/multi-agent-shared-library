#!/usr/bin/env python3
"""GitHub 仓库文件批量拉取（修复版实现）。

要点（针对旧实现全量 403/3xx 失败的修复）：
- 走 repositories/<仓库ID>/contents 路径，天然绕开账号改名后的 301 重定向；
- 每请求带 Authorization: Bearer + Accept: application/vnd.github+json；
- 串行拉取（可调间隔），避免并发触发 secondary rate limit 型 403；
- 大响应由 dynamic_credentials.read_response_body 分块读取，不整段读爆；
- 落盘后做 blob SHA 校验（git 风格 sha1("blob <len>\\0"+内容)），对不上算失败；
- 任一文件 401/403 立即停批并报错（通道级问题不硬刷）。

用法:
  github_pull.py --repo-id 1403962207 --list files.txt --dest /path/to/root [--delay 0.15]
  files.txt: 每行一个仓库内相对路径（# 开头为注释）。
退出码: 0=全成功; 2=通道级失败已停批; 3=部分失败（逐项列出）。
"""
import argparse, base64, hashlib, json, os, sys, time
import urllib.request, urllib.error, urllib.parse

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import dynamic_credential_entry, read_response_body  # noqa: E402


def blob_sha(data: bytes) -> str:
    h = hashlib.sha1()
    h.update(f"blob {len(data)}\0".encode())
    h.update(data)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-id", required=True)
    ap.add_argument("--list", required=True, dest="listfile")
    ap.add_argument("--dest", required=True)
    ap.add_argument("--delay", type=float, default=0.15)
    ap.add_argument("--cred", default="custom.github")
    args = ap.parse_args()

    paths = []
    with open(args.listfile, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                paths.append(line)
    print(f"[pull] 清单 {len(paths)} 个文件 → {args.dest}")

    entry = dynamic_credential_entry(args.cred)
    auth = f"Bearer {entry['surrogate']}"

    ok = fail = 0
    failures = []
    for i, p in enumerate(paths, 1):
        url = (f"https://api.github.com/repositories/{args.repo_id}/contents/"
               f"{urllib.parse.quote(p)}?ref=main")
        req = urllib.request.Request(url)
        req.add_header("Authorization", auth)
        req.add_header("Accept", "application/vnd.github+json")
        try:
            resp = urllib.request.urlopen(req, timeout=60)
            d = json.loads(read_response_body(resp) or b"{}")
        except urllib.error.HTTPError as e:
            print(f"[pull] {p} -> HTTP {e.code}，停批（通道级问题先修通道，勿硬刷）")
            print(f"RESULT ok={ok} fail={fail + 1} stopped_at={p} http={e.code}")
            return 2
        except Exception as e:  # noqa: BLE001
            fail += 1
            failures.append((p, f"请求异常 {e}"))
            continue
        if d.get("encoding") != "base64" or "content" not in d:
            fail += 1
            failures.append((p, f"响应格式异常 encoding={d.get('encoding')}"))
            continue
        raw = base64.b64decode(d["content"])
        sha_ok = blob_sha(raw) == d.get("sha")
        size_ok = len(raw) == d.get("size")
        if not (sha_ok and size_ok):
            fail += 1
            failures.append((p, f"校验不过 sha_ok={sha_ok} size_ok={size_ok}"))
            continue
        out = os.path.join(args.dest, p)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "wb") as f:
            f.write(raw)
        ok += 1
        if i % 10 == 0 or i == len(paths):
            print(f"[pull] 进度 {i}/{len(paths)} ok={ok} fail={fail}")
        if args.delay:
            time.sleep(args.delay)

    print(f"RESULT ok={ok} fail={fail} total={len(paths)}")
    for p, why in failures:
        print(f"  FAIL {p}: {why}")
    return 0 if fail == 0 else 3


if __name__ == "__main__":
    sys.exit(main())
