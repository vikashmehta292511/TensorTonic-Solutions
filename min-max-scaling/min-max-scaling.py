def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    
    if len(data) == 0:
        raise ValueError("data must not empty")
    n_rows = len(data)
    n_cols = len(data[0])

    result = [[0.0] * n_cols for _ in range(n_rows)]

    for j in range(n_cols):
        col_values = [data[i][j] for i in range(n_rows)]
        min_val = min(col_values)
        max_val = max(col_values)
        range_val = max_val - min_val
        for i in range(n_rows):
            result[i][j] = 0.0 if range_val == 0 else (data[i][j] - min_val) / range_val

    return result