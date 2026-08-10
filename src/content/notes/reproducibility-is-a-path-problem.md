---
title: "My analysis was reproducible. My file paths were not."
summary: "The scripts were correct and the numbers checked out, but every one of them had the path of the machine it was written on baked in — so nobody else could run a line."
date: 2026-08-10
tags: [Reproducibility, Python]
---

I had a case study I was fairly happy with. Cleaning documented transformation by transformation,
counts reconciled with an `assert`, seven verification checks, the obvious alternative explanation
tested and ruled out. The exit gate for the phase had one unchecked box: *analysis reproducible
from the raw file by a third party*. I had been treating that as paperwork.

It was not paperwork. When I finally tried to run the scripts on my own machine, none of them
worked. Every one started like this:

```python
RUTA_BASE = '/sessions/gifted-dazzling-albattani/mnt/Videojuegos'
```

That is the path of the temporary environment the code was written in. The notebook was worse: it
had been stitched together across two different sessions, and carried patches rewriting one
sandbox path into another mid-line.

The fix is three lines, and it is the same in any language:

```python
from pathlib import Path

RUTA_BASE = Path(__file__).resolve().parents[1]
```

Resolve paths from where the script lives, not from where it once ran. In Node,
`path.resolve(__dirname, '..')`. In Markdown, relative image links — one of my deliverables had
four broken images for the same reason.

What I take from it is not the fix, which is trivial, but the failure mode. **An analysis is not
reproducible because the logic is correct. It is reproducible because someone other than you can
run it.** Those are different claims, and only one of them can be verified by reading your own
code.

So the check went into my method, with the command that performs it:

```bash
grep -rn "/home/\|/Users/\|C:\\\\\|/sessions/\|/mnt/" --include="*.py" --include="*.md" .
```

A gate you never run is a gate you do not have.
