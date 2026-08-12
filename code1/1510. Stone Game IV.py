class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            j = 1

            while j * j <= i:
                # If we can move to a losing position,
                # the current position is winning.
                if not dp[i - j * j]:
                    dp[i] = True
                    break

                j += 1

        return dp[n]


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter number of stones: "))

    sol = Solution()
    result = sol.winnerSquareGame(n)

    print("Can Alice win?", result)