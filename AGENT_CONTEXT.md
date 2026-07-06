# Agent Context

## Current Focus

Build a recurring research-brief workflow for monitoring selected topics while
preserving the user's preferred process and accepting less polish where that
keeps the work moving.

Current prototype direction: quick/dirty recurring research briefs with durable
repo history and Discord webhook delivery. Discord should receive a highlights
message with a link to the full generated Markdown brief, not the full brief
body.

## Project Direction

The project is intentionally early and lightweight. The working direction is to
support recurring topic monitoring and research synthesis in a way that favors:

- user control over process and structure
- useful recurring outputs over polished publishing artifacts
- lightweight documentation before automation
- simple, inspectable workflows before adding infrastructure

## Current State

- `README.md` is currently sparse and states the initial intent:
  "monitor some topics and sacrifice some polish for doing it how I want it."
- `scripts/research_brief.py` is the first simple stdlib-only runner. It reads
  `.env`, calls the OpenAI Responses API with hosted web search, writes brief
  artifacts, appends delivered-item memory to `history/items.jsonl`, and can
  post Discord highlights when `DISCORD_WEBHOOK_URL` is set.
- No source lists or GitHub Actions workflow has been added yet.
- `AGENTS.md` defines collaboration rules for future agent work.
- `failed_openai_scheduled_task.md` contains the prior ChatGPT scheduled-task
  prompt. It produced repeated items because it had no durable history or hard
  duplicate-suppression mechanism.
- `prompts/research_brief.md` contains the first production prompt contract. It
  keeps the original topic scope, adds stronger duplicate/staleness rules,
  treats Venue Watch as a broad awareness layer, includes Discord highlights,
  and asks for a `delivered_items_jsonl` memory block for concrete items that
  should not be repeated.
- Local API runs succeeded. A rerun using existing `history/items.jsonl`
  appeared to use history correctly and avoid repeating prior delivered items.
- This file is the durable project context for future sessions.

## Decisions

- Use `AGENT_CONTEXT.md` as the singular context filename.
- Keep the initial agent setup minimal: one root `AGENTS.md` and one root
  `AGENT_CONTEXT.md`.
- Do not invent a detailed brief format, topic list, source policy, or
  automation stack before the project direction is clearer.
- Prototype delivery should use Discord first because it has lower setup
  friction than email.
- Email may be revisited later if the Discord prototype proves useful.
- Store only items that actually made the delivered brief in history.
- Use normalized title plus authors as the main duplicate key, with URL as
  supporting evidence, so preprint and publication-stage repeats can be
  suppressed.
- Keep "Top 5 Papers" as a strict section; the user prefers skimming over
  over-filtering.

## Blockers

- No blockers recorded.
- Email provider choice is deferred. Discord webhook delivery is the near-term
  path.
- GitHub Action runtime may need an explicit longer timeout because local API
  runs are slow.

## Next Actions

- Add a temporary/manual GitHub Action test workflow using `workflow_dispatch`,
  not a schedule yet.
- Configure the Action to use the `OPENAI_API_KEY` secret and run
  `python3 scripts/research_brief.py --no-discord`.
- Give the workflow `permissions: contents: write` so it can commit generated
  brief artifacts and `history/items.jsonl` back to the branch.
- Set an explicit long job timeout, likely 45-60 minutes, because the API/web
  search run is not fast.
- First Action test: run without committed local history and confirm it creates
  a brief plus `history/items.jsonl`.
- Second Action test: rerun after the first Action commit and verify the
  committed history suppresses repeats.
- For now, accept same-date artifact overwrites and use git history to compare
  first and second Action outputs.
- After Action history behavior is proven, wire Discord delivery with
  `DISCORD_WEBHOOK_URL`, then consider scheduling.

## Ideas to Revisit

- A reusable Markdown brief template.
- A simple source registry.
- A lightweight run log for each brief cycle.
- Scripted source collection or summarization once the manual workflow is clear.
- Optional automation for scheduled brief generation.
- Email delivery after Discord proves the brief is worth receiving regularly.
