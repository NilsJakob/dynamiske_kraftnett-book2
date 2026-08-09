import json
from pathlib import Path

# ---- CONFIG ----

MARKERS = [
    "# FEEDBACK CELL",
    "# SCORE CELL",
    "# TEST CELL",
    "# SOLUTION CELL"
]

TAGS_TO_ADD = ["remove-input"]

# ---- CORE FUNCTION ----

def tag_notebook(nb_path):
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    changed = False

    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue

        source = "".join(cell["source"])

        # Check if any marker is in the cell
        if any(marker in source for marker in MARKERS):
            metadata = cell.setdefault("metadata", {})
            tags = metadata.setdefault("tags", [])

            for tag in TAGS_TO_ADD:
                if tag not in tags:
                    tags.append(tag)
                    changed = True

    if changed:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print(f"Updated: {nb_path}")


# ---- APPLY TO ALL NOTEBOOKS ----

def process_all():
    for nb_path in Path(".").rglob("*.ipynb"):
        tag_notebook(nb_path)


# ---- ENTRY POINT ----

if __name__ == "__main__":
    process_all()