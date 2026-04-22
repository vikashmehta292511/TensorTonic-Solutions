import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here

    mat = np.asarray(matrix, dtype=float)
    if mat.ndim != 2:
        return None
    if axis is not None and (axis < 0 or axis >= mat.ndim):
        return None

    if norm_type == 'l1':
        norms = np.sum(np.abs(mat), axis=axis, keepdims=True)
    elif norm_type == 'l2':
        norms = np.sqrt(np.sum(mat**2, axis=axis, keepdims=True))
    elif norm_type == 'max':
        norms = np.max(np.abs(mat), axis=axis, keepdims=True)
    else:
        return None

    norms[norms == 0] = 1.0
    return mat / norms
    
    pass