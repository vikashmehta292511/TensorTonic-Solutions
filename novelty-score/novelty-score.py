import math

def novelty_score(recommendations: list, item_counts: list, n_users: int) -> float:
    """
    Returns the average self-information of the recommended items.
    """
    # Write code here

    if not recommendations:
        return 0.0
    total = 0.0
    for item in recommendations:
        popularity = item_counts[item] / n_users
        total += -math.log2(popularity)
    return total / len(recommendations)
    pass