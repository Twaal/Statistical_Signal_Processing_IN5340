import base64
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(r"c:\Users\theod\Documents\uio\in5340\Statistical_Signal_Processing_IN5340")
NOTEBOOK = ROOT / "Project_2" / "project_2.ipynb"
OUT_DIR = ROOT / "Project_2" / "presentation"
FIG_DIR = OUT_DIR / "figs"
EXEC_NOTEBOOK = OUT_DIR / "project_2_executed.ipynb"

OUT_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)

with NOTEBOOK.open("r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

client = NotebookClient(
    nb,
    timeout=300,
    kernel_name="python3",
    resources={"metadata": {"path": str(NOTEBOOK.parent)}},
)
client.execute()

with EXEC_NOTEBOOK.open("w", encoding="utf-8") as f:
    nbformat.write(nb, f)

img_index = 1
for cell_index, cell in enumerate(nb.cells):
    if cell.get("cell_type") != "code":
        continue
    for out_index, output in enumerate(cell.get("outputs", [])):
        data = output.get("data", {}) if isinstance(output, dict) else {}
        if "image/png" in data:
            b64 = data["image/png"]
            if isinstance(b64, list):
                b64 = "".join(b64)
            img_bytes = base64.b64decode(b64)
            # Use simple sequential naming: plot_01.png, plot_02.png, etc.
            filename = f"plot_{img_index:02d}.png"
            (FIG_DIR / filename).write_bytes(img_bytes)
            img_index += 1

print(f"Executed notebook saved to: {EXEC_NOTEBOOK}")
print(f"Exported {img_index - 1} PNG plots to: {FIG_DIR}")
