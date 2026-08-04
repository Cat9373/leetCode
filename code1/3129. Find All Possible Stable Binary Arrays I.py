from functools import lru_cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(z, o, last):
            if z == 0:
                return 1 if last == 1 and o <= limit else 0
            if o == 0:
                return 1 if last == 0 and z <= limit else 0

            if last == 0:
                res = dfs(z - 1, o, 0) + dfs(z - 1, o, 1)
                if z > limit:
                    res -= dfs(z - limit - 1, o, 1)
            else:
                res = dfs(z, o - 1, 0) + dfs(z, o - 1, 1)
                if o > limit:
                    res -= dfs(z, o - limit - 1, 0)

            return res % MOD

        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD


# Driver Code
if __name__ == "__main__":
    zero = int(input("Enter the number of zeros: "))
    one = int(input("Enter the number of ones: "))
    limit = int(input("Enter the limit: "))

    sol = Solution()
    result = sol.numberOfStableArrays(zero, one, limit)

    print("Number of Stable Arrays:", result)