def stoneGameVIII(stones):
    n = len(stones)

    # Prefix sums
    prefix = [0] * n
    prefix[0] = stones[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + stones[i]

    # Start with the total sum.
    dp = prefix[n - 1]

    # Consider possible positions from right to left.
    for i in range(n - 2, 0, -1):
        dp = max(dp, prefix[i] - dp)

    return dp


# Example 1
stones = [-1, 2, -3, 4, -5]

print(stoneGameVIII(stones))