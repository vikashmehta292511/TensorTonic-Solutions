import numpy as np
def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    x = np.asarray(series, dtype=float)
    x = x - x.mean()
    gamma0 = np.dot(x, x)

    if gamma0 == 0:
        return [1.0] + [0.0] * max_lag

    return [float(np.dot(x[:len(x)-k], x[k:]) / gamma0) for k in range(max_lag + 1)]