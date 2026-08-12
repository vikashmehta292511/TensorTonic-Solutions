import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    # Write code here

    if not (2 <= k <= N):
        raise ValueError("require 2 <= k <= N")

    idx = np.arange(N)
    if shuffle:
        idx = rng.permutation(idx) if rng is not None else np.random.permutation(idx)
    folds = np.array_split(idx, k)
    splits = []
    for i in range(k):
        val_idx = folds[i].astype(int)
        if k > 1:
            train_idx = np.concatenate([folds[j] for j in range(k) if j != i]).astype(int)
        else:
            train_idx = np.array([], dtype=int)
        splits.append((train_idx, val_idx))
    return splits
    pass
