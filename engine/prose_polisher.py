from engine.llm_client import ask_llm
from engine.memory_manager import load_prompt


def polish_prose(chapter_text):
    """Run the critic → rewrite pipeline on a full chapter draft."""

    critic_template = load_prompt("critic.txt")
    critic_prompt = critic_template.format(chapter_text=chapter_text)

    print("Running critic pass...")
    feedback = ask_llm(critic_prompt)
    print("--- CRITIC FEEDBACK ---")
    print(feedback)
    print("-----------------------")

    rewrite_template = load_prompt("rewrite.txt")
    rewrite_prompt = rewrite_template.format(draft=chapter_text, feedback=feedback)

    print("Running rewrite pass...")
    polished = ask_llm(rewrite_prompt)

    return polished
