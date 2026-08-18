class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] = maximum score Alice can get
        dp = [[0] * n for _ in range(n)]

        INF = float('-inf')

        rowMax = [[INF] * n for _ in range(n)]
        colMax = [[INF] * n for _ in range(n)]

        # Base cases
        for i in range(n):
            rowMax[i][i] = prefix[i + 1]
            colMax[i][i] = -prefix[i]

        # Increasing subarray length
        for length in range(2, n + 1):

            for l in range(n - length + 1):
                r = l + length - 1

                total = prefix[r + 1] - prefix[l]

                # Binary search for first split where
                # left_sum >= right_sum
                lo = l
                hi = r - 1

                while lo < hi:
                    mid = (lo + hi) // 2

                    left_sum = prefix[mid + 1] - prefix[l]

                    if 2 * left_sum >= total:
                        hi = mid
                    else:
                        lo = mid + 1

                k = lo

                best = 0

                # left_sum < right_sum
                if k > l:
                    best = max(
                        best,
                        rowMax[l][k - 1] - prefix[l]
                    )

                # Check split at k
                left_sum = prefix[k + 1] - prefix[l]
                right_sum = prefix[r + 1] - prefix[k + 1]

                if left_sum < right_sum:
                    best = max(
                        best,
                        left_sum + dp[l][k]
                    )

                elif left_sum > right_sum:
                    best = max(
                        best,
                        right_sum + dp[k + 1][r]
                    )

                else:
                    best = max(
                        best,
                        left_sum + dp[l][k],
                        right_sum + dp[k + 1][r]
                    )

                # right_sum < left_sum
                if k + 1 <= r - 1:
                    best = max(
                        best,
                        prefix[r + 1] + colMax[r][k + 2]
                    )

                dp[l][r] = best

                # Update row maximum
                rowMax[l][r] = max(
                    rowMax[l][r - 1],
                    dp[l][r] + prefix[r + 1]
                )

                # Update column maximum
                colMax[r][l] = max(
                    colMax[r][l + 1],
                    dp[l][r] - prefix[l]
                )

        return dp[0][n - 1]


# Driver Code
if __name__ == "__main__":
    stoneValue = list(
        map(int, input("Enter the stone values: ").split())
    )

    sol = Solution()
    result = sol.stoneGameV(stoneValue)

    print("Maximum score:", result)