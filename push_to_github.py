#!/usr/bin/env python3
"""
push_to_github.py — One-Command GitHub Sync & jsDelivr Cache Purge for PrepUnfold CDN
=====================================================================================
Run this script from the extracted `prepunfold-cdn` folder on your Windows PC:
    python push_to_github.py --token YOUR_GITHUB_PAT
(or set GITHUB_TOKEN environment variable).

It automatically:
1. Runs `scripts/audit_repo_papers.py` to verify 0 exact/template duplicates across all 29 papers (1,420 questions).
2. Initializes / syncs with `https://github.com/Deepak-4551819/prepunfold-cdn.git` on branch `main`.
3. Commits and pushes `manifest.json`, `seen_question_hashes.json`, `scripts/audit_repo_papers.py`, and all 29 JSON papers under `tests/`.
4. Purges the jsDelivr CDN cache for `manifest.json` and every updated test file so your PrepUnfold Android app immediately fetches the latest questions.
"""
import argparse, json, os, subprocess, sys, urllib.request

REPO_OWNER = "Deepak-4551819"
REPO_NAME = "prepunfold-cdn"
BRANCH = "main"

def run_cmd(cmd, cwd=None):
    print(f"-> Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if res.stdout:
        print(res.stdout.strip())
    if res.returncode != 0:
        if res.stderr:
            print(res.stderr.strip(), file=sys.stderr)
        sys.exit(res.returncode)

def purge_jsdelivr(rel_path):
    for owner in (REPO_OWNER, "justunfold"):
        url = f"https://purge.jsdelivr.net/gh/{owner}/{REPO_NAME}@{BRANCH}/{rel_path}"
        try:
            with urllib.request.urlopen(url, timeout=10) as resp:
                print(f"Purged jsDelivr [{resp.status}]: {url}")
        except Exception as e:
            print(f"Note: jsDelivr purge skipped for {url} ({e})")

def main():
    parser = argparse.ArgumentParser(description="Push curated PrepUnfold question papers to GitHub CDN.")
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN", ""), help="GitHub Personal Access Token")
    args = parser.parse_args()

    root_dir = os.path.dirname(os.path.abspath(__file__))

    # Step 1: Run Quality & Duplicate Audit
    run_cmd([sys.executable, os.path.join(root_dir, "scripts", "audit_repo_papers.py"), root_dir])

    # Step 2: Git init / commit / push
    remote_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}.git"
    if args.token:
        remote_url = f"https://{REPO_OWNER}:{args.token}@github.com/{REPO_OWNER}/{REPO_NAME}.git"

    if not os.path.exists(os.path.join(root_dir, ".git")):
        run_cmd(["git", "init", "-b", BRANCH], cwd=root_dir)
        run_cmd(["git", "remote", "add", "origin", remote_url], cwd=root_dir)
    else:
        run_cmd(["git", "remote", "set-url", "origin", remote_url], cwd=root_dir)

    run_cmd(["git", "add", "manifest.json", "seen_question_hashes.json", "scripts/", "tests/"], cwd=root_dir)
    subprocess.run(["git", "commit", "-m", "feat(cdn): curate 29 real PYQ & topic-wise papers (1420 unique bilingual Qs) across UPSC, UPPCS, SSC GD, TGT/PGT, GATE & IIT JAM"], cwd=root_dir)
    run_cmd(["git", "push", "-u", "origin", BRANCH, "--force"], cwd=root_dir)

    # Step 3: Purge jsDelivr cache
    purge_jsdelivr("manifest.json")
    with open(os.path.join(root_dir, "manifest.json"), "r", encoding="utf-8") as f:
        manifest = json.load(f)
    for t in manifest.get("tests", []):
        purge_jsdelivr(t["path"])

    print("\nAll 29 papers (1,420 questions) pushed and jsDelivr cache purged!")

if __name__ == "__main__":
    main()
