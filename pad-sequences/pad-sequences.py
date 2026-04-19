import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    N = len(seqs)
    if N == 0:
        return np.zeros((0, 0), dtype=int)

    if max_len is None:
        max_len = max((len(s) for s in seqs), default=0)

    out = np.full((N, max_len), pad_value, dtype=int)

    for i, seq in enumerate(seqs):
        length = min(len(seq), max_len)
        out[i, :length] = seq[:length]

    return out
    
    pass