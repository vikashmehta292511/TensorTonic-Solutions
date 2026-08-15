import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here

    values = np.asarray(values, dtype=float)
    min_val, max_val = np.min(values), np.max(values)
    if min_val == max_val:
        return [0] * len(values)
    bin_width = (max_val - min_val) / num_bins
    bins = []
    for v in values:
        idx = int((v - min_val) / bin_width)
        idx = min(idx, num_bins - 1)
        bins.append(idx)
    return bins