# Agent Context

## Current Focus

Build a recurring research-brief workflow for monitoring selected topics while
preserving the user's preferred process and accepting less polish where that
keeps the work moving.

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
- No application code, scripts, brief templates, source lists, or automation
  workflow has been added yet.
- `AGENTS.md` defines collaboration rules for future agent work.
- This file is the durable project context for future sessions.

## Decisions

- Use `AGENT_CONTEXT.md` as the singular context filename.
- Keep the initial agent setup minimal: one root `AGENTS.md` and one root
  `AGENT_CONTEXT.md`.
- Do not invent a detailed brief format, topic list, source policy, or
  automation stack before the project direction is clearer.

## Blockers

- No blockers recorded.

## Next Actions

- Define the recurring brief's first topic or topic set.
- Decide the first output format: Markdown note, digest, issue-style brief,
  email-style brief, or another lightweight artifact.
- Decide whether research will be manual, scripted, or partly automated.
- Identify initial sources and freshness expectations for the first topic.

## Ideas to Revisit

- A reusable Markdown brief template.
- A simple source registry.
- A lightweight run log for each brief cycle.
- Scripted source collection or summarization once the manual workflow is clear.
- Optional automation for scheduled brief generation.
