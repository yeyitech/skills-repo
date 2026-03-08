# skills-repo

This repository contains reusable skills.

## Included

- `infographic-image/` - full skill source with `SKILL.md`, `references/`, and `scripts/`
- `infographic-image.skill` - packaged distributable artifact
- `agent-harness-engineering/` - full skill source for agent-first engineering scaffolding
- `agent-harness-engineering.skill` - packaged distributable artifact

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
