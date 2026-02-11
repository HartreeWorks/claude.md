_This is an illustrative example showing the structure of my project map. Real project names and paths have been replaced with fictional examples._

# Project map

Last updated: 2026-02-11

## Client work

- **Acme Corp consulting** — `~/Documents/Projects/2025-09-acme-consulting`
  AI consulting engagement. Sprints combining tool development with strategic assessment.

- **BigCo Advisory** — `~/Documents/Projects/2026-01-bigco-advisory`
  External advisor. Strategy, AI uplift, mentoring. 5–10 hrs/month.

- **Coaching (Joe Blogs)** — `~/Documents/Projects/coaching-jamie`
  Senior grantmaker at BigPhil.

- **Coaching (Jane Doe)** — `~/Documents/Projects/coaching-sam`
  Director of The Center For Something Important. Long-term strategy, execution, psychology.

## Core business

- **Main Blog** — `~/Documents/Projects/blog` (strategy) + `~/Documents/www/blog` (website)
  Blog, newsletter, and coaching product.
  - Website: Next.js 15, port 3101
- **Audio Platform** — `~/Documents/www/audio-platform`
  AI-narrated audio content platform. Large ecosystem (15+ repos).
  - Core API: `~/Documents/www/audio-platform/_repos/api` (Vercel serverless, port 3003)
  - Player embed: `~/Documents/www/audio-platform/_repos/embed`
  - Feeds: `~/Documents/www/audio-platform/_repos/feeds`
  - Related skills: `fix-narration`, `invoice-clients`
- **Central Hub** — `~/Documents/www/hub/hub.example.com` (main site) + `~/Documents/www/hub/clients.example.com` (client portal)
  Central API hub: audio transcription, AI summarisation, alerts system. Next.js 15, Supabase, port 4001.
  - Related skills: `xero-invoice`, `monthly-admin`, `curate-podcasts`, `chief-of-staff`
- **Monthly admin & invoicing** — orchestrated via skills: `monthly-admin`, `xero-invoice`, `toggl-report`, `invoice-clients`

## Products & extensions

### Browser extensions (`~/Documents/www/Browser extensions/`)

- **Gmail Productivity Tool** — `~/Documents/www/Browser extensions/Gmail Tool`
  Chrome extension + PHP API + marketing site. Commercial product.

- **Summariser** — `~/Documents/www/Browser extensions/Summariser`
  Chrome extension for AI article summarisation.

- **Meet Helper** — `~/Documents/www/Browser extensions/Meet Helper`
  Chrome extension: auto-switch Google accounts to join Meet calls.

## Content sites

- **Content Aggregator** — `~/Documents/www/aggregator`
  AI/tech content aggregation + Twitter/X integration. Next.js 14, port 3051.

## Tools & utilities

- **Tools** — `~/Documents/www/Tools`
  Raycast scripts.

- **Claude plugins** — `~/Documents/www/Claude plugins/plugins`
  MCP plugins for Claude Code.

## Planning & reviews

- **Plans and reviews** — `~/Documents/Projects/plans-and-reviews`
  - Quarter plans: `work/2026-Q1-outline.md`
  - Month plans: `work/month-plans/` (e.g. `2026-02-plan.md`)
  - Week plans: `work/week-plans/` (e.g. `2026-W07-plan.md`)

## Claude Code skills (with project links)

Skills live at `~/.claude/skills/`. Those with clear project relationships:

| Skill | Related project |
|-------|----------------|
| `gmail-tool` | Gmail productivity extension |
| `fix-narration` | Audio platform transforms |
| `invoice-clients` | Audio platform invoicing |
| `curate-podcasts` | Central hub (reads DB) |
| `xero-invoice` | Central hub (client config) |
| `monthly-admin` | Central hub + Xero + Toggl |
| `chief-of-staff` | Plans-and-reviews + projects.yaml |
| `chrome-webstore-upload` | Various browser extensions |
| `day-tracker` | `~/Documents/day-tracker` |

## Experiments (`~/Documents/www/_try/`)

Date-prefixed experiment folders. Recent:

- `2026-02-10-session-dashboard` — Session monitoring dashboard
- `2026-01-30-multi-model-app` — Desktop app: query multiple AI models

Older experiments are in the same folder but not listed here.
