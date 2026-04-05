import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here

    X = np.asarray(X, dtype=float)
    
    mean = X.mean(axis=0)
    X_centered = X - mean
    
    n_samples = len(X)
    cov = X_centered.T @ X_centered / (n_samples - 1)
    
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    
    sorted_indices = np.argsort(eigenvalues)[::-1]
    top_k_indices = sorted_indices[:k]
    top_k_components = eigenvectors[:, top_k_indices]
    
    X_projected = X_centered @ top_k_components
    
    return X_projected.tolist()