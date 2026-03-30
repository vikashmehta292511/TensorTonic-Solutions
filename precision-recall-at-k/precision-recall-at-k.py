def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here

    relevant = set(relevant)
    hits = sum(1 for item in recommended[:k] if item in relevant)
    return [hits / k, hits / len(relevant)]