import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    
    A = np.asarray(A, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None
    
    if abs(np.linalg.det(A)) < 1e-10:
        return None
    A_inv = np.linalg.inv(A)
    I = np.eye(A.shape[0])
    
    if np.linalg.norm(A @ A_inv - I) >= 1e-7:
        return None
    return A_inv
    
    pass
