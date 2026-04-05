import numpy as np 

def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here

    points    = np.asarray(points,    dtype=float)
    centroids = np.asarray(centroids, dtype=float)
    
    sq_dists = ((points[:, np.newaxis, :] - centroids[np.newaxis, :, :]) ** 2).sum(axis=2)
    
    return np.argmin(sq_dists, axis=1).tolist()