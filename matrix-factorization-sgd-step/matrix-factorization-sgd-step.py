import numpy as np

def matrix_factorization_sgd_step(U: list, V: list, r: float, lr: float, reg: float) -> list:
    """
    Returns the updated user and item vectors in a two-item list.
    """
    # Write code here
    
    U = np.array(U, dtype=float)
    V = np.array(V, dtype=float)
    error = r - np.dot(U, V)
    U_new = U + lr * (error * V - reg * U)
    V_new = V + lr * (error * U - reg * V)
    U_new = [round(val, 4) for val in U_new]
    V_new = [round(val, 4) for val in V_new]
    return [U_new, V_new]