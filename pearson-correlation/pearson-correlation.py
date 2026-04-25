import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here

    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        return None
    N, D = X.shape
    if N < 2:
        return None

    mean = np.mean(X, axis=0)
    X_centered = X - mean
    cov = (X_centered.T @ X_centered) / (N - 1)

    std_devs = np.std(X, axis=0, ddof=1)
    denom = np.outer(std_devs, std_devs)

    with np.errstate(invalid='ignore', divide='ignore'):
        corr = cov / denom

    for i in range(D):
        if std_devs[i] != 0:
            corr[i, i] = 1.0

    return corr
    
    pass