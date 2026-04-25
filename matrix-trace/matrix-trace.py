import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here

    A = np.asarray(A)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None
        
    N = A.shape[0]
    trace_val = 0
    for i in range(N):
        trace_val += A[i, i]
        
    return trace_val
    
    pass
