---
title: "The obvious filter would have deleted what I was measuring"
summary: "Keeping only the transfers where both clubs were identified was 93% of the money and looked like cheap hygiene. The rows it dropped were the phenomenon under study."
date: 2026-08-14
tags: [Data quality, Sampling]
---

I was asking whether transfer spending concentrates in fewer clubs, and whether young players carry
a growing premium. The club table in my source is incomplete: some deals name both clubs, some only
the buyer or only the seller, some neither.

The obvious move is to keep the deals where both clubs are identified. That is 93.0% of the money,
which makes it read as cheap hygiene — a rounding error traded for a clean join.

Before dropping anything, I counted what was in each block:

| Block | Deals | 18–23 share | Median fee |
|---|---|---|---|
| Both clubs identified | 5,977 | 38.8% | 2.2M€ |
| Only the buyer identified | 1,579 | **60.2%** | 0.5M€ |
| Only the seller identified | 406 | 31.8% | 0.6M€ |
| Neither | 518 | 51.7% | 0.3M€ |

The block I was about to discard is 60.2% players aged 18–23, at roughly a quarter of the median
price. Those are the cheap purchases of young talent from clubs outside the covered competitions —
which is the exact thing I had set out to measure. Dropping them would not have cleaned the data.
It would have deleted the subject and left me with a confident answer about a different population,
one that skews old and expensive by construction.

So the analysis runs on two declared universes instead of one: 6,716 deals for the price and age
metrics, and the 5,109 with both clubs named for the metrics that have to attribute spend to a club
by name. Every published figure states which one it came from. Nothing is thrown away; the scope
narrows only where the metric itself demands it.

**Missing data is harmless only when it is missing at random, and that is a claim you test, not one
you inherit from how tidy the filter looks.** Four counts and a median per block is the whole test.
It cost one query.
