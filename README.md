# Napkin Math

Event napkin pack, week, cost and time arithmetic. The 585 napkins at 50 napkins a pack take 12 packs, the last pack holding 35 napkins.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The packs truth** - the napkins (1 to 1000000) divided by the napkins a pack (1 to 1000), rounded up, with what the last pack holds.
- **The weeks truth** - the napkins divided by the napkins used a week (1 to 100000), with the napkins left for the next week.
- **The cost truth** - the packs (1 to 100000) times the pack price ($0.01 to $999.99) to the cent, and spread over the napkins, half rounded up.
- **The time truth** - the napkins divided by the napkins napkined a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any napkin, pack or folding table and does not know whether napkins will really arrive uncreased, a supplier will run out or a price will hold, and it gives no verdict that a pack is worth its price or a napkin is right for an event. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every pack recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
