import numpy as np

def relu(x):
    """
    Compute the ReLU activation function.
    """
    x = np.asarray(x, dtype=float)
    return np.maximum(0, x)
    pass