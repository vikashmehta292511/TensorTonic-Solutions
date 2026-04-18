def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    # Your code here

    vocab = sorted(set(tokens))
    counts = {}
    for i in range(len(tokens) - 1):
        w1, w2 = tokens[i], tokens[i+1]
        counts[(w1, w2)] = counts.get((w1, w2), 0) + 1

    probs = {}
    V = len(vocab)
    for w1 in vocab:
        total = sum(counts.get((w1, v), 0) for v in vocab)
        denom = total + V
        for w2 in vocab:
            num = counts.get((w1, w2), 0) + 1
            probs[(w1, w2)] = num / denom

    return counts, probs
    
    pass