import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here

    anchor   = np.asarray(anchor,   dtype=float)
    positive = np.asarray(positive, dtype=float)
    negative = np.asarray(negative, dtype=float)
    
    if anchor.ndim == 1:
        anchor   = anchor.reshape(1, -1)
        positive = positive.reshape(1, -1)
        negative = negative.reshape(1, -1)
    
    dist_pos = np.sum((anchor - positive) ** 2, axis=1)
    dist_neg = np.sum((anchor - negative) ** 2, axis=1)
    
    losses = np.maximum(0, dist_pos - dist_neg + margin)
    
    return float(np.mean(losses))
    
    pass