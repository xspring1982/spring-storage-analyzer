# 💽 spring-storage-analyzer

SpingWang 维护的 Mac / Windows 存储空间分析与电脑垃圾清理 skill。它会扫描磁盘占用，把可安全清理的缓存和需要人工判断的用户数据分开，并生成带安全护栏的本地 HTML 清理报告。

SpingWang's storage cleanup skill for macOS and Windows. It scans disk usage, separates safe caches from user data, and generates an interactive local HTML report with guarded cleanup actions.

## 📦 安装方式 / Install

在 Claude Code、Codex、OpenClaw 等支持 Skill 的 Agent 里，直接说：

In any agent that supports Skills, say:

```text
帮我安装这个 skill: https://github.com/xspring1982/spring-storage-analyzer
```

或者用英文：

Or in English:

```text
Install this skill: https://github.com/xspring1982/spring-storage-analyzer
```

Agent 会自己 clone 到对应目录，不用你关心路径。安装后重启对应 AI 工具，让它重新加载 skill 列表。

The agent will clone it into the right skill directory. Restart the AI tool after installation so it reloads the skill list.

## ✨ 快速使用 / Quick Use

安装后，直接用一句自然语言触发：

After installation, trigger it with one natural-language request:

```text
帮我看看存储
C 盘满了
清理一下磁盘
看下电脑空间
storage analysis
clean up disk
```

它会按这个流程工作：

It works in this order:

1. 🔍 **只读扫描**：先扫描常见大目录和缓存位置，不删除、不移动、不改权限。<br>
   **Read-only scan**: scans common large directories and cache locations without deleting, moving, or changing permissions.
2. 📊 **生成报告**：在浏览器里打开交互式 HTML 报告，展示磁盘总览、占用 Top 5 和优先建议。<br>
   **Report**: opens an interactive HTML report with disk overview, top space users, and prioritized actions.
3. 🟢🟡🔴 **三色分级**：绿灯是可再生缓存；黄灯需要你判断；红灯只给正规卸载或保留建议。<br>
   **Three tiers**: green means regenerable cache; yellow needs your judgment; red means use official uninstall paths or keep it.
4. 🖱️ **手动确认清理**：需要清理时，必须由你在本地网页按钮上点击并二次确认。<br>
   **User-confirmed cleanup**: cleanup only runs after you click a local report button and confirm it.

## 🧰 功能 / What It Does

- 扫描 macOS 和 Windows 上常见的存储占用热点。<br>
  Scans common storage hot spots on macOS and Windows.
- 把结果分成绿灯、黄灯、红灯三类清理决策。<br>
  Classifies findings into green, yellow, and red cleanup tiers.
- 生成 HTML 报告，包含磁盘总览、占用 Top 5、优先清理建议和可复制命令。<br>
  Generates an HTML report with disk overview, top space users, prioritized cleanup suggestions, and copyable commands.
- 可启动本地 `127.0.0.1` 报告服务，让用户在网页上触发带确认的清理动作。<br>
  Can run a local `127.0.0.1` report server for user-triggered cleanup buttons.

## 🔒 安全模型 / Safety Model

- 扫描阶段只读，不删除、不移动、不改权限。<br>
  The scan phase is read-only. It does not delete, move, or change permissions.
- 静态报告不会删除文件，只展示建议和命令。<br>
  Static reports never delete files; they only show suggestions and commands.
- 本地清理按钮需要随机 token、Host 校验、路径白名单和浏览器二次确认。<br>
  Local cleanup buttons require a random token, Host validation, path allowlists, and a browser confirmation dialog.
- `rm` 和移到废纸篓动作只允许处理用户主目录内的白名单路径。<br>
  `rm` and Trash actions are restricted to allowlisted paths under the user's home directory.
- 用户主目录外的应用目录只能打开给用户手动审查或卸载，不能由网页接口删除。<br>
  Application folders outside the home directory can only be opened for manual review or uninstall.
- 这个 skill 不会常驻运行；`scripts/server.py` 只有在用户明确要求打开报告或清理时才启动，用完按 `Ctrl+C` 停止。<br>
  This skill does not run as a resident service. `scripts/server.py` starts only when the user explicitly asks to open a report or clean storage; stop it with `Ctrl+C` when finished.

## 🧪 手动运行 / Manual Run

通常不需要手动跑脚本，交给 Agent 处理即可。如果你要自己调试：

You normally do not need to run scripts manually; let the agent handle them. For debugging:

```bash
python3 scripts/scan.py > /tmp/storage_scan.json
python3 scripts/server.py /tmp/storage_analysis.json
```

只想要一份可保存、可分享的只读 HTML 文件时，用静态报告模式：

Use static report mode only when you want a read-only HTML file:

```bash
python3 scripts/build_report.py /tmp/storage_analysis.json ~/Desktop/storage-report.html
```

## ✅ 适合什么场景 / Good For

- 电脑空间不够，想知道到底是什么占了硬盘。<br>
  When your computer is running out of disk space and you need to know what is using it.
- 想清缓存，但不想误删聊天记录、项目代码、离线视频或应用数据。<br>
  When you want to clean caches without accidentally deleting chats, code projects, offline videos, or app data.
- 想要一份比普通磁盘工具更可解释的清理建议。<br>
  When you want cleanup advice that explains what each item is and what deletion would affect.

## 🚫 不适合什么场景 / Not For

- 查看运行内存 / RAM 占用。<br>
  Inspecting RAM or process memory usage.
- 自动接管整机清理。所有删除动作都必须由用户确认。<br>
  Fully automated cleanup. Every destructive action must be confirmed by the user.
- 替代 Time Machine、系统备份或专业数据恢复工具。<br>
  Replacing backups, Time Machine, or professional data recovery tools.

## 📄 授权与来源 / Attribution

本仓库基于 [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills/tree/main/storage-analyzer) 中 MIT 许可证的 `storage-analyzer` skill，并由 SpingWang 维护和调整。

This repository is based on the MIT-licensed `storage-analyzer` skill from [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills/tree/main/storage-analyzer). This fork is maintained and adjusted by SpingWang.
