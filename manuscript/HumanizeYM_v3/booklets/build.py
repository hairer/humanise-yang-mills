"""Rebuild the four reading booklets from the v3 manuscript with pdfLaTeX and BibTeX."""
from itertools import groupby
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
VOLUMES = [
    ("I", 1, 5, "Lattice fields and Gaussian blocking",
     "How does the Wilson measure encode a local field? "
     "The lattice observables and their free Maxwell counterparts fix the comparison. "
     "The renormalization transformation then identifies the Gaussian fluctuations "
     "and the critical configuration for the interacting integral."),
    ("II", 6, 9, "The nonlinear renormalization step",
     "At one pair of scales, large fields carry an action cost while small fields "
     "admit a local Gaussian expansion. Determinant matching and connected polymer "
     "estimates put the result back into a form that can be iterated."),
    ("III", 10, 13, "From a common trajectory to continuum fields",
     "A single choice of scales and couplings carries observables with insertions through "
     "successive steps. First the lattice spacing tends to zero at fixed "
     "volume. A subsequence of growing volumes then yields the continuum "
     "correlations used to define local fields."),
    ("IV", 14, 19, "Reconstruction, the trace law and operator products",
     "Reflection positivity and Ward identities lead from Euclidean fields to "
     "relativistic reconstruction in each phase. The final chapters derive the "
     "short-distance trace law in a fixed phase, construct finite-order "
     "operator products and collect the conclusions of the manuscript."),
]
STEMS = [f"HumanizeYM-v3-{roman}" for roman, *_ in VOLUMES]


def write_sources(work):
    master = (ROOT / "monograph.tex").read_text()
    chapters = re.findall(r"\\input\{(chapters/[^}]+)\}", master)
    numbers = [int(Path(p).name.split("-")[0]) for p in chapters]
    if numbers != list(range(1, VOLUMES[-1][2] + 1)):
        raise ValueError("Check the booklet boundaries against the current chapter list.")
    # The preamble now lives in monograph.tex (upstream removed the use of preamble.tex).
    start = master.index("\n", master.index(r"\documentclass")) + 1
    (work / "booklet-preamble.tex").write_text(master[start:master.index(r"\begin{document}")])
    about = master[master.index(r"\chapter*{About this draft}"):master.index(r"\input{reading-guide}")]
    (work / "booklet-about.tex").write_text(about)
    theorem = (ROOT / "main-theorem.tex").read_text().replace(
        r"(p.~\pageref{ch19:conditional})", r"(Booklet IV, p.~\pageref{ch19:conditional})")
    (work / "booklet-main-theorem.tex").write_text(theorem)
    subjects = {}
    for line in (HERE / "subjects.txt").read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        if line.startswith("["):
            group = subjects.setdefault(line.strip("[]"), [])
        else:
            term, labels = line.split(" | ")
            group.append((term, labels.split()))
    for n, (roman, first, last, title, guide) in enumerate(VOLUMES):
        stem = STEMS[n]
        settings = {
            "volumeNumber": n + 1, "volumeRoman": roman, "volumeTitle": title,
            "volumeGuide": guide, "chapterRange": f"{first}--{last}", "previousChapter": first - 1,
            "seriesTable": "\n".join(
                rf"\seriesrow{{{i}}}{{{r} \quad {a}--{b}}}{{{t}}}"
                for i, (r, a, b, t, _) in enumerate(VOLUMES, 1)),
        }
        lines = [rf"\newcommand{{\{k}}}{{{v}}}" for k, v in settings.items()]
        lines += [rf"\IfFileExists{{{s}.aux}}{{\externaldocument[][nocite]{{{s}}}[{s}.pdf]}}{{}}"
                  for s in STEMS if s != stem]
        (work / f"{stem}-settings.tex").write_text("\n".join(lines))
        (work / f"{stem}-chapters.tex").write_text(
            "\n".join(rf"\input{{{p}}}" for p in chapters[first - 1:last]))
        lines = []
        for letter, entries in groupby(sorted(subjects[roman]), key=lambda entry: entry[0][0]):
            lines.append(rf"\indexletter{{{letter}}}")
            for term, labels in entries:
                lines.append(rf"\subjectentry{{{term}}}{{{','.join(labels)}}}")
        (work / f"{stem}-index.tex").write_text("\n".join(lines))


def build(work):
    env = os.environ.copy()
    env.update(TEXINPUTS=f".:{ROOT}:{HERE}:" + env.get("TEXINPUTS", ""),
               BIBINPUTS=f"{ROOT}:" + env.get("BIBINPUTS", ""))

    def run(*args):
        result = subprocess.run(args, cwd=work, env=env, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, errors="replace")
        if result.returncode:
            raise RuntimeError(result.stdout[-4500:])

    def latex(stem):
        run("pdflatex", "-interaction=nonstopmode", "-halt-on-error",
            "-file-line-error", f"-jobname={stem}", "booklet.tex")

    def crossrefs():
        return [(work / f"{stem}.{ext}").read_bytes() for stem in STEMS for ext in ("aux", "toc")]

    for stem in STEMS:
        latex(stem)
        run("bibtex", stem)
    for _ in range(6):
        before = crossrefs()
        for stem in STEMS:
            latex(stem)
        if before == crossrefs():
            break
    else:
        raise RuntimeError("Cross-booklet references did not stabilize.")
    for stem in STEMS:
        log = (work / f"{stem}.log").read_text(errors="replace")
        warnings = [line for line in log.splitlines()
                    if re.search(r"undefined|multiply defined|destination.*does not exist", line, re.I)]
        if warnings:
            raise RuntimeError(f"{stem}: " + "\n".join(warnings))
    for stem in STEMS:
        shutil.copyfile(work / f"{stem}.pdf", HERE / f"{stem}.pdf")
        print(f"Built {stem}.pdf")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="ym-booklets-") as folder:
        write_sources(Path(folder))
        build(Path(folder))
