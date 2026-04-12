import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.asarray(g, dtype=float)
    norm = np.linalg.norm(g)

    if norm == 0 or max_norm <= 0:
        return g.copy()

    if norm <= max_norm:
        return g.copy()
    else:
        scale = max_norm / norm
        return g * scale
        
    pass