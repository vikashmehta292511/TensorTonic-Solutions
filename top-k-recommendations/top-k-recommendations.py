import numpy as np
def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    scores = np.asarray(scores, dtype=float)
    mask   = np.ones(len(scores), dtype=bool)
    mask[list(rated_indices)] = False

    unrated_idx = np.where(mask)[0]
    top_k = unrated_idx[np.argsort(-scores[unrated_idx])][:k]
    return top_k.tolist()