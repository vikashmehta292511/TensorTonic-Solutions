import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here

    x = np.asarray(x, dtype=float)
    var = float(np.var(x, ddof=1))
    std = float(np.std(x, ddof=1))
    return var, std
    pass