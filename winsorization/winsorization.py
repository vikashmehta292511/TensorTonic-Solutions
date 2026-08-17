import numpy as np
def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    # Write code here

    vals = np.asarray(values, float)
    n = len(vals)
    s = np.sort(vals)
    def pct(p):
        k = (n - 1) * p / 100
        f, c = int(np.floor(k)), int(np.ceil(k))
        return s[f] if f == c else s[f] + (k - f) * (s[c] - s[f])
    lo, hi = pct(lower_pct), pct(upper_pct)
    return np.clip(vals, lo, hi).tolist()