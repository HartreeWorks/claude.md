# CLAUDE.md example

A real-world `CLAUDE.md` configuration for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), lightly redacted for public sharing.

This is the setup I use daily across ~20 active projects. It's shared as-is—some parts are specific to my workflow, but most patterns should be adaptable.

## What's here

- **`CLAUDE.md`** — the main configuration file (lives at `~/.claude/CLAUDE.md`)
- **`references/ai-models.md`** — auto-updated model ID reference, so Claude never guesses wrong model IDs
- **`references/project-map.md`** — illustrative example of a project map (fictional names, real structure)
- **`references/dual-machine-setup.md`** — instructions for delegating work to a second Mac via Tailscale + Syncthing
- **`scripts/format-calendar.py`** — deterministic calendar formatting (because LLMs miscalculate days of the week)

## Patterns worth noting

- **Safety rules** — `trash` instead of `rm -rf` (enforced via a [hook](https://docs.anthropic.com/en/docs/claude-code/hooks)), ask-before-cloning policy
- **Communication style** — "push back on overcommitment", "don't add motivational padding"
- **Calendar date verification** — forces Claude to use `date` or a Python script rather than computing days of the week itself
- **AI model reference file** — avoids hallucinated model IDs when writing code that calls AI APIs
- **Project map** — gives Claude awareness of your full project landscape so it can find relevant code across repos
- **Cross-project references** — plans/reviews directory, MEMORY.md convention, blogging skills, alerts endpoint
- **Dual-machine delegation** — hard-won lessons about running Claude Code on a remote Mac via tmux + SSH

## Context

I'm [Peter Hartree](https://x.com/peterhartree), an independent consultant working on AI uplift for AI safety organisations. I use Claude Code extensively and have built a large collection of [skills](https://docs.anthropic.com/en/docs/claude-code/skills), [hooks](https://docs.anthropic.com/en/docs/claude-code/hooks), and [MCP integrations](https://docs.anthropic.com/en/docs/claude-code/mcp-servers) around it.
