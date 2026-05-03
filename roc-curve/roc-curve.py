import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    # Write code here

    y_true = np.asarray(y_true, dtype=int)
    y_score = np.asarray(y_score, dtype=float)
    if y_true.shape != y_score.shape or y_true.ndim != 1:
        return None
        
    order = np.argsort(-y_score, kind="mergesort")
    y_true_sorted = y_true[order]
    y_score_sorted = y_score[order]
    P = np.sum(y_true_sorted == 1)
    N = np.sum(y_true_sorted == 0)
    tp_cum = np.cumsum(y_true_sorted == 1)
    fp_cum = np.cumsum(y_true_sorted == 0)
    distinct_indices = np.where(np.diff(y_score_sorted))[0]
    threshold_indices = np.r_[distinct_indices, y_true_sorted.size - 1]
    
    tpr = tp_cum[threshold_indices] / P if P > 0 else np.zeros_like(threshold_indices, dtype=float)
    fpr = fp_cum[threshold_indices] / N if N > 0 else np.zeros_like(threshold_indices, dtype=float)
    thresholds = y_score_sorted[threshold_indices]
    tpr = np.r_[0.0, tpr]
    fpr = np.r_[0.0, fpr]
    thresholds = np.r_[np.inf, thresholds]
    
    return fpr.tolist(), tpr.tolist(), thresholds.tolist()
    
    pass