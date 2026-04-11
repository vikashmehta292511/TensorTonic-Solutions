import numpy as np

def decision_tree_split(X, y):
    """
    Find the best feature and threshold to split the data.
    """
    # Write code here

    X = np.array(X, dtype=float)
    y = np.array(y)

    def gini(labels):
        
        if len(labels) == 0:
            return 0.0
        _, counts = np.unique(labels, return_counts=True)
        probs = counts / len(labels)
        return 1.0 - np.sum(probs ** 2)

    n_samples, n_features = X.shape
    parent_gini = gini(y)

    best_gain = -1.0
    best_feature = None
    best_threshold = None

    
    for f in range(n_features):
        
        values = sorted(set(X[:, f]))
        
        thresholds = [(values[i] + values[i+1]) / 2 for i in range(len(values)-1)]

        for t in thresholds:
            left_mask = X[:, f] <= t
            right_mask = ~left_mask

            if not left_mask.any() or not right_mask.any():
                continue  

            gini_left = gini(y[left_mask])
            gini_right = gini(y[right_mask])

            
            gini_split = (np.sum(left_mask) / n_samples) * gini_left + \
                         (np.sum(right_mask) / n_samples) * gini_right

            gain = parent_gini - gini_split

            
            if (gain > best_gain or
                (gain == best_gain and (best_feature is None or f < best_feature)) or
                (gain == best_gain and f == best_feature and (best_threshold is None or t < best_threshold))):
                best_gain = gain
                best_feature = f
                best_threshold = t

    return [best_feature, best_threshold]