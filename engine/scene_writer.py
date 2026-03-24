from engine.llm_client import ask_llm
from engine.memory_manager import load_memory, load_prompt


def write_scene(scene_plan):

    world = load_memory("world.json")
    characters = load_memory("characters.json")
    themes = load_memory("themes.json")
    state = load_memory("chapter_state.json")

    template = load_prompt("scene_writer.txt")
    prompt = template.format(world=world, characters=characters, themes=themes, state=state, scene_plan=scene_plan)

    return ask_llm(prompt)