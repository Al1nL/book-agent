import json
import re
from engine.llm_client import ask_llm
from engine.memory_manager import load_memory, save_memory, load_prompt


def _extract_json(text):
    """Try multiple strategies to extract a JSON object from LLM output."""
    # Strategy 1: strip markdown fences
    cleaned = text.strip()
    if "```" in cleaned:
        parts = cleaned.split("```")
        for part in parts:
            if part.startswith("json"):
                part = part[4:]
            candidate = part.strip()
            if candidate.startswith("{"):
                cleaned = candidate
                break

    # Strategy 2: find the first { ... } block
    if not cleaned.startswith("{"):
        match = re.search(r'\{.*\}', cleaned, re.DOTALL)
        if match:
            cleaned = match.group(0)

    return json.loads(cleaned)


def update_threads(chapter_text):

    threads = load_memory("unresolved_threads.json")
    state = load_memory("chapter_state.json")
    chapter_number = state.get("current_chapter", 1)

    template = load_prompt("thread_updater.txt")
    prompt = template.format(
        threads=json.dumps(threads, indent=2),
        chapter_text=chapter_text,
        chapter_number=chapter_number
    )

    response = ask_llm(prompt)

    try:
        updated = _extract_json(response)
        save_memory("unresolved_threads.json", updated)
        print("Threads updated.")
        return updated
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Warning: thread update failed to parse JSON ({e}). Threads unchanged.")
        print(f"Raw response was: {response[:300]!r}")
        return threads
