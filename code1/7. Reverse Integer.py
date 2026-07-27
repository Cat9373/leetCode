class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow
            if rev > (INT_MAX - digit) // 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev


# Driver Code
if __name__ == "__main__":
    x = int(input("Enter an integer: "))

    sol = Solution()
    result = sol.reverse(x)

    print("Reversed Integer:", result)