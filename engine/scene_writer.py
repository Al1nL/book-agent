from engine.llm_client import ask_llm
from engine.memory_manager import load_memory


def write_scene(scene_plan):

    world = load_memory("world.json")
    characters = load_memory("characters.json")
    themes = load_memory("themes.json")

    prompt = f"""
You are writing a suspenseful steampunk novel scene.

WORLD:
{world}

CHARACTERS:
{characters}

THEMES:
{themes}

SCENE DIRECTION PLAN:
{scene_plan}

WRITING RULES:

• Write in short paragraphs (1–3 lines max)
• Alternate between:
  - description
  - action
  - dialogue
• Dialogue must be at least 40–50% of the scene
• Characters must interrupt, question, and react
• Every 2–3 paragraphs must increase tension
• Avoid long descriptive blocks

At least one character must:
- disagree
- challenge another character
- or hide something

Every scene must include:
- a question that is not answered
- a decision point
- a new problem introduced

CRITICAL:
Do NOT explain everything immediately.
Delay information to build suspense.

STYLE:
- use pauses (...)
- use broken dialogue
- use hesitation

Make the reader feel something is wrong before explaining it.
Write 1200–1600 words.
"""

    return ask_llm(prompt)