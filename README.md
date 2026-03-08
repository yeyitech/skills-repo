# skills-repo

This repository contains reusable skills.

## Install

This repo is meant to be easy to install into local skill runtimes such as Agents, Codex, or Claude.

这个仓库的目标是：让用户可以方便地把公开 GitHub 仓库里的 Skill 安装到本地可识别的 skills 目录中，例如 Agents、Codex、Claude 等运行时。

### Two-step install: install the installer first

### 两步安装：先安装安装器，再安装 Skill

If you want a persistent local command, install the installer once:

如果你希望后续反复安装、更新 Skill，都通过一个固定的本地命令来完成，推荐先安装安装器：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/bootstrap.sh)
```

This installs a local command here by default:

默认会安装一个本地命令到：

```bash
~/.local/bin/yeyitech-skills
```

Then you can use it anytime:

之后你就可以在任何时候直接执行：

```bash
yeyitech-skills --list
yeyitech-skills --skill generate-alipay-wechat-report
yeyitech-skills --all
```

The installer command will keep a local cache of the GitHub repo, update that cache when needed, then copy the selected skill into a recognized local skills directory.

这个安装器命令会自动：

1. 把仓库同步到本地缓存目录
2. 在需要时更新缓存
3. 把指定 Skill 复制到本地可识别的 skills 目录

### One-line install from GitHub

### 一条命令直接安装

Install one skill with `curl`. The installer will:

如果你只是想快速装一个 Skill，也可以直接用 `curl` 拉取安装脚本并立即执行。

安装脚本会：

1. fetch the installer script from GitHub
2. clone or update this repo into a local cache directory
3. copy the selected skill into a recognized local skills directory

Install one skill:

安装单个 Skill：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/install.sh) \
  --skill generate-alipay-wechat-report
```

Install all skills:

安装全部 Skill：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/install.sh) \
  --all
```

By default the repo cache lives at:

默认仓库缓存目录：

```bash
~/.cache/yeyitech/skills-repo
```

You can override it:

也可以自定义缓存目录：

```bash
SKILLS_REPO_CACHE_DIR=~/project/cache/skills-repo \
  bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/install.sh) \
  --skill generate-alipay-wechat-report
```

### Quick install from a local clone

### 从本地 clone 仓库后安装

Clone the repo, then install one skill:

如果你已经把仓库 clone 到本地，也可以直接调用本地安装器：

```bash
git clone https://github.com/yeyitech/skills-repo.git
cd skills-repo
python3 scripts/install_skill.py --skill generate-alipay-wechat-report
```

Install all skills:

安装全部 Skill：

```bash
python3 scripts/install_skill.py --all
```

List available skills:

查看可用 Skill：

```bash
python3 scripts/install_skill.py --list
```

Overwrite an existing installed skill:

覆盖已安装的同名 Skill：

```bash
python3 scripts/install_skill.py --skill generate-alipay-wechat-report --force
```

### Target directory behavior

### 目标目录规则

The installer scans these common local skill directories:

安装器会扫描这些常见的本地 skills 目录：

- `~/.agents/skills`
- `~/.codex/skills`
- `~/.claude/skills`
- `~/.config/claude/skills`

Behavior:

规则如下：

- If one or more of those directories already exist, the installer copies the selected skill(s) into all existing targets.
- If none exist, the installer creates `~/.agents/skills` and installs there by default.
- You can override the destination explicitly with `--target /custom/path/to/skills`.

### Install to a custom skills directory

### 安装到自定义目录

```bash
python3 scripts/install_skill.py \
  --skill generate-alipay-wechat-report \
  --target ~/.codex/skills
```

## Included

- `infographic-image/` - full skill source with `SKILL.md`, `references/`, and `scripts/`
- `infographic-image.skill` - packaged distributable artifact
- `agent-harness-engineering/` - full skill source for agent-first engineering scaffolding
- `agent-harness-engineering.skill` - packaged distributable artifact
- `generate-alipay-wechat-report/` - full skill source for native Alipay/WeChat bill analysis and HTML spending reports
- `generate-alipay-wechat-report.skill` - packaged distributable artifact

## Installer

- `scripts/install_skill.py` - installs one or more skills into common local skill directories

## Default behavior

The skill defaults to the white magnetic meeting-board handwritten style and uses `qwen-image-2.0-pro` for image generation.

## Built-in presets

- `default`
- `clean-editorial`
- `comic-story`
- `spatial-gallery`
- `frosted-whiteboard`

## Agent Harness Engineering

The `agent-harness-engineering` skill bootstraps a repository for agent-first software development.

It focuses on:

- keeping `AGENTS.md` short and router-like
- moving durable knowledge into `docs/agent/`
- progressive disclosure of context instead of giant prompts
- mechanical validation via `scripts/agent_repo_check.py`
- optional garbage-collection reporting via `scripts/agent_gc_report.py`
