# spring-storage-analyzer

SpingWang's storage cleanup skill for macOS and Windows. It scans disk usage, separates safe caches from user data, and generates an interactive local HTML report with guarded cleanup actions.

## What It Does

- Scans common storage hot spots on macOS and Windows.
- Classifies findings into green, yellow, and red cleanup tiers.
- Generates an HTML report with disk overview, top space users, prioritized cleanup suggestions, and copyable commands.
- Can run a local `127.0.0.1` report server for user-triggered cleanup buttons.

## Safety Model

- The scan phase is read-only.
- Static reports never delete files.
- Local cleanup buttons require a random token, Host validation, path allowlists, and a browser confirmation dialog.
- `rm` and Trash actions are restricted to allowlisted paths under the user's home directory.
- Application folders outside the home directory can only be opened for manual review or uninstall.

## Install

Ask a skill-aware agent to install:

```text
Install this skill: https://github.com/xspring1982/spring-storage-analyzer
```

## Usage

Say things like:

```text
帮我看看存储
C 盘满了
清理一下磁盘
storage analysis
```

The agent should run the scan, analyze `/tmp/storage_scan.json`, create an analysis JSON, and open the report with:

```bash
python3 scripts/server.py /tmp/storage_analysis.json
```

Use the static report mode only when you want a read-only file:

```bash
python3 scripts/build_report.py /tmp/storage_analysis.json ~/Desktop/storage-report.html
```

## Attribution

This repository is based on the MIT-licensed `storage-analyzer` skill from [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills/tree/main/storage-analyzer). This fork is maintained and adjusted by SpingWang.
