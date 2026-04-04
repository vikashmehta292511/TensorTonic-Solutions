import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here

    X = np.asarray(X, dtype=float)
    X_centered = X - X.mean(axis=0)
    cov = X_centered.T @ X_centered / (len(X) - 1)

    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    
    top_k = eigenvectors[:, ::-1][:, :k]
    
    return (X_centered @ top_k).tolist()