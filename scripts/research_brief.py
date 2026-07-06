#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import traceback
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = ROOT / "prompts" / "research_brief.md"
HISTORY_PATH = ROOT / "history" / "items.jsonl"
RUNS_DIR = ROOT / "runs"
BRIEFS_DIR = ROOT / "briefs"
OPENAI_RESPONSES_URL = "https://api.openai.com/v1/responses"
DEFAULT_MODEL = "gpt-5.5"
DISCORD_LIMIT = 2000


def load_dotenv() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def extract_fenced_block(text: str, label: str) -> str:
    pattern = rf"```{re.escape(label)}\s*\n(.*?)\n```"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_output_text(response: dict) -> str:
    if isinstance(response.get("output_text"), str):
        return response["output_text"]

    parts = []
    for item in response.get("output", []):
        for content in item.get("content", []):
            if isinstance(content.get("text"), str):
                parts.append(content["text"])

    if parts:
        return "\n".join(parts)

    raise RuntimeError(f"Could not find response text in OpenAI response:\n{json.dumps(response, indent=2)}")


def call_openai(model_input: str, model: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY.")

    body = {
        "model": model,
        "input": model_input,
        "tools": [{"type": "web_search"}],
        "tool_choice": "required",
    }
    request = urllib.request.Request(
        OPENAI_RESPONSES_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8")
        raise RuntimeError(f"OpenAI request failed with HTTP {exc.code}:\n{detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"OpenAI request failed: {exc}") from exc

    return extract_output_text(data)


def brief_link(brief_path: Path) -> str:
    base_url = os.environ.get("BRIEF_BASE_URL")
    if base_url:
        return f"{base_url.rstrip('/')}/{brief_path.relative_to(ROOT)}"
    return str(brief_path)


def ensure_brief_link(message: str, link: str) -> str:
    if link in message:
        return message
    return f"{message.rstrip()}\n\nFull brief: {link}"


def extract_discord_highlights(brief: str, brief_path: Path) -> str:
    link = brief_link(brief_path)
    heading = r"^#{2,3}\s+(?:Section\s+)?5:\s+Discord Highlights\s*$"
    match = re.search(heading, brief, flags=re.MULTILINE)
    if not match:
        return ensure_brief_link("Research brief generated.", link)

    rest = brief[match.end() :].strip()
    next_heading = re.search(r"^#{2,3}\s+", rest, flags=re.MULTILINE)
    message = rest[: next_heading.start()].strip() if next_heading else rest
    memory_block = message.find("```delivered_items_jsonl")
    if memory_block != -1:
        message = message[:memory_block].strip()
    message = message.replace(
        "Full brief: <link inserted by workflow>",
        f"Full brief: {link}",
    )
    message = message.replace(
        "Full brief: `<link inserted by workflow>`",
        f"Full brief: {link}",
    )
    message = ensure_brief_link(message, link)

    if len(message) <= DISCORD_LIMIT:
        return message

    suffix = "\n\n[truncated]"
    return message[: DISCORD_LIMIT - len(suffix)].rstrip() + suffix


def post_discord(message: str) -> None:
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("\nDISCORD_WEBHOOK_URL not set. Discord message:\n")
        print(message)
        return

    request = urllib.request.Request(
        webhook_url,
        data=json.dumps({"content": message}).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "recurring-research-brief/0.1",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30):
            return
    except urllib.error.HTTPError as exc:
        print(f"Discord post failed with HTTP {exc.code}:", file=sys.stderr)
        print(exc.read().decode("utf-8"), file=sys.stderr)
    except urllib.error.URLError as exc:
        print(f"Discord post failed: {exc}", file=sys.stderr)


def run(args: argparse.Namespace) -> None:
    if not PROMPT_PATH.exists():
        raise RuntimeError(f"Missing prompt file: {PROMPT_PATH}")

    prompt = PROMPT_PATH.read_text(encoding="utf-8")
    history = HISTORY_PATH.read_text(encoding="utf-8") if HISTORY_PATH.exists() else ""
    model_input = f"""Current date: {args.date}

{prompt}

Already Delivered History

{history.strip() if history.strip() else "(none)"}
"""

    if args.dry_run:
        print(model_input)
        return

    brief = call_openai(model_input, args.model)

    run_dir = RUNS_DIR / args.date
    run_dir.mkdir(parents=True, exist_ok=True)
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)

    run_brief_path = run_dir / "brief.md"
    brief_path = BRIEFS_DIR / f"{args.date}.md"
    run_brief_path.write_text(brief, encoding="utf-8")
    brief_path.write_text(brief, encoding="utf-8")

    delivered_items = extract_fenced_block(brief, "delivered_items_jsonl")
    if not delivered_items:
        raise RuntimeError("No delivered_items_jsonl block found; history not updated.")
    else:
        parsed_lines = []
        for line in delivered_items.splitlines():
            line = line.strip()
            if not line:
                continue
            json.loads(line)
            parsed_lines.append(line)

        if not parsed_lines:
            raise RuntimeError("delivered_items_jsonl block was empty; history not updated.")

        HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
        with HISTORY_PATH.open("a", encoding="utf-8") as history_file:
            for line in parsed_lines:
                history_file.write(line + "\n")

    if not args.no_discord:
        highlights = extract_discord_highlights(brief, brief_path)
        post_discord(highlights)

    print(f"Wrote {brief_path}")
    print(f"Wrote {run_brief_path}")


def notify_failure(run_date: str, message: str, no_discord: bool) -> None:
    failure_message = f"Research brief failed for {run_date}:\n\n{message}"
    if not no_discord:
        post_discord(failure_message)
    print(failure_message, file=sys.stderr)


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Generate a recurring research brief.")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", DEFAULT_MODEL))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-discord", action="store_true")
    args = parser.parse_args()

    try:
        run(args)
    except Exception as exc:
        notify_failure(args.date, traceback.format_exc(), args.no_discord)
        sys.exit(1)


if __name__ == "__main__":
    main()
