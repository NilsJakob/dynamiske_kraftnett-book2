import json

fname = "01_forord/about330.ipynb"

with open(fname, encoding="utf-8") as f:
    nb = json.load(f)

nb["cells"] = [
    cell
    for cell in nb["cells"]
    if not (
        cell.get("cell_type") == "markdown"
        and any("Figur 1." in line for line in cell.get("source", []))
    )
]

with open(fname, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("Done")