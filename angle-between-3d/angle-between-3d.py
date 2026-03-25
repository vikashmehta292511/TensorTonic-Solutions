import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    
    v = np.asarray(v, dtype=float)
    w = np.asarray(w, dtype=float)

    nv = np.linalg.norm(v)
    nw = np.linalg.norm(w)

    if nv < 1e-10 or nw < 1e-10:
        return np.nan

    cos_theta = np.clip(np.dot(v, w) / (nv * nw), -1.0, 1.0)
    return float(np.arccos(cos_theta))
    
    pass