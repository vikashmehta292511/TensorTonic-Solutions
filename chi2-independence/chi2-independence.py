import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.asarray(C, dtype=float)
    total = C.sum()
    expected = np.outer(C.sum(axis=1), C.sum(axis=0)) / total
    chi2 = float(np.sum((C - expected) ** 2 / expected))
    return chi2, expected
    pass