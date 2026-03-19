import numpy as np 
def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    # Write code here
    m, n = len(s1), len(s2)
    dp = np.arange(n + 1, dtype=int).reshape(1, -1).repeat(m + 1, axis=0)
    dp[:, 0] = np.arange(m + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i, j] = dp[i - 1, j - 1]
            else:
                dp[i, j] = 1 + min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1])

    return int(dp[m, n])