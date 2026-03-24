from engine.llm_client import ask_llm
from engine.memory_manager import load_prompt


def enhance_tension(scene_plan):

    template = load_prompt("tension_engine.txt")
    prompt = template.format(scene_plan=scene_plan)

    return ask_llm(prompt)