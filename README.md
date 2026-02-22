# IN5340 Statistical Signal Processing - Projects

Here are my projects for a statistical signal processing course at the University of Oslo.

## Presentations

This repository supports Beamer slides for any project folder (for example Project_1, Project_2, Project_3, ...).

### Folder structure

Each project should contain a presentation folder in one of these forms:

- Preferred: Project_X/presentation/
- Legacy (template default): Project_X/-presentation/

Inside that folder:

- presentation_pX.tex (LaTeX source)
- presentation_pX.pdf (compiled deck)
- igs/ (images: plot_01.png, plot_02.png, ..., plot_NN.png)

### Template files

Reusable boilerplate lives in:

- presentation_template/in5340_beamer_template.tex
- presentation_template/new_in5340_presentation.ps1

---

## Automated Build Pipeline (Recommended)

The easiest way to generate a complete presentation is to use the automated build script, which:
1. Executes the Jupyter notebook (extracting all cell outputs as plots)
2. Exports PNG figures to Project_X/presentation/figs/
3. Compiles the LaTeX presentation to PDF

### Quick Start

From the repo root in Windows PowerShell:

```powershell
.\scripts\build_presentation.ps1 -Project 2
```

This will:
- Execute Project_2/project_2.ipynb with the conda in5340 environment
- Extract all PNG plots as igs/plot_01.png, plot_02.png, ..., etc.
- Compile Project_2/presentation/presentation_p2.tex to PDF (two passes)
- Output: Project_2/presentation/presentation_p2.pdf

### Usage Options

```powershell
# Build Project X
.\scripts\build_presentation.ps1 -Project 1
.\scripts\build_presentation.ps1 -Project 3

# Skip notebook execution (use if notebook is already executed)
.\scripts\build_presentation.ps1 -Project 2 -SkipNotebook

# Skip LaTeX compilation (only run notebook and extract figures)
.\scripts\build_presentation.ps1 -Project 2 -SkipLatex

# Execute notebook and extract figures, then manually compile LaTeX
.\scripts\build_presentation.ps1 -Project 2 -SkipLatex
cd .\Project_2\presentation
pdflatex -interaction=nonstopmode -halt-on-error presentation_p2.tex
pdflatex -interaction=nonstopmode -halt-on-error presentation_p2.tex
```

### Prerequisites for Automated Build

- **Python environment**: Conda in5340 with 
bformat and 
bclient packages
- **LaTeX**: MiKTeX or TeX Live with pdflatex
- **Notebook**: Project_X/project_X.ipynb (executes in conda in5340)
- **LaTeX file**: Project_X/presentation/presentation_pX.tex

Verify prerequisites:

```powershell
conda activate in5340; python --version
pdflatex --version
```

---

## Manual Beamer Deck Generation (Alternative)

If you prefer to create a deck from scratch:

```powershell
.\presentation_template\new_in5340_presentation.ps1 \
  -ProjectDir .\Project_X \
  -Output presentation_X.tex \
  -Title "IN5340 Project X" \
  -ShortTitle "IN5340 PX" \
  -Author "Your Name" \
  -Compile -Force
```

Notes:

- Default output folder is Project_X/-presentation/.
- To use Project_X/presentation/, add -PresentationDir presentation.
- Put figures in the project presentation igs/ folder and reference them as \includegraphics{my_figure.png}.

---

## Manual LaTeX Compilation

If the notebook and figures are already in place, compile directly:

### 1) Prerequisites (Windows)

- Install MiKTeX or TeX Live.
- Verify pdflatex is available:

```powershell
pdflatex --version
```

### 2) Compile from the deck folder

```powershell
cd .\Project_X\presentation
pdflatex -interaction=nonstopmode -halt-on-error presentation_pX.tex
pdflatex -interaction=nonstopmode -halt-on-error presentation_pX.tex
```

Run twice so references, navigation symbols, and table-of-contents metadata are fully resolved.

### 3) One-line compile

```powershell
cd .\Project_X\presentation; pdflatex -interaction=nonstopmode -halt-on-error presentation_pX.tex; pdflatex -interaction=nonstopmode -halt-on-error presentation_pX.tex
```

### 4) Output

Compiled PDF path:

- Project_X/presentation/presentation_pX.pdf

---

## Figure Naming Convention

The automated build system uses consistent, simple figure names:

- plot_01.png - First plot from notebook
- plot_02.png - Second plot from notebook
- plot_NN.png - Nth plot from notebook

These are extracted in the order they appear during notebook execution. In your LaTeX file, reference them as:

```latex
\fullfig{plot_01.png}
\colfig{plot_02.png}
```

---

## Troubleshooting

### pdflatex : The term 'pdflatex' is not recognized

- Restart terminal after installing MiKTeX/TeX Live, or add the LaTeX bin folder to PATH.

### Cannot find file ...tex

- Run from the correct presentation folder or pass the full .tex path.

### Missing image errors

- Confirm images are in igs/ and filenames match exactly (e.g., plot_01.png, not plot_1.png).
- Verify LaTeX references use exact names: \fullfig{plot_01.png} not {plot_01}.

### Notebook execution fails in build script

- Verify conda in5340 environment exists: conda env list
- Activate and test: conda activate in5340; cd Project_X; jupyter notebook project_X.ipynb

### LaTeX compilation produces blank pages or missing TOC

- Run pdflatex twice (or use uild_presentation.ps1 which does this automatically).
