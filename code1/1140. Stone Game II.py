from functools import lru_cache


class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, M):
            # No piles remaining
            if i >= n:
                return 0

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                opponent = dp(i + X, max(M, X))

                current = suffix[i] - opponent

                best = max(best, current)

            return best

        return dp(0, 1)


# Driver Code
if __name__ == "__main__":
    piles = list(map(int, input("Enter the piles: ").split()))

    sol = Solution()
    result = sol.stoneGameII(piles)

    print("Maximum stones Alice can get:", result)