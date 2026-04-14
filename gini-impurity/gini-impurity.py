import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here

    def gini(labels):
        if len(labels) == 0:
            return 0.0
        _, counts = np.unique(labels, return_counts=True)
        probs = counts / len(labels)
        return 1.0 - np.sum(probs ** 2)

    y_left = np.asarray(y_left)
    y_right = np.asarray(y_right)

    N_left, N_right = len(y_left), len(y_right)
    N = N_left + N_right

    if N == 0:
        return 0.0

    gini_left = gini(y_left)
    gini_right = gini(y_right)

    return (N_left / N) * gini_left + (N_right / N) * gini_right
    
    pass