import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here

    tokens = np.asarray(tokens, dtype=object)
    vocab = np.asarray(vocab, dtype=object)
    vocab_index = {word: i for i, word in enumerate(vocab)}
    bow = np.zeros(len(vocab), dtype=int)
    for t in tokens:
        if t in vocab_index:
            bow[vocab_index[t]] += 1
    return bow
    
    pass