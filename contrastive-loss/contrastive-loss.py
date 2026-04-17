import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here

    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)

    if a.shape != b.shape:
        raise ValueError("a and b must have the same shape")
    if a.ndim == 1:
        a = a[np.newaxis, :]
        b = b[np.newaxis, :]
    if y.shape[0] != a.shape[0]:
        raise ValueError("y must have same length as number of pairs")
    if not np.all(np.isin(y, [0, 1])):
        raise ValueError("y must contain only 0 or 1")

    d = np.linalg.norm(a - b, axis=1)
    loss = y * (d ** 2) + (1 - y) * (np.maximum(0.0, margin - d) ** 2)

    if reduction == "mean":
        return float(loss.mean())
    elif reduction == "sum":
        return float(loss.sum())
    else:
        raise ValueError("reduction must be 'mean' or 'sum'")
        
    pass