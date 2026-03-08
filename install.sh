#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${SKILLS_REPO_URL:-https://github.com/yeyitech/skills-repo.git}"
BRANCH="${SKILLS_REPO_BRANCH:-main}"

TMPDIR="$(mktemp -d 2>/dev/null || mktemp -d -t skills-repo-install)"
cleanup() {
  rm -rf "$TMPDIR"
}
trap cleanup EXIT

echo "Cloning $REPO_URL ($BRANCH)..."
git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$TMPDIR/repo"
echo "Installing skill(s)..."
python3 "$TMPDIR/repo/scripts/install_skill.py" "$@"
