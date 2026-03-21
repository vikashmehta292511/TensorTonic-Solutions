import numpy as np
def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    x = np.asarray(values, dtype=float)
    n = len(x)
    s = np.sort(x)


    if n % 2 == 1:
        median = s[n // 2]
    else:
        median = (s[n // 2 - 1] + s[n // 2]) / 2

    
    lower = s[:n // 2]
    upper = s[n - n // 2:]

    q1 = np.median(lower) if len(lower) > 0 else median
    q3 = np.median(upper) if len(upper) > 0 else median
    iqr = q3 - q1

    if iqr == 0:
        return (x - median).tolist()
    return ((x - median) / iqr).tolist()