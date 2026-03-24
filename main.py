from engine.chapter_planner import plan_chapter
from engine.scene_writer import write_scene
from engine.memory_manager import update_chapter_state, load_memory
from engine.drift_detector import detect_drift
from engine.scene_director import direct_scene
from engine.tension_engine import enhance_tension
from engine.thread_updater import update_threads


def generate_chapter():

    state = load_memory("chapter_state.json")
    chapter_number = state.get("current_chapter", 1)

    print(f"Planning chapter {chapter_number}...")
    plan = plan_chapter()
    print("--- CHAPTER PLAN ---")
    print(plan)
    print("--------------------")

    scenes = plan.split("Scene")
    valid_scenes = [s for s in scenes if len(s.strip()) >= 10]
    print(f"Found {len(valid_scenes)} scene(s) to write.")

    chapter_text = ""

    for i, scene in enumerate(valid_scenes, 1):

        print(f"Directing scene {i}...")
        directed_scene = direct_scene(scene)

        print(f"Enhancing tension {i}...")
        directed_scene = enhance_tension(directed_scene)

        print(f"Writing scene {i}...")
        text = write_scene(directed_scene)
        print(f"Scene {i} written ({len(text.split())} words).")

        chapter_text += text + "\n\n"

    print("Checking drift...")
    drift = detect_drift(chapter_text)
    print(drift)

    print("Updating plot threads...")
    update_threads(chapter_text)

    summary = chapter_text[:500]
    update_chapter_state(summary)

    filename = f"drafts/chapter_{chapter_number:02d}.txt"
    with open(filename, "w") as f:
        f.write(chapter_text)

    # Keep chapter.txt as the latest for easy access
    with open("drafts/chapter.txt", "w") as f:
        f.write(chapter_text)

    print(f"Chapter {chapter_number} complete — saved to {filename}")


if __name__ == "__main__":
    generate_chapter()
