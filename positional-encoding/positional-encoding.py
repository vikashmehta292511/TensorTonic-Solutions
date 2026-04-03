import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here

    n_sin = (d_model + 1) // 2  
    n_cos = d_model // 2          

    pos    = np.arange(seq_len).reshape(-1, 1)
    i_sin  = np.arange(n_sin).reshape(1, -1)
    i_cos  = np.arange(n_cos).reshape(1, -1)

    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(pos / base ** (2 * i_sin / d_model))
    pe[:, 1::2] = np.cos(pos / base ** (2 * i_cos / d_model))

    return pe
    pass