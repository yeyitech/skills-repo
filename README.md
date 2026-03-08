# skills-repo

This repository contains reusable skills.

## Install

This repo is meant to be easy to install into local skill runtimes such as Agents, Codex, or Claude.

### One-line install from GitHub

Install one skill without keeping a local clone:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/install.sh) \
  --skill generate-alipay-wechat-report
```

Install all skills:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/install.sh) \
  --all
```

### Quick install from a local clone

Clone the repo, then install one skill:

```bash
git clone https://github.com/yeyitech/skills-repo.git
cd skills-repo
python3 scripts/install_skill.py --skill generate-alipay-wechat-report
```

Install all skills:

```bash
python3 scripts/install_skill.py --all
```

List available skills:

```bash
python3 scripts/install_skill.py --list
```

Overwrite an existing installed skill:

```bash
python3 scripts/install_skill.py --skill generate-alipay-wechat-report --force
```

### Target directory behavior

The installer scans these common local skill directories:

- `~/.agents/skills`
- `~/.codex/skills`
- `~/.claude/skills`
- `~/.config/claude/skills`

Behavior:

- If one or more of those directories already exist, the installer copies the selected skill(s) into all existing targets.
- If none exist, the installer creates `~/.agents/skills` and installs there by default.
- You can override the destination explicitly with `--target /custom/path/to/skills`.

### Install to a custom skills directory

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
