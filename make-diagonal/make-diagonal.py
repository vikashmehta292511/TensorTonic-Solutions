import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v = np.asarray(v)
    if v.ndim != 1 or v.size == 0:
        return None
    return np.diag(v)
    
    pass
