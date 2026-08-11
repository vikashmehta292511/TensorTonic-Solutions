import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    """
    Split features X and labels y into train/test while preserving class proportions.
    """
    # Write code here
    X, y = np.asarray(X), np.asarray(y)
    train_idx, test_idx = [], []
    for c in sorted(set(y.tolist())):
        idx = np.where(y == c)[0].copy()
        if rng is not None:
            idx = rng.permutation(idx)
        n_test = int(round(len(idx) * test_size))
        if n_test >= len(idx) and len(idx) > 1:
            n_test = len(idx) - 1
        test_idx.extend(idx[:n_test].tolist())
        train_idx.extend(idx[n_test:].tolist())
    train_idx = np.array(sorted(train_idx), dtype=int)
    test_idx = np.array(sorted(test_idx), dtype=int)
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]