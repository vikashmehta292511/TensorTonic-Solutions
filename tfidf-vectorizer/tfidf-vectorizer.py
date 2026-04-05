import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here

    tokenized = [doc.lower().split() for doc in documents]
    
    vocab = sorted(set(word for doc in tokenized for word in doc))
    word_to_idx = {word: idx for idx, word in enumerate(vocab)}
    
    num_docs = len(documents)
    num_words = len(vocab)
    matrix = np.zeros((num_docs, num_words))
    
    for doc_idx, tokens in enumerate(tokenized):
        total_terms = len(tokens)
        if total_terms == 0:
            continue
        
        term_counts = Counter(tokens)
        
        for word, count in term_counts.items():
            matrix[doc_idx, word_to_idx[word]] = count / total_terms
    
    doc_freq = np.sum(matrix > 0, axis=0)
    idf = np.array([math.log(num_docs / df) if df > 0 else 0 for df in doc_freq])
    
    tfidf_matrix = matrix * idf
    
    return tfidf_matrix, vocab
    
    pass