import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.asarray(x, dtype=float)
    if x.ndim == 0:
        x = x.reshape(1)
    sigmoid = 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    return x * sigmoid
    pass