# Book Agent — Project Guide for Claude

## What This Project Does

AI-assisted novel writing system that generates fantasy novel chapters using a **multi-stage LLM pipeline via Ollama** (local LLM server). Each chapter is produced by chaining specialized agents: planner → scene director → tension enhancer → prose writer → drift detector.

---

## Architecture

```
main.py
  └── generate_chapter()
        ├── plan_chapter()              → engine/chapter_planner.py
        ├── for each scene:
        │     ├── direct_scene()        → engine/scene_director.py
        │     ├── enhance_tension()     → engine/tension_engine.py
        │     └── write_scene()         → engine/scene_writer.py
        ├── polish_prose()              → engine/prose_polisher.py  (critic → rewrite pass)
        ├── detect_drift()              → engine/drift_detector.py
        └── update_chapter_state()      → engine/memory_manager.py
```

All LLM calls go through `engine/llm_client.py` → `POST http://localhost:11434/api/generate`.

### Engine Modules

| File | Class/Function | Role |
|------|---------------|------|
| `llm_client.py` | `ask_llm(prompt)` | Streams JSON from Ollama, aggregates text |
| `memory_manager.py` | `load_memory(f)` / `save_memory(f, d)` | Read/write JSON from `memory/` |
| `memory_manager.py` | `update_chapter_state(summary)` | Increments chapter counter, saves summary |
| `chapter_planner.py` | `plan_chapter()` | Loads world/characters/plot, prompts LLM for chapter design |
| `scene_director.py` | `direct_scene(outline)` | Designs dramatic structure for a scene |
| `scene_writer.py` | `write_scene(plan)` | Generates 1200–1600 word prose from scene plan |
| `tension_engine.py` | `enhance_tension(plan)` | Adds uncertainty, hidden info, conflict to scene plan |
| `drift_detector.py` | `detect_drift(text)` | Checks chapter for character/plot/theme consistency |
| `prose_polisher.py` | `polish_prose(text)` | Runs critic pass then full rewrite for style/atmosphere |

### Prompts (`prompts/`)

Each engine module loads a `.txt` prompt template. Key ones:
- `master_planner.txt` — novel blueprint
- `chapter_planner.txt` — chapter-level planning
- `scene_director.txt` — dramatic structure
- `scene_writer.txt` — prose generation rules (SJM/JKR style, mandatory atmospheric opening)
- `tension_engine.txt` — tension enhancement rules
- `drift_analysis.txt` — continuity checking
- `critic.txt` / `rewrite.txt` — critic→rewrite polish pipeline (wired into main.py via `prose_polisher.py`)
- `continuity_check.txt` — additional continuity rules

### Memory (`memory/` — JSON files)

Runtime story state persisted between runs:
- `chapter_state.json` — current chapter number + summaries
- `characters.json` — character profiles
- `world.json` — world/setting details
- `plot_structure.json` — 3-act breakdown (10 acts, 30 chapters)
- `themes.json` — thematic elements
- `factions.json` — faction data
- `unresolved_threads.json` — open plot threads

### Output

- `drafts/chapter.txt` — latest generated chapter
- `old/` — archived previous drafts
- `summaries/` — chapter summaries

---

## Configuration (`config.py`)

```python
MODEL = "llama3"                                      # Ollama model
OLLAMA_URL = "http://localhost:11434/api/generate"    # Ollama endpoint
MEMORY_PATH = "memory/"
DRAFT_PATH = "drafts/"
```

LLM params (in `llm_client.py`): `temperature=0.9`, `top_p=0.95`, `repeat_penalty=1.15`.

---

## How to Run

```bash
# Prerequisites: Ollama installed and running
ollama pull llama3
ollama serve

# Install deps
pip install requests

# Generate next chapter
python main.py
```

---

## Story Context

**Novel:** "Elohm" — steampunk fantasy about an AI Construct learning language through magic runes

**Setting:** Aeloria, City of Whispering Towers — steampunk-magical hybrid world where language IS magic

**Metaphor system:** runes = tokens, resonance = attention, memory circles = context windows, the Archive = training data

**Protagonist:** Arkan Veyr — young builder/engineer who creates Elohm

**Core theme:** "Rules alone cannot create understanding" / rigid systems vs. adaptive learning

### Characters

| Name | Role |
|------|------|
| Arkan Veyr | Protagonist, builder/engineer |
| Elohm | AI Construct, learns to speak via runes |
| Maelin | Chief Archivist, mentor figure |
| Serah Kade | Skeptic / safety advocate |
| Circle of Judges | AI alignment council, antagonist force |

### Plot Structure (10 acts, 30 chapters)

| Act | Chapters | Title |
|-----|----------|-------|
| 1 | 1–3 | Age of Rules |
| 2 | 4–6 | Learning Engine ← **current** |
| 3 | 7–9 | Runes and Resonance |
| 4 | 10–12 | Art of Focus |
| 5 | 13–15 | Awakening |
| 6 | 16–18 | Mirrors and Shadows |
| 7 | 19–21 | Trials of Guidance |
| 8 | 22–24 | Users Arrive |
| 9 | 25–27 | Crisis |
| 10 | 28–30 | Co-Evolution |

---

## Thread Tracking

`memory/unresolved_threads.json` tracks active plot threads with full state:
- `id` — unique key
- `title` — the open question
- `status` — `open` / `progressing` / `resolved`
- `chapter_introduced` / `last_updated` — chapter numbers
- `progress` — current state of this thread
- `stakes` — what each resolution path means for the story

After each chapter, `engine/thread_updater.py` calls the LLM with `prompts/thread_updater.txt` to update thread statuses and add any new threads introduced in the chapter.

Active threads:
- `elohm_understanding` — Does Elohm truly understand or only simulate?
- `judges_control` — Can the Judges contain Elohm before it outgrows their rules?
- `city_trust` — Will the city trust or fear the new intelligence?
- `arkan_proof` — Can Arkan prove adaptive learning is safer than rigid rules?
- `maelin_secret` — What is Maelin hiding in the restricted Archive sections?

---

## Known Gaps / Improvement Areas

All previously known gaps have been resolved:

1. ~~Critic → rewrite pipeline not wired up~~ — Fixed: `engine/prose_polisher.py` + wired into `main.py`.
2. ~~`requirements.txt` is empty~~ — Fixed: lists `requests`.
3. ~~Scenes split by naive string split~~ — Fixed: `main.py` uses `re.split(r'(?=Scene \d+:)', plan)`.
4. ~~No retry/error handling on LLM calls~~ — Fixed: `llm_client.py` retries up to 3× with 5s delay, raises clear errors.
5. ~~Thread updater JSON parsing crash~~ — Already had fallback in `thread_updater.py`.
