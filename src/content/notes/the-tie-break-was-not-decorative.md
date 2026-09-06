---
title: "My risk bands changed every time I rebuilt the database"
summary: "The query was correct and every number it produced was plausible. Half the rows still changed between two runs of the same pipeline over the same data — because of a tie-break I had not written."
date: 2026-09-02
tags: [Reproducibility, SQL, DuckDB]
---

The loan size bands in my last case are quartiles *within* each fiscal year. A $100,000 loan was
large in 1993 and mid-sized in 2025, so quartiling across the whole history would have turned the
size band into a disguised clock: it would have measured inflation and programme growth, not risk.

```sql
ntile(4) OVER (
  PARTITION BY anio_fiscal
  ORDER BY importe_aprobado
)
```

That reads as finished. It is also not deterministic.

Approved amounts cluster hard on round numbers — $50,000, $150,000, $500,000 — so ordering by
amount alone leaves thousands of ties, and `ntile` splits them by whatever order the rows happen to
arrive in. DuckDB makes no promise about that order when it reads four files in parallel.
Rebuilding the database changed **half the rows** of the size-band export.

The fix is a tie-break long enough to be total:

```sql
ORDER BY importe_aprobado,
         fecha_aprobacion,
         plazo_meses,
         estado,
         fecha_fallido,
         lender_id,
         naics
```

The two outcome fields are in that list on purpose. Any tie that survives is then between loans
that defaulted or survived alike, so moving one across a quartile boundary cannot move the curve.

What I take from it is not the `ORDER BY`. It is that **a non-deterministic result does not fail,
and that is what makes it worse than one that does.** Nothing raised. No check went red. Every run
produced numbers I would have believed — just not the same ones.

I did not find it by reading the code. I found it by building the database twice and diffing the
sha256 of every exported file, which also caught a second drift: `sum()` over millions of doubles
is not associative under parallel execution, so one total serialised as `3834629259.01` and the
next as `3834629259.0099998`.

The two-run diff costs one rebuild. It now runs in every case that promises a third party can
reproduce it — because that promise is worth exactly what the check behind it is worth.
