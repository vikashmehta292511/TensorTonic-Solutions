import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A, dtype=float)
    N, M = A.shape
    AT = np.zeros((M, N))
    for i in range(N):
        for j in range(M):
            AT[j, i] = A[i, j]
    return AT 
    pass
