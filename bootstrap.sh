#!/usr/bin/env bash
set -euo pipefail

INSTALL_BIN_DIR="${INSTALL_BIN_DIR:-$HOME/.local/bin}"
INSTALL_BIN_NAME="${INSTALL_BIN_NAME:-yeyitech-skills}"
TARGET="$INSTALL_BIN_DIR/$INSTALL_BIN_NAME"

mkdir -p "$INSTALL_BIN_DIR"

cat > "$TARGET" <<'EOF'
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

python3 "$CACHE_ROOT/scripts/install_skill.py" --repo-dir "$CACHE_ROOT" "$@"
EOF

chmod +x "$TARGET"

echo "Installed installer to: $TARGET"
echo
if [[ ":$PATH:" != *":$INSTALL_BIN_DIR:"* ]]; then
  echo "Add this to your shell profile if needed:"
  echo "  export PATH=\"$INSTALL_BIN_DIR:\$PATH\""
  echo
fi

echo "Then use it like:"
echo "  $INSTALL_BIN_NAME --list"
echo "  $INSTALL_BIN_NAME --skill generate-alipay-wechat-report"
echo "  $INSTALL_BIN_NAME --all"
