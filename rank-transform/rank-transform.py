import numpy as np
def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here

    values = np.asarray(values, dtype=float)
    N = len(values)
    sorted_idx = np.argsort(values)
    ranks = np.zeros(N, dtype=float)
    i = 0
    while i < N:
        j = i
        while j + 1 < N and values[sorted_idx[j]] == values[sorted_idx[j+1]]:
            j += 1
        avg_rank = (i+1 + j+1) / 2.0
        for k in range(i, j+1):
            ranks[sorted_idx[k]] = avg_rank
        i = j + 1
    return ranks.tolist()