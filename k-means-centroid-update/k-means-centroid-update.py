import numpy as np

def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here

    points      = np.asarray(points,      dtype=float)
    assignments = np.asarray(assignments, dtype=int)
    D           = points.shape[1]

    centroids = np.zeros((k, D))
    counts    = np.zeros(k)

    np.add.at(centroids, assignments, points)
    np.add.at(counts,    assignments, 1)

    mask = counts > 0
    centroids[mask] /= counts[mask, np.newaxis]

    return centroids.tolist()