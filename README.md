# spring-storage-analyzer

SpingWang 维护的 Mac / Windows 存储空间分析与电脑垃圾清理 skill。它会扫描磁盘占用，把可安全清理的缓存和需要人工判断的用户数据分开，并生成带安全护栏的本地 HTML 清理报告。

SpingWang's storage cleanup skill for macOS and Windows. It scans disk usage, separates safe caches from user data, and generates an interactive local HTML report with guarded cleanup actions.

## 功能 / What It Does

- 扫描 macOS 和 Windows 上常见的存储占用热点。
  Scans common storage hot spots on macOS and Windows.
- 把结果分成绿灯、黄灯、红灯三类清理决策。
  Classifies findings into green, yellow, and red cleanup tiers.
- 生成 HTML 报告，包含磁盘总览、占用 Top 5、优先清理建议和可复制命令。
  Generates an HTML report with disk overview, top space users, prioritized cleanup suggestions, and copyable commands.
- 可启动本地 `127.0.0.1` 报告服务，让用户在网页上触发带确认的清理动作。
  Can run a local `127.0.0.1` report server for user-triggered cleanup buttons.

## 安全模型 / Safety Model

- 扫描阶段只读，不删除、不移动、不改权限。
  The scan phase is read-only. It does not delete, move, or change permissions.
- 静态报告不会删除文件，只展示建议和命令。
  Static reports never delete files; they only show suggestions and commands.
- 本地清理按钮需要随机 token、Host 校验、路径白名单和浏览器二次确认。
  Local cleanup buttons require a random token, Host validation, path allowlists, and a browser confirmation dialog.
- `rm` 和移到废纸篓动作只允许处理用户主目录内的白名单路径。
  `rm` and Trash actions are restricted to allowlisted paths under the user's home directory.
- 用户主目录外的应用目录只能打开给用户手动审查或卸载，不能由网页接口删除。
  Application folders outside the home directory can only be opened for manual review or uninstall.

## 安装 / Install

### 公开安装 / Public install

让支持 Skill 的 agent 安装这个仓库：

Ask a skill-aware agent to install this repository:

```text
Install this skill: https://github.com/xspring1982/spring-storage-analyzer
```

### 本机开发安装 / Local development install

在自己的电脑上维护这个仓库时，建议用符号链接安装，同一份源码同时给多个 AI 工具读取：

When maintaining this repository locally, install it with symlinks so multiple AI tools read the same source copy:

```bash
ln -s /Users/Wang/D盘/dev/skills/spring-storage-analyzer ~/.agents/skills/spring-storage-analyzer
ln -s ~/.agents/skills/spring-storage-analyzer ~/.codex/skills/spring-storage-analyzer
ln -s ~/.agents/skills/spring-storage-analyzer ~/.claude/skills/spring-storage-analyzer
```

这只是注册 skill，不会启动后台服务。`scripts/server.py` 只有在用户明确要求扫描、打开报告或清理时才运行；用完按 `Ctrl+C` 停止。

This only registers the skill; it does not start a background service. `scripts/server.py` runs only when the user explicitly asks to scan, open a report, or clean storage. Stop it with `Ctrl+C` when finished.

## 使用 / Usage

可以这样触发：

Say things like:

```text
帮我看看存储
C 盘满了
清理一下磁盘
看下电脑空间
storage analysis
clean up disk
```

agent 会运行扫描，分析 `/tmp/storage_scan.json`，生成 `/tmp/storage_analysis.json`，然后打开报告：

The agent should run the scan, analyze `/tmp/storage_scan.json`, create `/tmp/storage_analysis.json`, and open the report:

```bash
python3 scripts/server.py /tmp/storage_analysis.json
```

如果只想要一份可保存、可分享的只读 HTML 文件，用静态报告模式：

Use static report mode only when you want a read-only HTML file:

```bash
python3 scripts/build_report.py /tmp/storage_analysis.json ~/Desktop/storage-report.html
```

## 适合什么场景 / Good For

- 电脑空间不够，想知道到底是什么占了硬盘。
  When your computer is running out of disk space and you need to know what is using it.
- 想清缓存，但不想误删聊天记录、项目代码、离线视频或应用数据。
  When you want to clean caches without accidentally deleting chats, code projects, offline videos, or app data.
- 想要一份比普通磁盘工具更可解释的清理建议。
  When you want cleanup advice that explains what each item is and what deletion would affect.

## 不适合什么场景 / Not For

- 查看运行内存 / RAM 占用。
  Inspecting RAM or process memory usage.
- 自动接管整机清理。所有删除动作都必须由用户确认。
  Fully automated cleanup. Every destructive action must be confirmed by the user.
- 替代 Time Machine、系统备份或专业数据恢复工具。
  Replacing backups, Time Machine, or professional data recovery tools.

## 授权与来源 / Attribution

本仓库基于 [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills/tree/main/storage-analyzer) 中 MIT 许可证的 `storage-analyzer` skill，并由 SpingWang 维护和调整。

This repository is based on the MIT-licensed `storage-analyzer` skill from [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills/tree/main/storage-analyzer). This fork is maintained and adjusted by SpingWang.
