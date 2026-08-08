import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here
    
    p = np.array(points, float)
    c, s = np.cos(theta), np.sin(theta)
    if p.ndim == 1:
        x, y, z = p
        return np.array([x*c - y*s, x*s + y*c, z])
    x, y, z = p[:,0], p[:,1], p[:,2]
    return np.column_stack([x*c - y*s, x*s + y*c, z])
    pass