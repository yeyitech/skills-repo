#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${SKILLS_REPO_URL:-https://github.com/yeyitech/skills-repo.git}"
BRANCH="${SKILLS_REPO_BRANCH:-main}"
CACHE_ROOT="${SKILLS_REPO_CACHE_DIR:-${XDG_CACHE_HOME:-$HOME/.cache}/yeyitech/skills-repo}"

mkdir -p "$(dirname "$CACHE_ROOT")"

if [ -d "$CACHE_ROOT/.git" ]; then
  echo "Updating cached repo at $CACHE_ROOT ..."
  git -C "$CACHE_ROOT" fetch origin "$BRANCH"
  git -C "$CACHE_ROOT" checkout "$BRANCH"
  git -C "$CACHE_ROOT" pull --ff-only origin "$BRANCH"
else
  echo "Cloning $REPO_URL ($BRANCH) into cache $CACHE_ROOT ..."
  rm -rf "$CACHE_ROOT"
  git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$CACHE_ROOT"
fi

echo "Installing skill(s) from cache ..."
python3 "$CACHE_ROOT/scripts/install_skill.py" --repo-dir "$CACHE_ROOT" "$@"
