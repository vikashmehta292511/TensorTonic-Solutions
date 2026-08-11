import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here

    X, y = np.asarray(X), np.asarray(y)
    if batch_size <= 0:
        raise ValueError("batch size be > 0")
    n = len(y)
    idx = np.arange(n)
    idx = rng.permutation(idx) if rng is not None else np.random.permutation(idx)
    for i in range(0, n, batch_size):
        b = idx[i:i+batch_size]
        if drop_last and len(b) < batch_size:
            break
        yield X[b], y[b]
    pass