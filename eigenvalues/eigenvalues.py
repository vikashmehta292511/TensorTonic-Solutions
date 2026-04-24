import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here

    if not isinstance(matrix, (list, np.ndarray)) or not all(isinstance(row, (list,     np.ndarray)) for row in matrix):
        return None
        
    if not all(len(row) == len(matrix) for row in matrix):
        return None
        
    mat = np.asarray(matrix, dtype=float)
    if mat.ndim != 2 or mat.shape[0] != mat.shape[1]:
        return None
        
    if mat.size == 0:
        return np.array([], dtype=float)
    vals = np.linalg.eigvals(mat)
    order = np.lexsort((vals.imag, vals.real))
    return vals[order]
    
    pass