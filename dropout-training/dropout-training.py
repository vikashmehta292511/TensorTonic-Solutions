import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    
    x = np.asarray(x, dtype=float)
    if p < 0.0 or p >= 1.0:
        raise ValueError("Dropout probability p must be in [0, 1).")

    if rng is None:
        rand = np.random.random(x.shape)
    else:
        rand = rng.random(x.shape)
    keep_mask = rand >= p
    scale = 1.0 / (1.0 - p) if p < 1.0 else 0.0
    pattern = keep_mask.astype(float) * scale
    output = x * pattern
    return output, pattern
    
    pass