import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here
    
    k = min(k, len(relevance_scores))

    def dcg(scores):
        return sum((2 ** r - 1) / math.log2(i + 2)
                   for i, r in enumerate(scores[:k]))

    actual = dcg(relevance_scores)
    ideal  = dcg(sorted(relevance_scores, reverse=True))

    return actual / ideal if ideal > 0 else 0.0
    pass