def baseline_predict(ratings_matrix: list, target_pairs: list) -> list:
    """
    Returns the baseline predictions for the requested user-item pairs.
    """
    # Write code here

    all_ratings = [r for row in ratings_matrix for r in row if r != 0]
    mu = sum(all_ratings) / len(all_ratings)
    n_users = len(ratings_matrix)
    n_items = len(ratings_matrix[0])

    user_biases = []
    for u in range(n_users):
        u_ratings = [r for r in ratings_matrix[u] if r != 0]
        if u_ratings:
            user_biases.append(sum(u_ratings) / len(u_ratings) - mu)
        else:
            user_biases.append(0.0)
    item_biases = []
    for i in range(n_items):
        i_ratings = [ratings_matrix[u][i] for u in range(n_users) if ratings_matrix[u][i] != 0]
        if i_ratings:
            item_biases.append(sum(i_ratings) / len(i_ratings) - mu)
        else:
            item_biases.append(0.0)

    predictions = []
    for u, i in target_pairs:
        predictions.append(mu + user_biases[u] + item_biases[i])
    return predictions
    
    pass