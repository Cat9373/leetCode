class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        mask = 1
        while mask <= n:
            mask <<= 1

        return (mask - 1) ^ n


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter an integer: "))

    sol = Solution()
    result = sol.bitwiseComplement(n)

    print("Bitwise Complement:", result)