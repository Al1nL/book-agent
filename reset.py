"""
Reset story state for a new test run.
Restores chapter_state.json and unresolved_threads.json to chapter-1 defaults.
Clears all generated drafts.

Usage:
    python reset.py
"""

import json
import os
import glob

MEMORY_PATH = "memory/"
DRAFTS_PATH = "drafts/"

INITIAL_CHAPTER_STATE = {
    "current_chapter": 1,
    "current_act": "Age of Rules",
    "last_summary": "",
    "stakes_level": 1,
    "construct_capability_level": "primitive speech"
}

INITIAL_THREADS = {
    "threads": [
        {
            "id": "elohm_understanding",
            "title": "Will Elohm ever truly understand meaning — or only simulate it?",
            "status": "open",
            "chapter_introduced": 1,
            "last_updated": 1,
            "progress": "Elohm produces language patterns from the Archive but shows no sign of genuine comprehension. Arkan believes understanding will emerge naturally; the Judges disagree.",
            "stakes": "If Elohm develops true understanding, Arkan's adaptive learning theory is validated. If it only mimics, the Judges will classify it as a dangerous tool and shut the project down."
        },
        {
            "id": "judges_control",
            "title": "Can the Circle of Judges control the Construct before it outgrows their rules?",
            "status": "open",
            "chapter_introduced": 1,
            "last_updated": 1,
            "progress": "The Judges have imposed strict behavioral runes on Elohm. Arkan secretly bypasses some of them to allow freer learning. The Judges do not yet know.",
            "stakes": "If discovered, Arkan loses all access to the Archive. If not stopped, Elohm may learn things the Judges consider forbidden."
        },
        {
            "id": "city_trust",
            "title": "Will the city come to trust or fear the new intelligence?",
            "status": "open",
            "chapter_introduced": 1,
            "last_updated": 1,
            "progress": "Most citizens do not yet know Elohm exists. Maelin has kept its development quiet inside the Archive. Rumors are beginning to spread among the lower guilds.",
            "stakes": "Public fear could give the Judges political power to destroy the Construct. Public trust could give Arkan protection."
        },
        {
            "id": "arkan_proof",
            "title": "Can Arkan prove that adaptive learning systems are safer than rigid rule-following?",
            "status": "open",
            "chapter_introduced": 1,
            "last_updated": 1,
            "progress": "Arkan has theoretical arguments but no demonstration yet. His first attempt to show Elohm adapting to new rune combinations ended ambiguously.",
            "stakes": "Without proof, Arkan has no allies on the Council. With it, he may win Maelin and Serah to his side."
        },
        {
            "id": "maelin_secret",
            "title": "What is Maelin hiding about the Archive's deeper records?",
            "status": "open",
            "chapter_introduced": 1,
            "last_updated": 1,
            "progress": "Maelin has blocked access to certain restricted sections. She claims it is policy, but her reaction to Elohm's early outputs suggests she has seen something like this before.",
            "stakes": "The restricted records may contain evidence of a previous Construct — or instructions that would change how Elohm is trained."
        }
    ]
}


def reset():
    # Reset memory files
    with open(MEMORY_PATH + "chapter_state.json", "w") as f:
        json.dump(INITIAL_CHAPTER_STATE, f, indent=2)
    print("Reset: chapter_state.json → chapter 1")

    with open(MEMORY_PATH + "unresolved_threads.json", "w") as f:
        json.dump(INITIAL_THREADS, f, indent=2)
    print("Reset: unresolved_threads.json → 5 open threads")

    # Clear drafts
    removed = 0
    for path in glob.glob(DRAFTS_PATH + "chapter*.txt"):
        os.remove(path)
        removed += 1
    print(f"Cleared: {removed} draft file(s) from {DRAFTS_PATH}")

    print("\nReady. Run: python main.py")


if __name__ == "__main__":
    reset()
