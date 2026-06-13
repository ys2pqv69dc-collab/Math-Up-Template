"""Example test. The point of this folder is the validation habit:
every model is checked against something you trust.
"""

import numpy as np
from scipy.stats import norm

from src.example import parametric_var


def test_parametric_var_matches_closed_form():
    # Construct a sample with known mean and std, then check the function
    # reproduces the closed-form normal-quantile VaR.
    rng = np.random.default_rng(42)
    returns = rng.normal(loc=0.0, scale=0.02, size=100_000)

    result = parametric_var(returns, confidence=0.99)

    mu, sigma = np.mean(returns), np.std(returns, ddof=1)
    expected = -(mu - norm.ppf(0.99) * sigma)

    assert abs(result - expected) < 1e-9
