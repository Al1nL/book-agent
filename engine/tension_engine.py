from engine.llm_client import ask_llm

def enhance_tension(scene_plan):

    prompt = f"""
Improve this scene plan to increase suspense.

Scene plan:
{scene_plan}

Add:
- more uncertainty
- hidden information
- conflicting character goals
- subtle danger signals

Return improved version.
"""

    return ask_llm(prompt)