import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here

    x = np.asarray(x, dtype=float)
    n = len(x)
    return float((np.mean(x) - mu0) / (np.std(x, ddof=1) / np.sqrt(n)))
    pass