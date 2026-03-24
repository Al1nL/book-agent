from engine.llm_client import ask_llm
from engine.memory_manager import load_memory, load_prompt


def detect_drift(chapter_text):

    characters = load_memory("characters.json")
    themes = load_memory("themes.json")
    threads = load_memory("unresolved_threads.json")

    template = load_prompt("drift_analysis.txt")
    prompt = template.format(characters=characters, themes=themes, threads=threads, chapter_text=chapter_text)

    return ask_llm(prompt)