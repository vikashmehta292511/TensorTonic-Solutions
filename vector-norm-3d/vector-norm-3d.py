import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here

    v = np.asarray(v, dtype=float)

    if v.ndim == 1:  
        return float(np.sqrt(np.sum(v ** 2)))
    elif v.ndim == 2 and v.shape[1] == 3:  
        return np.sqrt(np.sum(v ** 2, axis=1))
    else:
        raise ValueError("Input must be shape (3) or (N,3)")
    pass