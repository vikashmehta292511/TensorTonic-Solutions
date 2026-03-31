import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here

    v = np.asarray(v, dtype=float)
    single = v.ndim == 1
    v = v.reshape(-1, 3)

    norms = np.linalg.norm(v, axis=1, keepdims=True)
    mask = norms > 1e-10
    result = np.where(mask, v / np.where(mask, norms, 1), 0.0)

    return result[0] if single else result
    pass