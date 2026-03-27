import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)

    if not np.allclose(p.sum(), 1.0, atol=1e-6):
        raise ValueError("Probabilities must sum to 1.")

    return float(np.dot(x, p))
    
    pass
