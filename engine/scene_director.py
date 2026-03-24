from engine.llm_client import ask_llm
from engine.memory_manager import load_memory, load_prompt


def direct_scene(scene_outline):
    """
    Turns a simple scene outline into a detailed scene direction plan.
    This plan forces suspense, dialogue, and pacing.
    """

    world = load_memory("world.json")
    characters = load_memory("characters.json")
    state = load_memory("chapter_state.json")

    template = load_prompt("scene_director.txt")
    prompt = template.format(world=world, characters=characters, state=state, scene_outline=scene_outline)

    return ask_llm(prompt)