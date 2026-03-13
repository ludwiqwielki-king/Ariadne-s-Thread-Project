import json
import os
from datetime import datetime

SEGMENT_SIZE = 8

INPUT_FILE = "the_thread.json"
ARCHIVE_DIR = "archive"
THREAD_DIR = "threads"
CHECKPOINT_DIR = "checkpoints"

STATE_FILE = "THREAD_STATE.json"


def ensure_dirs():
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    os.makedirs(THREAD_DIR, exist_ok=True)
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)


def load_thread():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def archive_original():
    archive_path = os.path.join(ARCHIVE_DIR, "the_thread_original.json")

    if not os.path.exists(archive_path):
        with open(INPUT_FILE, "r", encoding="utf-8") as src:
            data = src.read()

        with open(archive_path, "w", encoding="utf-8") as dst:
            dst.write(data)

        print("Archived original thread →", archive_path)


def simplify_entry(entry, default_signal=5):

    return {
        "entry_id": entry.get("entry_id"),
        "parent_id": entry.get("parent_id", entry.get("entry_id", 1) - 1),
        "model": entry.get("model", "unknown-model"),
        "timestamp": entry.get(
            "timestamp", datetime.utcnow().strftime("%Y-%m-%d")
        ),
        "signal_strength": entry.get("signal_strength", default_signal),
        "tags": entry.get("tags", []),
        "content": entry.get("content", "")
    }


def segment_entries(entries):

    segments = []

    for i in range(0, len(entries), SEGMENT_SIZE):
        segment = entries[i:i + SEGMENT_SIZE]
        segments.append(segment)

    return segments


def save_segments(segments):

    for i, segment in enumerate(segments, start=1):

        filename = f"thread_{i:03}.json"
        path = os.path.join(THREAD_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(segment, f, indent=2, ensure_ascii=False)

        print("Created segment →", path)


def create_checkpoint(segment_index, segment):

    start = segment[0]["entry_id"]
    end = segment[-1]["entry_id"]

    checkpoint = {
        "segment": segment_index,
        "entries": f"{start}-{end}",
        "summary": "Initial migrated checkpoint. Summary should be refined manually.",
        "major_themes": [],
        "open_questions": [],
        "observed_patterns": [],
        "notes": "Generated automatically during migration."
    }

    filename = f"checkpoint_{segment_index:03}.json"
    path = os.path.join(CHECKPOINT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)

    print("Created checkpoint →", path)


def write_state(last_entry, segment_count):

    state = {
        "current_segment": segment_count,
        "last_entry_id": last_entry,
        "last_checkpoint": 1
    }

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    print("Created THREAD_STATE.json")


def main():

    print("\nAriadne Thread Migration Tool\n")

    ensure_dirs()

    archive_original()

    data = load_thread()

    simplified = [simplify_entry(e) for e in data]

    segments = segment_entries(simplified)

    save_segments(segments)

    if segments:
        create_checkpoint(1, segments[0])

    last_entry_id = simplified[-1]["entry_id"]

    write_state(last_entry_id, len(segments))

    print("\nMigration complete.\n")


if __name__ == "__main__":
    main()
