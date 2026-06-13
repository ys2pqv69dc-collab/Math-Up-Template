"""Example module. Replace with your project's core logic.

Keep computation here (importable, testable) and keep narrative/plots in notebooks.
"""

import numpy as np


def parametric_var(returns: np.ndarray, confidence: float = 0.99) -> float:
    """One-period parametric (variance-covariance) VaR for a return series.

    Assumes returns are approximately normal. Returns a positive loss number.

    This is a placeholder to show the pattern: a small, documented, testable
    function. The accompanying test checks it against a known closed-form value.
    """
    from scipy.stats import norm

    mu = float(np.mean(returns))
    sigma = float(np.std(returns, ddof=1))
    z = norm.ppf(confidence)
    return -(mu - z * sigma)
