import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here

    x = np.asarray(x, dtype=float)
    N = len(x)
    alpha = (1 - ci) / 2

    if rng is None:
        rng = np.random.default_rng()

    idx = rng.integers(0, N, size=(n_bootstrap, N))
    boot_means = x[idx].mean(axis=1)

    lower = float(np.quantile(boot_means, alpha))
    upper = float(np.quantile(boot_means, 1 - alpha))

    return boot_means, lower, upper
    pass
