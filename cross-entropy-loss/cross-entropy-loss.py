import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=float)

    correct_probs = y_pred[np.arange(len(y_true)), y_true]
    return float(-np.mean(np.log(correct_probs)))
    pass