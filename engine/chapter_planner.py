from engine.llm_client import ask_llm
from engine.memory_manager import load_memory, load_prompt


def plan_chapter():

    world = load_memory("world.json")
    characters = load_memory("characters.json")
    plot = load_memory("plot_structure.json")
    state = load_memory("chapter_state.json")

    template = load_prompt("chapter_planner.txt")
    prompt = template.format(world=world, characters=characters, plot=plot, state=state)

    return ask_llm(prompt)