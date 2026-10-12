---
title: "On Steam, the cheapest price band is never the best-received, in any of 10 genres"
summary: "Across 10 Steam genres, games priced under a real $3.25 never get the best reception, and in 9 of them they get the worst. The pattern is clearest among older games; among recent ones it holds only in Adventure, Indie and Casual — the three genres I recommend for due diligence first."
hero: "./images/01-price-band-vs-best-band.png"
heroAlt: "Horizontal bar chart comparing each genre's cheapest price band against its best band. In all 10 genres the best band's median review score is higher than the cheapest band's, by 2.5 to 5.0 percentage points."
date: 2026-07-28
tools: [Python, pandas, matplotlib]
domain: "Video games"
problemType: "find patterns"
scale: "125,855 games · 2 sources combined"
repo: "https://github.com/BobbyTarantino099/steam-price-reception"
report:
  href: "/reports/steam-price-reception.pdf"
  pages: 9
featured: true
video:
  youtube: "zHiZ3W4nJxE"
  seconds: 68
  poster: "./images/video-poster.jpg"
demonstrates: "Turning an investment question into a pricing-and-sentiment analysis on a dataset with a real structural flaw — not trivial nulls, but a broken header that misaligns columns — enriched with a second source (CPI-U) to compare prices across 29 years in real dollars. The part I most want to show is the one that is usually missing: testing the obvious alternative explanation before publishing the finding, and reporting what it changed."
---

## Context

A video-game-focused investment fund has no data-driven basis for deciding which genre to
prioritise for its thesis in the PC/Steam market. It has more candidates than filters: the
operating question isn't "is this a good game?" but "where in the catalogue is due diligence
time best spent?".

The analytical question I framed: **which genre and price-band combinations (inflation-adjusted
price quartiles, over paid games with ≥500 reviews) in Steam's historical catalogue show the most
consistent pattern of high positive-review share, controlling for game age?** The decision this
unlocks is concrete: recommend 2-3 genres where the committee should prioritise due diligence,
with evidence of which price band sustains the best reception in each.

## Data

