# Project Name

> One-sentence statement of what this project computes and why it matters.

## Problem

What question does this project answer? State it the way a practitioner would.
(e.g. "Estimate the 1-day 99% Value at Risk of a multi-asset portfolio and test
whether the model's exception rate is consistent with its confidence level.")

## Method

The approach in 3–5 sentences. Name the technique(s) and the key idea behind each.

## Key assumptions

- Assumption 1 (e.g. returns are measured daily, log returns)
- Assumption 2 (e.g. correlations estimated over a 250-day window)
- Assumption 3

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/      # or: python src/main.py
```

## Validation / correctness check

How do I know the result is right? (e.g. "Parametric VaR cross-checked against a
closed-form normal quantile; Monte Carlo VaR converges to the parametric figure as
paths increase — see `tests/` and the convergence plot in the notebook.")

## Result

One figure or one number that tells the story. Embed the key chart here.

## Honest limitation

One real weakness of this approach and when it would fail. (Stating this is a
feature, not a confession — it signals you think like a validator.)

## Structure

- `src/` — core logic
- `notebooks/` — narrative exploration and the key figure
- `tests/` — correctness checks
