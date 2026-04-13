import numpy as np
def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here

    p = np.asarray(predictions, dtype=float)
    K = len(p)

    q = np.full(K, epsilon / K)
    q[target] = (1 - epsilon) + (epsilon / K)

    loss = -np.sum(q * np.log(p + 1e-12))
    return float(loss)