# Nooks — BDR platform slide

A single 16:9 slide making the case for consolidating the 5-person BDR team onto **Nooks** as one AI platform (prospecting + dialing + sequencing + coaching), instead of a stack of separate tools.

## Files
- `nooks-slide.html` — the slide (self-contained, no dependencies)
- `nooks-slide.png` — rendered 1920×1080 (2×) export for dropping into the deck
- `render.cjs` — Playwright script to re-export the PNG after edits

## The story
1. **The play** — give 5 BDRs one place to find accounts, dial, sequence, and get coached. No tab-hopping, no lost context.
2. **Already invested** — the team already runs on AI Dialer + Nooks numbers + AI Prospector, with live workflows built. Nooks is merging Prospector into its Sequencing product, so adopting Sequencing is the natural next step, not a new vendor.
3. **Why it lands for BDRs** — all-in-one workflow, AI that compounds, and it feeds the GTM-wide move to Gong.
4. **The full cost** — every line item from the order, all-in.

## Cost (source: Nooks Order ORD-XHY110Y, draft — term Sep 17 2026 → Sep 16 2027)
| Line item | Qty | Unit / yr | Annual |
|---|---|---|---|
| AI Dialer — Standard Seat | 5 | $3,600 | $18,000 |
| AI Sequencing — User Seats | 5 | $1,440 | $7,200 |
| AI Sequencing — Admin Seats | 3 | $300 | $900 |
| AI Coaching | 5 | $600 | $3,000 |
| AI Action Credits | 1,400,000 | $0.02 | $28,000 |
| Sequencing Implementation Fee | 1 | $10,000 → **waived** | $0 |
| **List subtotal** | | | **$67,100** |
| **Discount (implementation waived, 14.9%)** | | | **– $10,000** |
| **Grand total, all-in** | | | **$57,100 / yr** |

Billed yearly, Net 30, 5 BDR seats.

## Re-export
```bash
node render.cjs   # regenerates nooks-slide.png from the HTML
```
