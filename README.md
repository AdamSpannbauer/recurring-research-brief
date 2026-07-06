# Recurring research brief 🔁📜🔍🔁

A quick-and-dirty recurring research brief workflow.

The goal is not a polished newsletter system. The goal is to monitor research
topics, keep enough memory to avoid repeated items, save inspectable artifacts,
and push a useful highlights message to Discord.

## How It Works

- `prompts/research_brief.md` defines the research interests, output format, duplicate-suppression rules, and Discord highlights section.
- `scripts/research_brief.py` reads the prompt and prior history, calls the OpenAI Responses API with hosted web search, writes brief artifacts, updates history, and posts Discord highlights when configured.
- `history/items.jsonl` stores delivered-item memory. This is the anti-repeat layer.
- `briefs/YYYY-MM-DD.md` stores the full generated Markdown brief.
- `runs/YYYY-MM-DD/brief.md` stores the generated run output.
- `.github/workflows/research-brief.yml` runs the workflow manually or on a weekday schedule.

Discord gets a compact highlights message and a link to the full Markdown brief. The Markdown file is the canonical output.

## Make It Your Own

1. Fork or copy the repo.
2. Edit `prompts/research_brief.md` for your topics, venues, and output taste.
3. Add GitHub Actions repository secrets:
   - `OPENAI_API_KEY`
   - `DISCORD_WEBHOOK_URL`
4. Adjust the schedule in `.github/workflows/research-brief.yml`.
5. Clear `history/items.jsonl` if you want a fresh baseline.
6. Run the workflow manually before trusting the schedule.

The current schedule is Monday-Friday at `0 12 * * 1-5`, which is about 8 AM Eastern during daylight time and 7 AM Eastern during standard time.

## Local Runs

Create a local `.env` file:

```text
OPENAI_API_KEY=...
DISCORD_WEBHOOK_URL=...
```

Generate without Discord:

```bash
python3 scripts/research_brief.py --no-discord
```

Generate and post Discord highlights:

```bash
python3 scripts/research_brief.py
```

## Notes

- History is intentionally plain JSONL, not a database.
- The script is intentionally one file and stdlib-only.
- Same-date reruns overwrite `briefs/YYYY-MM-DD.md` and `runs/YYYY-MM-DD/brief.md`; git history preserves prior versions.
- If the Discord highlights section cannot be parsed, the script still posts a link to the full brief when the brief file exists.

## AI Disclosure

This project was created with a heavy dose of Codex using GPT-5.5. AI authorship touched all parts of the project, including code, prompts, workflow configuration, documentation, and generated research-brief artifacts.
