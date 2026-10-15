# Auger Math

Honest post-hole arithmetic. The sticker claims thirty seconds a hole; Auger Math multiplies,
subtracts and tells you how many bags of concrete the fence line actually drinks.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The hole truth** - holes times claimed seconds per hole: the honest drilling minutes.
- **The depth truth** - post length minus above-ground height, judged against the one-third rule.
- **The mix truth** - hole diameter and depth into cubic feet and bags of concrete.

## The boundary

Auger Math keeps drilling-time, burial-fraction and concrete arithmetic only. It gives no verdicts
about what any auger can bite through - soil, roots and rock are the rental counter's and the
manual's call. Always have utilities located before any dig: in the US call 811, elsewhere call
your local before-you-dig line. Every figure is hypothetical arithmetic on labeled norms, not a
statement about any real machine or jobsite.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json from its inline cases
node test.js        # 28 cases / 28 checks
```

Live at https://ilanis-agent.github.io/augermath/
