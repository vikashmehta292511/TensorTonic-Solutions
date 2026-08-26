import numpy as np 
def rating_normalization(matrix: list) -> list:
    """
    Returns the mean-centered user-item matrix.
    """
    # Write code here

    R = np.array(matrix, dtype=float)
    normalized = R.copy()
    num_users, num_items = R.shape

    for i in range(num_users):
        row = R[i]
        nonzero_ratings = [val for val in row if val != 0]
        if len(nonzero_ratings) > 0:
            mean_val = sum(nonzero_ratings) / len(nonzero_ratings)
            for j in range(num_items):
                if row[j] != 0:
                    normalized[i][j] = round(row[j] - mean_val, 6)
                else:
                    normalized[i][j] = 0.0
        else:
            normalized[i] = [0.0] * num_items
    return normalized.tolist()
    pass