| Source | Period | Volume | Licence |
|---|---|---|---|
| [Steam Games Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) (fronkongames) | 1997-06-30 → 2026-05 | 125,855 games × 40 columns | CC BY 4.0 |
| [CPI-U, series `CUUR0000SA0`](https://www.bls.gov/cpi/) (US Bureau of Labor Statistics) | 1997-2026 | Annual index | Public domain |

The raw CSV is ~400 MB and is not stored in the case repository — it is downloaded from the
Kaggle link (see Reproduce). CC BY 4.0 requires attribution: fronkongames dataset, Kaggle. No PII
in either source.

**Main limitations:**

- **No causality.** The pattern is a descriptive correlation. The strongest alternative reading —
  that studios charging more also invest more in production — cannot be ruled out with this data.
  What I did test is game age: it explains part of the pattern (see finding 4).
- **No revenue or sales data.** `estimated_owners` comes as SteamSpy-estimated ranges, not
  Valve-confirmed figures, and was not used as a metric. This case speaks to reception, not
  profitability.
- **The long tail is excluded.** The ≥500-review filter deliberately excludes 34.1% of the
  catalogue, which has zero reviews. The sample is biased toward visible games.
- **Survivorship bias.** Only games that shipped on Steam. Not cancelled titles, not delisted
  ones, not console or mobile.

## Process

**Tools:** Python with pandas. The file is 400 MB with a structural header bug — auditing it by
hand in a spreadsheet was not viable, and the case required the cleaning to be reproducible end
to end.

**Key cleaning decisions:**

1. **Fixed a header bug.** The raw header declares 39 columns but every row carries 40: the name
   `DiscountDLC count` merges two real columns, `Discount` and `DLC count`. Everything past that
   position was misaligned. Fixed by inserting the missing name before loading.
2. **Inflation adjustment instead of a declared limitation.** I combined the catalogue with the
   BLS CPI-U to compare, in real 2026 dollars, prices of games released 29 years apart. A $9.99
   game from 1999 is not the same product as a $9.99 game from 2025.
3. **Exploded by genre.** A game with N genres produces N rows, so each genre gets its own
   evidence. 117,430 games → 338,575 game-genre rows.
4. **Cleaned the genre taxonomy.** Steam's `Genres` column mixes real genres with content
   descriptors (`Violent`, `Gore`), non-game software tags (`Accounting`, `Utilities`) and
   business model (`Free To Play`, `Early Access`). I excluded the 23 tags that are not a video
   game genre and kept the 10 real ones.

Count reconciliation: 125,855 − 2 (future release date) − 0 (duplicates) − 8,423 (no genre) =
**117,430**, verified with an `assert` in the script. Final analysis base: 9,048 paid games with
≥500 reviews; 8,998 of them carry at least one of the 10 real genres, and those are the games
behind the genre tables and figures.

## Findings

### 1. The cheapest band is never the best, in any of the 10 genres

![Horizontal bar chart comparing each genre's cheapest price band against its best band, showing the best band ahead by 2.5 to 5.0 percentage points in every genre.](./images/01-price-band-vs-best-band.png)

The median positive-review share in Q1 (≤$3.25 real) ranges from 76.0% in Massively Multiplayer
to 86.3% in Casual. In none of the ten genres is it the best band, and in nine it is the worst.
The exception is Massively Multiplayer, where Q1 comes second, ahead of Q3 and Q4 (see finding 5).

### 2. The peak sits at mid-to-high prices, not the highest price

![Heatmap of median positive-review share by genre and price band, with darker cells at Q3 and Q4 across most genres.](./images/02-genre-price-heatmap.png)

Where each genre peaks:

- **Q3 ($6.46–$12.36)** — Action, Indie, Simulation, Casual and Strategy.
- **Q4 (>$12.36)** — Adventure, Racing, Sports and RPG.
- **Q2 ($3.25–$6.46)** — Massively Multiplayer, the exception (see finding 5).

No genre has its best reception in Q1. That rules out the simplistic "more expensive is
always better" reading too: in half the genres, the most expensive band already trails Q3.

### 3. The effect is real but moderate: 2.50 to 5.04 percentage points

![Ranking of the price effect by genre, with Adventure, Indie and Casual highlighted as the strongest combined candidates.](./images/03-effect-ranking.png)

The gap between Q1 and each genre's best band ranges from 2.50 p.p. (RPG) to 5.04 p.p. (Adventure).
Quantifying it matters: it supports a directional screening argument, not a claim that price alone
transforms a product's reception.

Three genres combine the best effect, volume and absolute reception:

| Genre | Games | Median reception |
|---|---|---|
| Adventure | 4,030 | 86.2% |
| Indie | 5,561 | 86.7% |
| Casual | 2,230 | 88.2% |

### 4. Age explains part of it: among recent games, the pattern holds in only three genres

![Two panels of dot strips, older games and recent games, one row per genre, with each price band's median review score as a dot. Among older games the cheapest band is the leftmost dot in all 9 genres with enough data; among recent games only in Adventure, Casual and Indie, and in RPG and Sports it edges ahead.](./images/04-age-control.png)

The obvious objection is that cheap games are simply the old ones. It is partly right. Splitting
games at the median age (6 years), among older games Q1 comes last in all 9 genres with enough
data. Among recent games it comes last only in Adventure, Indie and Casual; in the other six the
gap mostly closes, and in RPG and Sports Q1 even edges ahead, by 1 point or less. The overall
correlation between age and reception is weak (−0.087), but the split shows that age changes the
pattern. The finding is solid for older games, and for recent ones it is limited to three genres.

### 5. Massively Multiplayer is the exception, and is reported as such

It has no chart of its own, deliberately. It's the only genre with a non-monotonic pattern (its
best band is Q2), has the lowest median of the ten across all four bands (74.8%-79.0%), and the
smallest n in the base (176 games). The evidence is weak, so it is neither recommended nor
dismissed: it is documented as insufficient.

*Corrected on 2026-10-11: an earlier version said the cheapest band was the worst in all 10
genres and that age played no role. Both overstated the data; see the
[repository's log](https://github.com/BobbyTarantino099/steam-price-reception/blob/main/CASO.md).*

## Recommendations

| # | Recommendation | Evidence | Impact | Effort |
|---|---|---|---|---|
| **R1** | Concentrate next cycle's due diligence on **Adventure, Indie and Casual** | The three highest reception medians (86.2 / 86.7 / 88.2%) + price-band effect of 3.31-5.04 p.p. + sufficient target volume + the only three genres where the pattern survives among recent games | High | Low |
| **R2** | Add the **catalogue's position in the price quartiles** to screening; flag studios with >50% in Q1 for review | Q1 is never the best band and is the worst in 9 of 10 genres; the signal is clearest among older catalogues | Medium | Low |
| **R3** | **Deprioritise Massively Multiplayer** this cycle; Sports and Racing as "insufficient evidence" | MMO: 76.4% median, non-monotonic pattern, n=176. Sports (329) and Racing (338) below the n<350 threshold | Medium | Low |

All three are low-effort because all three are rules layered on a process the fund already runs.
That's deliberately the ceiling of what this analysis can support: with aggregated reviews and no
revenue data, the honest recommendation is **where to look first**, not where to put the money.

**Main next step:** lower the review threshold to 50 and 100 to see whether the pattern holds in
the indie/niche long tail. That unlocks the decision of whether the fund should open an
investment lane for small studios.

## Reproduce

```bash
# 1. Clone
git clone https://github.com/BobbyTarantino099/steam-price-reception.git
cd steam-price-reception

# 2. Dependencies
pip install pandas matplotlib seaborn jupyter

# 3. Download the raw file (not in the repo, ~400 MB)
#    https://www.kaggle.com/datasets/fronkongames/steam-games-dataset
#    Save it as:
#    datos/crudos/steam_fronkongames_catalogo-historico_2026-07-28.csv
#    The CPI-U file is already at datos/crudos/bls_cpi-u_anual_1997-2026_2026-07-28.csv

# 4. Run in order
python notebooks/procesar.py    # cleaning -> datos/limpios/
python notebooks/analizar.py    # quartiles and genre x band table -> salidas/tablas/
python notebooks/verificar.py   # the 7 analysis checks
python notebooks/graficos.py    # the 4 figures -> salidas/graficos/
```

## What this demonstrates

Turning an investment question into a pricing-and-sentiment analysis, on a dataset with a real
structural flaw — not trivial nulls, but a broken header that misaligns columns — and combining
it with a second source (CPI-U) to compare prices across 29 years in real dollars.

What I most want to show here is the part that's usually missing: **testing the alternative
explanation before publishing the finding, and saying what it changed**. The obvious objection to
"cheap games get worse reception" is that cheap games are the old ones. I checked, and it is
partly right: the pattern is solid among older games and, among recent ones, survives in only
three genres — the same three I recommend. That check is in the repository with its code. And
the genre that didn't fit — Massively Multiplayer — is reported as insufficient evidence instead
of being left out.
