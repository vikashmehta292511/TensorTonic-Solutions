import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p = np.clip(np.asarray(p, dtype=float), 1e-15, 1 - 1e-15)
    y = np.asarray(y, dtype=float)

    term1 = (1 - p) ** gamma * y * np.log(p)
    term2 = p ** gamma * (1 - y) * np.log(1 - p)

    return float(-np.mean(term1 + term2))
    pass