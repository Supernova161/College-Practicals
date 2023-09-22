def all_lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D table to store the length of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the length of LCS
    lcs_length = dp[m][n]

    # Reconstruct the LCS itself
    lcs_sequence = [""] * lcs_length
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_sequence[lcs_length - 1] = X[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Function to find all common subsequences
    def find_all_lcs(i, j):
        if i == 0 or j == 0:
            return [""]
        if X[i - 1] == Y[j - 1]:
            lcs = find_all_lcs(i - 1, j - 1)
            for idx in range(len(lcs)):
                lcs[idx] += X[i - 1]
            return lcs
        if dp[i - 1][j] > dp[i][j - 1]:
            return find_all_lcs(i - 1, j)
        if dp[i][j - 1] > dp[i - 1][j]:
            return find_all_lcs(i, j - 1)
        top = find_all_lcs(i - 1, j)
        left = find_all_lcs(i, j - 1)
        return top + left

    # Find all common subsequences
    common_subsequences = find_all_lcs(m, n)

    return "".join(lcs_sequence), common_subsequences

# Example usage:
X = "AGGTAB"
Y = "GXTXAYB"
lcs_sequence, common_subsequences = all_lcs(X, Y)
print("Sequence X:", X)
print("Sequence Y:", Y)
print("Longest Common Subsequence:", lcs_sequence)
print("All Common Subsequences:", common_subsequences)