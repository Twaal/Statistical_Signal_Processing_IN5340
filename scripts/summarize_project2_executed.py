from pathlib import Path
import nbformat

nb_path = Path(r"c:\Users\theod\Documents\uio\in5340\Statistical_Signal_Processing_IN5340\Project_2\presentation\project_2_executed.ipynb")
nb = nbformat.read(nb_path.open("r", encoding="utf-8"), as_version=4)

for i, cell in enumerate(nb.cells, start=1):
    ctype = cell.get("cell_type")
    src = "".join(cell.get("source", [])) if isinstance(cell.get("source"), list) else cell.get("source", "")
    first = src.strip().splitlines()[0] if src.strip() else ""
    if ctype == "markdown":
        if first.startswith("#") or "Exercise" in src:
            print(f"[{i:02d}] MD: {first}")
    else:
        outs = cell.get("outputs", [])
        img_count = 0
        txt = []
        for o in outs:
            if o.get("output_type") == "stream":
                t = o.get("text", "")
                if t:
                    txt.append(t.strip().splitlines()[0])
            data = o.get("data", {})
            if "image/png" in data:
                img_count += 1
        if img_count or txt:
            print(f"[{i:02d}] CODE: {first[:80]}")
            if img_count:
                print(f"      images: {img_count}")
            if txt:
                print(f"      text: {txt[0][:120]}")
