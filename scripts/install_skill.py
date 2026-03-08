#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_URL = "https://github.com/yeyitech/skills-repo.git"
DEFAULT_BRANCH = "main"
COMMON_TARGETS = [
    Path.home() / ".agents" / "skills",
    Path.home() / ".codex" / "skills",
    Path.home() / ".claude" / "skills",
    Path.home() / ".config" / "claude" / "skills",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install one or more skills from this repository into common local skill directories."
    )
    parser.add_argument("--skill", action="append", default=[], help="Skill name to install. Repeat for multiple skills.")
    parser.add_argument("--all", action="store_true", help="Install all skills found in the repository.")
    parser.add_argument("--target", action="append", default=[], help="Explicit target skill directory. Repeat for multiple targets.")
    parser.add_argument("--repo-dir", type=Path, default=None, help="Use an existing local skills-repo checkout as the source.")
    parser.add_argument("--repo-url", default=REPO_URL, help="Git repository to clone when --repo-dir is not provided.")
    parser.add_argument("--branch", default=DEFAULT_BRANCH, help="Branch to clone when --repo-dir is not provided.")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing installed skill directory.")
    parser.add_argument("--list", action="store_true", help="List available skills and exit.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without copying files.")
    return parser.parse_args()


def is_skill_dir(path: Path) -> bool:
    return path.is_dir() and (path / "SKILL.md").is_file()


def find_local_repo_root(hint: Path | None = None) -> Path | None:
    candidates = []
    if hint is not None:
        candidates.append(hint.expanduser().resolve())
    try:
        candidates.append(Path(__file__).resolve().parents[1])
    except Exception:
        pass

    for candidate in candidates:
        if candidate.is_dir() and any(is_skill_dir(child) for child in candidate.iterdir()):
            return candidate
    return None


def clone_repo(repo_url: str, branch: str) -> Path:
    temp_dir = Path(tempfile.mkdtemp(prefix="skills-repo-install-"))
    subprocess.run(
        ["git", "clone", "--depth", "1", "--branch", branch, repo_url, str(temp_dir)],
        check=True,
    )
    return temp_dir


def resolve_repo_root(args: argparse.Namespace) -> tuple[Path, bool]:
    local_repo = find_local_repo_root(args.repo_dir)
    if local_repo is not None:
        return local_repo, False
    return clone_repo(args.repo_url, args.branch), True


def available_skills(repo_root: Path) -> list[str]:
    return sorted(child.name for child in repo_root.iterdir() if is_skill_dir(child))


def resolve_requested_skills(args: argparse.Namespace, repo_root: Path) -> list[str]:
    skills = available_skills(repo_root)
    if args.list:
        for skill in skills:
            print(skill)
        sys.exit(0)
    if args.all:
        return skills
    if args.skill:
        missing = [skill for skill in args.skill if skill not in skills]
        if missing:
            raise SystemExit(f"Unknown skill(s): {', '.join(missing)}. Available: {', '.join(skills)}")
        return args.skill
    raise SystemExit("Pass --skill <name> or --all. Use --list to inspect available skills.")


def detect_targets(explicit_targets: list[str]) -> list[Path]:
    if explicit_targets:
        return [Path(target).expanduser().resolve() for target in explicit_targets]

    existing = [target for target in COMMON_TARGETS if target.exists()]
    if existing:
        return existing

    return [COMMON_TARGETS[0]]


def install_skill(repo_root: Path, skill_name: str, target_root: Path, force: bool, dry_run: bool) -> None:
    source_dir = repo_root / skill_name
    destination_dir = target_root / skill_name

    if not source_dir.exists():
        raise FileNotFoundError(f"Skill source not found: {source_dir}")

    if destination_dir.exists() and not force:
        print(f"skip  {destination_dir} (already exists; use --force to overwrite)")
        return

    print(f"copy  {source_dir} -> {destination_dir}")
    if dry_run:
        return

    target_root.mkdir(parents=True, exist_ok=True)
    if destination_dir.exists():
        shutil.rmtree(destination_dir)
    shutil.copytree(source_dir, destination_dir)


def main() -> None:
    args = parse_args()
    repo_root, is_temp_clone = resolve_repo_root(args)
    try:
        selected_skills = resolve_requested_skills(args, repo_root)
        targets = detect_targets(args.target)

        print(f"repo   {repo_root}")
        for target in targets:
            print(f"target {target}")
        print("---")

        for skill_name in selected_skills:
            for target in targets:
                install_skill(repo_root, skill_name, target, args.force, args.dry_run)

        if not args.dry_run:
            print("---")
            print("done")
    finally:
        if is_temp_clone:
            shutil.rmtree(repo_root, ignore_errors=True)


if __name__ == "__main__":
    main()
