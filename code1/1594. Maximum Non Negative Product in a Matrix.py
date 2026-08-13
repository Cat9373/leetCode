class Solution:
    def maxProductPath(self, grid):
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                value = grid[i][j]

                candidates = []

                if i > 0:
                    candidates.append(
                        max_dp[i - 1][j] * value
                    )
                    candidates.append(
                        min_dp[i - 1][j] * value
                    )

                if j > 0:
                    candidates.append(
                        max_dp[i][j - 1] * value
                    )
                    candidates.append(
                        min_dp[i][j - 1] * value
                    )

                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)

        result = max_dp[m - 1][n - 1]

        if result < 0:
            return -1

        return result % MOD


# Driver Code
if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    grid = []

    print("Enter the grid:")
    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        grid.append(row)

    sol = Solution()
    result = sol.maxProductPath(grid)

    print("Maximum non-negative product:", result)