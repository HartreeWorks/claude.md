# Dual-machine setup

I use two Macs that work together:

| Machine | Purpose | Hostname |
|---------|---------|----------|
| **MacBook Pro** | Primary work machine, day-to-day use | `mbp` |
| **Mac Mini** | Dedicated to running AI agents and heavy workloads | `mini` |

## Software differences

- **OpenClaw** is installed on the Mac Mini only (not on MacBook Pro). Use it for scheduling autonomous AI agent tasks on the Mini.

## Identifying which machine you're on

Run `hostname` — returns `mbp` or `mini`.

## Connectivity

- **Tailscale** connects both machines (works from home or remotely)
- **SSH:** `ssh mini` from MacBook reaches Mac Mini
- **Screen Sharing:** Available over Tailscale for GUI access

## Synced folders (via Syncthing)

All of these sync bidirectionally between both machines:

| Folder ID | Path | Notes |
|-----------|------|-------|
| `documents-projects` | `~/Documents/Projects` | All project files |
| `www` | `~/Documents/www` | Web projects (ignores videos, zips, `.next/cache`) |
| `REDACTED` | `~/.claude` | Skills, commands, settings, conversations—everything |
| `REDACTED` | `~/.dotfiles` | Shell config, gitconfig |

Projects and www sync via Syncthing, not Git. Both machines have identical paths—no need to push/pull.

## When running on Mac Mini

- Expect to be running long tasks (hours) autonomously
- Use `tmux` for persistent sessions—the user may disconnect and reconnect
- If you need to verify visual work, use browser control (Computer Use)
- When done with a major task, notify via the [REDACTED] endpoint

## Exposing dev servers via Tailscale

Either machine can expose a local dev server to the other using `tailscale serve`:

```bash
# Expose port 3000 (or any port)
tailscale serve --bg --set-path /3000 http://localhost:3000

# Check what's being served
tailscale serve status

# Stop serving a port
tailscale serve --remove /3000
```

Access from the other machine at `https://[hostname].[tailnet-domain]/[port]`.

Use this when you need the user to view your work without them pulling the code, or when testing cross-machine access.

## Setting up ad-hoc folder sync (Syncthing)

For projects that need to sync between machines:

```bash
# Syncthing CLI
ST="/opt/homebrew/opt/syncthing/bin/syncthing"

# On MacBook - add folder and share with Mini
$ST cli config folders add --id my-folder-id --label "My Folder" --path "/path/to/folder"
$ST cli config folders my-folder-id devices add --device-id "$MINI_DEVICE"

# On Mac Mini - create dir, add folder, share with MacBook
ssh mini "mkdir -p '/path/to/folder'"
ssh mini "$ST cli config folders add --id my-folder-id --label 'My Folder' --path '/path/to/folder'"
ssh mini "$ST cli config folders my-folder-id devices add --device-id $MBP_DEVICE"

# Verify
$ST cli config folders list
```

Use kebab-case folder IDs (e.g., `valmy-transcripts`). Sync starts automatically once both sides are configured.

## Switching between machines

**Always commit or stash WIP before switching machines.** Syncthing syncs files bidirectionally, so uncommitted changes on one machine will conflict with new changes on the other. This especially affects lock files (`yarn.lock`, `package-lock.json`) which get fully rewritten by package managers, but it applies to any modified file.

## Delegating a task to Mac Mini

### Known pitfalls

- **Non-interactive SSH doesn't load homebrew PATH.** Always export it explicitly in scripts: `export PATH="/opt/homebrew/bin:$PATH"`
- **`--dangerously-skip-permissions` fails in tmux.** The confirmation prompt requires a real TTY; after accepting, the session dies. Don't use it.
- **`claude -p` (print/headless mode) is single-turn only.** It won't execute tools or do multi-step work—useless for plans.
- **Piping stdin (heredoc) to `claude` kills the session.** Claude exits when stdin closes.

### Working approach

1. **Write the task prompt to a file** (e.g., `/tmp/task-prompt.md`) and `scp` it to the Mini
2. **Set up folder sync** (if needed) using Syncthing commands above
3. **Start Claude in tmux** (without `--dangerously-skip-permissions`):
   ```bash
   ssh mini "tmux new-session -d -s task-name 'export PATH=/opt/homebrew/bin:\$PATH; cd /path/to/project; claude'"
   ```
4. **Send the prompt via `tmux send-keys`:**
   ```bash
   ssh mini "tmux send-keys -t task-name 'Please execute this plan: /tmp/task-prompt.md' Enter"
   ```
5. **Tell the user to attach** to approve tool uses and confirm the initial prompt:
   ```bash
   ssh -t mini "tmux attach -t task-name"
   ```
6. **Detach:** `Ctrl+B` then `D`
7. **Check later:** `ssh -t mini "tmux attach -t task-name"`
