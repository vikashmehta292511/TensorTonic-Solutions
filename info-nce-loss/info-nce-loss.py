import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here

    Z1 = np.asarray(Z1, dtype=float)
    Z2 = np.asarray(Z2, dtype=float)
    
    if Z1.ndim != 2 or Z2.ndim != 2 or Z1.shape != Z2.shape or temperature <= 0:
        return None
        
    S = (Z1 @ Z2.T) / temperature
    S_max = np.max(S, axis=1, keepdims=True)
    S_stable = S - S_max
    exp_S = np.exp(S_stable)
    denom = np.sum(exp_S, axis=1)
    exp_pos = np.exp(np.diag(S_stable))
    
    return float(-np.mean(np.log(exp_pos / denom)))
    
    pass