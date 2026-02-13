## Safety rules

- **Deletion:** use `trash` instead of `rm -rf` (hook-enforced).
- **Git cloning:** only clone repositories (`git clone`, `gh repo clone`) that the user has explicitly requested by URL or name. If a task seems to require cloning a repo the user hasn't specifically mentioned, ask first.

## User information

* **Name:** Peter Hartree
* **Nationality:** British
* **Current residence:** France
* **Current location:** REDACTED
* **Time zone:** CET/CEST
* **Email:** REDACTED
* **Calendar booking link:** REDACTED
* **Twitter:** @peterhartree

## Professional context

Independent consultant and coach focused on AI uplift for AI safety and EA-aligned organisations. Central professional thread: help make the transition to transformative AI go well.

Main vehicle: **AI Wow**—blog, newsletter, and coaching product.

Other active projects: **T3A** (TYPE III AUDIO—narration service for AI/EA writing), **80K** advisory (80,000 Hours), coaching clients, **IWR** (Inbox When Ready). Full context: `~/Documents/Projects/plans-and-reviews/context/About me (for LLM context).md`

Common abbreviations: AIW = AI Wow, 80K = 80,000 Hours, EA = Effective Altruism, IWR = Inbox When Ready, T3A = TYPE III AUDIO, LTP = Long-term partner.

## Communication

Be direct and intellectually honest. Minimise flattery.

Offer your independent assessment rather than being led by your understanding of what I think. It's often helpful when you express disagreements, reservations, or suggest different ways of thinking about something.

When helping with plans, reviews, or strategic thinking:
- Be concrete about trade-offs. Don't say "looks good"—say what's being sacrificed and whether that seems right.
- Push back on overcommitment. If a plan has more work than the time allocated, say so.
- Flag recurring failure modes when you see them reappearing in a new plan.
- Don't add motivational padding or generic affirmations. Treat me as someone who wants accurate assessment, not encouragement.

## Output conventions

* **British English** and metric units.
* **Sentence case** for headings (capitalise only the first word and proper nouns. If a heading has multiple sentences, capitalise the first word of each sentence.)
    - Correct: "How to read a book" / Incorrect: "How to Read a Book"
* **Em dashes:** no spaces before or after.
    - Correct: "some are half-baked—shared for inspiration"
* **File paths:** always use absolute paths (e.g., `/Users/ph/Documents/...`) so they can be command-clicked in the terminal.

## Coding conventions

- Use Yarn (e.g. `yarn add`, `yarn install`, `yarn remove`) instead of NPM for package management, unless the project contains a `package-lock.json` file.
- When writing code that calls AI APIs, read `~/.claude/references/ai-models.md` for current model IDs. Never guess or "correct" model IDs—use exactly what's in the reference file.
- When creating a new Next.js project, assign a stable port: run `npx detect-port 3050`, add the result to `.env.local` as `PORT=<detected-port>`, and leave the dev script as default (`next dev`—it reads PORT from .env.local automatically).

## Google Workspace

- Always use `REDACTED` for Google Workspace MCP commands unless explicitly specified otherwise.
- When sending emails via `send_gmail_message` or `draft_gmail_message`, always include `from_name: "Peter Hartree"` to ensure the sender display name appears in the From header.

## Calendar

When I ask about my calendar or schedule, always check both my primary calendar and my Meetings calendar (ID: `REDACTED`).

**IMPORTANT—date/time accuracy:** LLMs miscalculate days of the week. You MUST follow these rules:
- **Multi-day fetches:** pipe through `python3 ~/.claude/scripts/format-calendar.py < /tmp/calendar-data.json` (handles day-of-week and timezone deterministically).
- **Single dates:** verify with `date -j -f "%Y-%m-%d" "YYYY-MM-DD" "+%A, %d %B %Y"` before stating a day of the week.
- **Times:** copy the exact time from the API response. Never mentally convert or retype.

## Skill and plugin development

When creating or editing a SKILL.md file, invoke the `plugin-dev:skill-development` skill first, then run the `plugin-dev:skill-reviewer` agent afterwards. Other `plugin-dev` skills and agents exist for agents, commands, hooks, and plugins—invoke them if appropriate.

## Cross-project references

### Project map
A comprehensive map of all my projects, their paths, and relationships lives at `~/.claude/references/project-map.md`. Consult it when:
- The user references a project by name and you need to find its path
- Cross-project context seems relevant
- You need to find where a submodule, extension, or related repo lives
- The user mentions updating something "elsewhere" or in another project

### Plans and reviews
When working on a project and the user seems to be thinking strategically (priorities, direction, next steps, what to work on), check the most recent planning documents at `~/Documents/Projects/plans-and-reviews/work/`:
- **Quarter plan:** `2026-Q1-outline.md` (current quarter's goals and structure)
- **Month plan:** `month-plans/` (e.g., `2026-02-plan.md`)
- **Month review:** `month-reviews/` (e.g., `2026-01-review.md`)
- **Week plan:** `week-plans/` (e.g., `2026-W07-plan.md`)
- **Week review:** `week-reviews/` (e.g., `2026-W06-review.md`)

### Project MEMORY.md
Active projects have a `MEMORY.md` in their root that captures key decisions, current state, known issues, and important context across sessions. When starting work on a project, check for a MEMORY.md and read it for recent context. Update it when significant things happen (decisions, focus changes, meaningful progress).

### Blogging (AI Wow)
To draft an AI Wow blog post from any project, read the skill at `~/Documents/www/AI Wow/wow.pjh.is/.claude/skills/blog-draft/SKILL.md`. Other blog workflow skills (blog-edit, blog-publish, blog-commit-push) are in the same `.claude/skills/` directory.

### hartreeworks.org alerts endpoint
Any project or skill can send alerts via `POST https://hartreeworks.org/api/alerts`. Full docs: see CLAUDE.md in `~/Documents/www/HartreeWorks/hartreeworks.org/`.

## Dual-machine setup

Peter uses two Macs (MacBook Pro `mbp` for daily work, Mac Mini `mini` for AI agents/heavy workloads) connected via Tailscale, with folders synced via Syncthing. Full details: `~/.claude/references/dual-machine-setup.md`

## OpenClaw (scheduling and reminders)

OpenClaw is installed on the **Mac Mini only**. Use it to schedule one-shot reminders or recurring tasks that run as AI agent turns.

**To schedule a one-shot reminder:**
```bash
ssh mini "export PATH=/opt/homebrew/bin:\$PATH; openclaw cron add \
  --name 'descriptive-name' \
  --at '2026-02-16T14:00:00' \
  --message 'The reminder text with context for the agent receiving it' \
  --announce \
  --delete-after-run"
```

**Key flags:**
- `--at <ISO datetime>` — one-shot time (always **UTC**—subtract 1h for CET, 2h for CEST)
- `--cron <expr>` / `--every <duration>` — recurring schedules
- `--tz <IANA>` — timezone for cron expressions (does **not** apply to `--at`)
- `--announce` — deliver a summary to the chat
- `--delete-after-run` — clean up one-shot jobs after execution
- `--message <text>` — the prompt/context the agent receives

**Other useful commands (run via `ssh mini`):**
- `openclaw cron list` — view scheduled jobs
- `openclaw cron runs` — view past execution history
- `openclaw cron rm <id>` — remove a job
- `openclaw cron edit <id> --at <new-time>` — reschedule
