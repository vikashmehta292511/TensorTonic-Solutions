import numpy as np

def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    # Write code here

    if len(candidate) == 0:
        return 0.0

    precisions = []
    for n in range(1, max_n + 1):
        cand_ngrams = {}
        ref_ngrams = {}

        for i in range(len(candidate) - n + 1):
            ng = tuple(candidate[i:i+n])
            cand_ngrams[ng] = cand_ngrams.get(ng, 0) + 1

        for i in range(len(reference) - n + 1):
            ng = tuple(reference[i:i+n])
            ref_ngrams[ng] = ref_ngrams.get(ng, 0) + 1

        match = 0
        total = sum(cand_ngrams.values())
        for ng, c_count in cand_ngrams.items():
            r_count = ref_ngrams.get(ng, 0)
            match += min(c_count, r_count)

        if total == 0 or match == 0:
            return 0.0
        precisions.append(match / total)

    log_precisions = np.log(precisions)
    geo_mean = np.exp(np.mean(log_precisions))

    c_len = len(candidate)
    r_len = len(reference)
    bp = 1.0 if c_len >= r_len else np.exp(1 - r_len / c_len)

    return float(bp * geo_mean)