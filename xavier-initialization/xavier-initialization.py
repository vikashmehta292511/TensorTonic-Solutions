import numpy as np
def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    W = np.asarray(W, dtype=float)
    L = np.sqrt(6 / (fan_in + fan_out))
    return (W * 2 * L - L).tolist()