Here are my projects for a statistical signal processing course at the University of Oslo.

## Presentations

Each project keeps slides and figures under `Project_X/-presentation/`:

- `Project_X/-presentation/presentation*.tex` / `presentation*.pdf`
- `Project_X/-presentation/figs/` (PNG/PDF figures used by the slides)

### Presentation template

Reusable boilerplate lives in `presentation_template/`:

- `presentation_template/in5340_beamer_template.tex`
- `presentation_template/new_in5340_presentation.ps1`

### Generate a new deck

From the repo root (Windows PowerShell):

```powershell
.\presentation_template\new_in5340_presentation.ps1 `
	-ProjectDir .\Project_2 `
	-Output presentation.tex `
	-Title "IN5340 Project II" `
	-ShortTitle "IN5340 P2" `
	-Author "Theodor Wålberg" `
	-Compile -Force
```

Notes:

- Output goes to `Project_2/-presentation/presentation.tex` by default.
- Put figures in `Project_2/-presentation/figs/` and reference them as `\includegraphics{my_figure.png}`.
- Optional: override the presentation folder name with `-PresentationDir`.

### Compile an existing deck

From the deck folder:

```powershell
cd .\Project_1\-presentation
pdflatex -interaction=nonstopmode -halt-on-error presentation_p1.tex
pdflatex -interaction=nonstopmode -halt-on-error presentation_p1.tex
```
