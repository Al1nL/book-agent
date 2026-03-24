from engine.llm_client import ask_llm
from engine.memory_manager import load_memory


def direct_scene(scene_outline):
    """
    Turns a simple scene outline into a detailed scene direction plan.
    This plan forces suspense, dialogue, and pacing.
    """

    world = load_memory("world.json")
    characters = load_memory("characters.json")
    state = load_memory("chapter_state.json")

    prompt = f"""
You are a cinematic story director planning a suspenseful novel scene.

WORLD:
{world}

CHARACTERS:
{characters}

CURRENT STORY STATE:
{state}

SCENE OUTLINE:
{scene_outline}

Design the scene with strong dramatic structure.

OUTPUT:

1. OPENING HOOK
Start with unease or anomaly.

2. TENSION STEPS (5 steps)
Each step must increase danger or uncertainty.

3. CHARACTER CONFLICT
Force disagreement, suspicion, or emotional friction.

4. DIALOGUE PLAN
Write at least 10 dialogue beats:
- include interruptions
- include questions without answers
- include disagreement

5. MICRO-REACTIONS
List body language:
- hesitation
- glances
- pauses
- physical movement

6. TURNING POINT
Something unexpected happens or is revealed.

7. CLIFFHANGER
End with a question, danger, or unresolved action.

IMPORTANT:
- tension must escalate, not stay flat
- characters must react emotionally
"""

    return ask_llm(prompt)