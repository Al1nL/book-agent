import json
from config import MEMORY_PATH, PROMPTS_PATH


def load_memory(filename):

    with open(MEMORY_PATH + filename) as f:
        return json.load(f)


def save_memory(filename, data):

    with open(MEMORY_PATH + filename, "w") as f:
        json.dump(data, f, indent=2)


def load_prompt(filename):
    with open(PROMPTS_PATH + filename) as f:
        return f.read()


def update_chapter_state(summary):

    state = load_memory("chapter_state.json")

    state["last_summary"] = summary
    state["current_chapter"] += 1

    save_memory("chapter_state.json", state)