# Repository Instructions

## Scope

- This repository is the source for the `spring-storage-analyzer` agent skill.
- `SKILL.md` is the behavior contract for the skill. Keep scripts, references, and README aligned with it.
- `CLAUDE.md` and `GEMINI.md` are symlinks to this file so Claude Code, Gemini CLI, Codex, and other tools read the same project rules.

## Runtime Boundary

- Do not make this skill resident or background-running.
- Do not add LaunchAgent, cron, shell startup hooks, watchers, auto-start services, or persistent daemons.
- Run `scripts/server.py` only when the user explicitly asks to scan storage, open the report, or perform cleanup.
- Scanning must remain read-only. Cleanup actions must remain user-triggered through guarded report actions or explicit user-confirmed commands.

## Development Checks

- After code changes, run `python3 -m unittest discover -v`.
- After script changes, run `python3 -m py_compile scripts/*.py`.
- Before committing, run `git diff --check` and remove generated caches such as `__pycache__/`.
