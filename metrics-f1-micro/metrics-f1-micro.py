import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if y_true.shape != y_pred.shape:
        return none
        
    TP = np.sum(y_true == y_pred)
    FP = np.sum(y_pred != y_true)
    FN = FP 
    return float(2 * TP / (2 * TP + FP + FN))
    
    pass