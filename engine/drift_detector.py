from engine.llm_client import ask_llm
from engine.memory_manager import load_memory


def detect_drift(chapter_text):

    characters = load_memory("characters.json")
    themes = load_memory("themes.json")
    threads = load_memory("unresolved_threads.json")

    prompt = f"""
Analyze the chapter for story drift.

CHARACTERS:
{characters}

THEMES:
{themes}

UNRESOLVED THREADS:
{threads}

CHAPTER TEXT:
{chapter_text}

Check for:

1. character personality inconsistencies
2. dropped plot threads
3. theme violations
4. world rule violations

Return a drift score (0-10) and explanation.
"""

    return ask_llm(prompt)