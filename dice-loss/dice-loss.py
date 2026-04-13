import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here

    p = np.asarray(p, dtype=float).flatten()
    y = np.asarray(y, dtype=float).flatten()

    intersection = np.sum(p * y)
    sum_p = np.sum(p)
    sum_y = np.sum(y)

    dice_coeff = (2 * intersection + eps) / (sum_p + sum_y + eps)
    return 1.0 - dice_coeff
    
    pass