from engine.chapter_planner import plan_chapter
from engine.scene_writer import write_scene
from engine.memory_manager import update_chapter_state
from engine.drift_detector import detect_drift
from engine.scene_director import direct_scene
from engine.tension_engine import enhance_tension
def generate_chapter():

    print("Planning chapter...")
    plan = plan_chapter()

    print(plan)

    scenes = plan.split("Scene")

    chapter_text = ""

    for scene in scenes:

        if len(scene.strip()) < 10:
            continue

        print("Directing scene...")
        directed_scene = direct_scene(scene)

        print("Enhancing tension...")
        directed_scene = enhance_tension(directed_scene)

        print("Writing scene...")
        text = write_scene(directed_scene)

        chapter_text += text + "\n\n"

    print("Checking drift...")
    drift = detect_drift(chapter_text)

    print(drift)

    summary = chapter_text[:500]

    update_chapter_state(summary)

    with open("drafts/chapter.txt", "w") as f:
        f.write(chapter_text)

    print("Chapter complete")


if __name__ == "__main__":
    generate_chapter()