class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float("-inf")
            take = 0

            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    dp[i] = max(dp[i], take - dp[i + k + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of stones: "))

    print("Enter the stone values separated by spaces:")
    stoneValue = list(map(int, input().split()))

    if len(stoneValue) != n:
        print(f"Error: Expected {n} stone values, but got {len(stoneValue)}.")
    else:
        sol = Solution()
        result = sol.stoneGameIII(stoneValue)

        print("Winner:", result)