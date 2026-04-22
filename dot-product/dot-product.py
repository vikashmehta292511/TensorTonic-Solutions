import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here

    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("Inputs must be 1D arrays")
    if x.shape != y.shape:
        raise ValueError("x and y must have the same length")
    return float(np.dot(x, y))
    
    pass