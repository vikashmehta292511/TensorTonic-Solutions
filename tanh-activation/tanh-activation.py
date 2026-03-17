import numpy as np

def tanh(x):
    """
    Compute the Tanh activation function.
    """
    x = np.asarray(x, dtype=float)
    return np.tanh(x)
    