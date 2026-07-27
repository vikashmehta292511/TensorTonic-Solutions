def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here

    if len(values) == 0:
        raise ValueError("values must not empty")

    total = len(values)
    counts = {}
    for v in values:
        if v not in counts:
            counts[v] = 0
        counts[v] = counts[v] + 1
    freqs = {}
    for v in counts:
        freqs[v] = counts[v] / total
    result = []
    for v in values:
        result.append(freqs[v])

    return result