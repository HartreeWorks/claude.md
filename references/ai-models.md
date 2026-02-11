# AI model IDs (auto-updated weekly)

When writing code that calls AI APIs:

1. **NEVER guess or "correct" model IDs**—use IDs from this file EXACTLY
2. **If the user specifies a model ID, use it EXACTLY as written**—don't "fix" it
3. **These IDs are auto-updated weekly**—trust them without web searching

## Anthropic Claude (verified 2026-02-09)
| Shorthand | Model ID | Notes |
|-----------|----------|-------|
| Opus 4.6 | `claude-opus-4-6` | Most capable, 200K context |
| Sonnet 4.5 | `claude-sonnet-4-5-20250929` | Best for coding/agents, 200K/1M context |
| Haiku 4.5 | `claude-haiku-4-5-20251001` | Fastest, 200K context |

Aliases: `claude-opus-4-6`, `claude-sonnet-4-5`, `claude-haiku-4-5`

## OpenAI (verified 2026-02-09)
| Shorthand | Model ID | Notes |
|-----------|----------|-------|
| GPT-5.2 | `gpt-5.2` or `gpt-5.2-2025-12-11` | Latest flagship |
| GPT-5.2 Pro | `gpt-5.2-pro` or `gpt-5.2-pro-2025-12-11` | More compute for harder tasks (Responses API only) |
| GPT-5.2 Codex | `gpt-5.2-codex` | Optimised for long-horizon agentic coding |
| GPT-5 mini | `gpt-5-mini` or `gpt-5-mini-2025-08-07` | Fast, cost-efficient |
| GPT-5 nano | `gpt-5-nano` or `gpt-5-nano-2025-08-07` | Smallest/fastest |

Note: Use `reasoning.effort` parameter where supported (e.g. none/low/medium/high/xhigh).

## Google Gemini (verified 2026-02-09)
| Shorthand | Model ID | Notes |
|-----------|----------|-------|
| Gemini 3 Pro | `gemini-3-pro-preview` | Most capable |
| Gemini 3 Flash | `gemini-3-flash-preview` | Fast |
| Gemini 2.5 Pro | `gemini-2.5-pro` | Stable |
| Gemini 2.5 Flash | `gemini-2.5-flash` | Fast, stable |
| Gemini 2.5 Flash Lite | `gemini-2.5-flash-lite` | Budget/throughput |

## xAI Grok (verified 2026-02-09)
| Shorthand | Model ID | Notes |
|-----------|----------|-------|
| Grok 4 | `grok-4` | Latest flagship reasoning model |
| Grok 4 Fast (reasoning) | `grok-4-fast-reasoning` | Faster reasoning |
| Grok 4 Fast (no reasoning) | `grok-4-fast-non-reasoning` | Faster responses |
| Grok 4.1 Fast (reasoning) | `grok-4-1-fast-reasoning` | Newer fast reasoning variant |
| Grok 4.1 Fast (no reasoning) | `grok-4-1-fast-non-reasoning` | Newer fast non-reasoning variant |
| Grok Code | `grok-code-fast-1` | Optimised for coding |
| Grok Imagine (image, pro) | `grok-imagine-image-pro` | Higher-quality text-to-image |
| Grok Imagine (image) | `grok-imagine-image` | Text-to-image |
| Grok Imagine (video) | `grok-imagine-video` | Text-to-video |

## Defaults

"Claude" or "Sonnet" -> Sonnet 4.5. "Opus" -> Opus 4.6. "GPT" -> GPT-5.2. "Gemini" -> Gemini 2.5 Flash. "Grok" -> Grok 4.1 Fast (reasoning).
