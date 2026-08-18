import numpy as np 
def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    # Write code here

    R = np.array(ratings_matrix, dtype=float)
    imputed = R.copy()
    num_users, num_items = R.shape
    if mode == "user":
        for i in range(num_users):
            row = R[i]
            nonzero_ratings = [val for val in row if val != 0]
            if len(nonzero_ratings) > 0:
                mean_val = sum(nonzero_ratings) / len(nonzero_ratings)
                for j in range(num_items):
                    if row[j] == 0:
                        imputed[i][j] = mean_val
    elif mode == "item":
        for j in range(num_items):
            col_values = [R[i][j] for i in range(num_users) if R[i][j] != 0]
            if len(col_values) > 0:
                mean_val = sum(col_values) / len(col_values)
                for i in range(num_users):
                    if R[i][j] == 0:
                        imputed[i][j] = mean_val
    else:
        raise ValueError("mode must user or item")
    return imputed.tolist()