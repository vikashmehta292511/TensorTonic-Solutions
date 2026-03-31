import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here

    
    T      = np.asarray(T,      dtype=float)
    points = np.asarray(points, dtype=float)
    single = points.ndim == 1
    points = points.reshape(-1, 3)

    ones   = np.ones((len(points), 1))
    ph     = np.hstack([points, ones])        
    result = (T @ ph.T).T[:, :3]              

    return result[0] if single else result
    
    
    pass