class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        dp0[0][0] = dp1[0][0] = 1

        for i in range(zero + 1):
            for j in range(one + 1):

                if i:
                    dp0[i][j] = (dp0[i][j] + dp1[i - 1][j]) % MOD
                    if i > limit:
                        dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j]) % MOD
                    if i > 1:
                        dp0[i][j] = (dp0[i][j] + dp0[i - 1][j]) % MOD

                if j:
                    dp1[i][j] = (dp1[i][j] + dp0[i][j - 1]) % MOD
                    if j > limit:
                        dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1]) % MOD
                    if j > 1:
                        dp1[i][j] = (dp1[i][j] + dp1[i][j - 1]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD


# Driver Code
if __name__ == "__main__":
    zero = int(input("Enter the number of zeros: "))
    one = int(input("Enter the number of ones: "))
    limit = int(input("Enter the limit: "))

    sol = Solution()
    result = sol.numberOfStableArrays(zero, one, limit)

    print("Number of Stable Arrays:", result)