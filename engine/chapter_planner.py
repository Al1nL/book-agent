from engine.llm_client import ask_llm
from engine.memory_manager import load_memory


def plan_chapter():

    world = load_memory("world.json")
    characters = load_memory("characters.json")
    plot = load_memory("plot_structure.json")
    state = load_memory("chapter_state.json")

    prompt = f"""
You are a professional fantasy novelist.

WORLD:
{world}

CHARACTERS:
{characters}

PLOT STRUCTURE:
{plot}

CURRENT STORY STATE:
{state}

Design the next chapter.

Return:

1. chapter title
2. chapter purpose
3. main conflict
4. emotional shift
5. cliffhanger
6. 4-6 scene breakdown
"""

    return ask_llm(prompt)