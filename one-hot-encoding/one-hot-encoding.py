import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here

    y = np.asarray(y, dtype=int)
    if num_classes is None:
        num_classes = int(y.max()) + 1
    if np.any(y < 0) or np.any(y >= num_classes):
        raise ValueError("labels out of range for num classes")
    N = len(y)
    Y = np.zeros((N, num_classes), dtype=float)
    Y[np.arange(N), y] = 1.0
    return Y
    pass