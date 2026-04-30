import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    # Write code here

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if y_true.shape != y_pred.shape:
        return None

    labels = np.unique(np.concatenate([y_true, y_pred]))
    K = len(labels)
    label_to_idx = {label: idx for idx, label in enumerate(labels)}

    cm = np.zeros((K, K), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[label_to_idx[t], label_to_idx[p]] += 1

    TP = np.diag(cm)
    FP = cm.sum(axis=0) - TP
    FN = cm.sum(axis=1) - TP
    support = cm.sum(axis=1)

    accuracy = float((TP.sum()) / len(y_true))

    if average == "micro":
        TP_sum, FP_sum, FN_sum = TP.sum(), FP.sum(), FN.sum()
        precision = TP_sum / (TP_sum + FP_sum) if TP_sum + FP_sum > 0 else 0.0
        recall = TP_sum / (TP_sum + FN_sum) if TP_sum + FN_sum > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0.0

    elif average == "macro":
        prec = np.divide(TP, TP + FP, out=np.zeros_like(TP, dtype=float), where=(TP+FP)!=0)
        rec = np.divide(TP, TP + FN, out=np.zeros_like(TP, dtype=float), where=(TP+FN)!=0)
        f1s = np.divide(2*prec*rec, prec+rec, out=np.zeros_like(prec, dtype=float), where=(prec+rec)!=0)
        precision, recall, f1 = prec.mean(), rec.mean(), f1s.mean()

    elif average == "weighted":
        prec = np.divide(TP, TP + FP, out=np.zeros_like(TP, dtype=float), where=(TP+FP)!=0)
        rec = np.divide(TP, TP + FN, out=np.zeros_like(TP, dtype=float), where=(TP+FN)!=0)
        f1s = np.divide(2*prec*rec, prec+rec, out=np.zeros_like(prec, dtype=float), where=(prec+rec)!=0)
        weights = support / support.sum()
        precision = (prec * weights).sum()
        recall = (rec * weights).sum()
        f1 = (f1s * weights).sum()

    elif average == "binary":
        if pos_label not in label_to_idx:
            return None
        idx = label_to_idx[pos_label]
        tp, fp, fn = TP[idx], FP[idx], FN[idx]
        precision = tp / (tp + fp) if tp + fp > 0 else 0.0
        recall = tp / (tp + fn) if tp + fn > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0.0
    else:
        return None

    return {
        "accuracy": accuracy,
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1)
    }
    
    pass