import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Write code here

    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)

    q = q + eps

    mask = p > 0

    return float(np.sum(p[mask] * np.log(p[mask] / q[mask])))
    pass