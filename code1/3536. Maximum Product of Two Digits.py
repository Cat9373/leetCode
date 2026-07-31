class Solution:
    def maxProduct(self, n: int) -> int:
        first = second = 0

        while n:
            digit = n % 10
            if digit >= first:
                second = first
                first = digit
            elif digit > second:
                second = digit
            n //= 10

        return first * second


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter an integer: "))

    sol = Solution()
    result = sol.maxProduct(n)

    print("Maximum Product of Two Digits:", result)