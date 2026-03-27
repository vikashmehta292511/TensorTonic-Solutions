import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x     = np.asarray(x,     dtype=float)
    gamma = np.asarray(gamma, dtype=float)
    beta  = np.asarray(beta,  dtype=float)

    if x.ndim == 2:
        mu  = x.mean(axis=0, keepdims=True)
        var = x.var(axis=0,  keepdims=True)
        x_hat = (x - mu) / np.sqrt(var + eps)
        return gamma * x_hat + beta

    else: 
        mu  = x.mean(axis=(0, 2, 3), keepdims=True)
        var = x.var(axis=(0, 2, 3),  keepdims=True)
        x_hat = (x - mu) / np.sqrt(var + eps)
        return gamma.reshape(1, -1, 1, 1) * x_hat + beta.reshape(1, -1, 1, 1)
    pass