class Solution:
    def maximumAmount(self, coins):
        m = len(coins)
        n = len(coins[0])

        NEG = float('-inf')

        # dp[i][j][k] =
        # maximum profit reaching (i, j)
        # using k neutralizations
        dp = [[[NEG] * 3 for _ in range(n)] for _ in range(m)]

        # Starting cell
        value = coins[0][0]

        dp[0][0][0] = value

        if value < 0:
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                value = coins[i][j]

                for used in range(3):

                    # Come from top
                    if i > 0:
                        dp[i][j][used] = max(
                            dp[i][j][used],
                            dp[i - 1][j][used] + value
                        )

                    # Come from left
                    if j > 0:
                        dp[i][j][used] = max(
                            dp[i][j][used],
                            dp[i][j - 1][used] + value
                        )

                    # Neutralize this robber
                    if value < 0 and used > 0:

                        if i > 0:
                            dp[i][j][used] = max(
                                dp[i][j][used],
                                dp[i - 1][j][used - 1]
                            )

                        if j > 0:
                            dp[i][j][used] = max(
                                dp[i][j][used],
                                dp[i][j - 1][used - 1]
                            )

        return max(dp[m - 1][n - 1])


# Driver Code
if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    coins = []

    print("Enter the grid:")
    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        coins.append(row)

    sol = Solution()
    result = sol.maximumAmount(coins)

    print("Maximum amount:", result)