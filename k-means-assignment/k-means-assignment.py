import numpy as np 

def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here

    points    = np.asarray(points,    dtype=float)
    centroids = np.asarray(centroids, dtype=float)
    
    assignments = []
    
    for point in points:
        best_idx  = 0
        best_dist = float('inf')
        
        for idx, centroid in enumerate(centroids):
            dist = np.sum((point - centroid) ** 2)
            
            if dist < best_dist:
                best_dist = dist
                best_idx  = idx
        
        assignments.append(best_idx)
    
    return assignments