class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        bits = 0

        for i in range(1, n + 1):
            # Increase bit length when i is a power of 2
            if (i & (i - 1)) == 0:
                bits += 1

            ans = ((ans << bits) + i) % MOD

        return ans


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))

    sol = Solution()
    result = sol.concatenatedBinary(n)

    print("Concatenated Binary Value:", result)