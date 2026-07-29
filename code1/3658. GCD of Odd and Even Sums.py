class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))

    sol = Solution()
    result = sol.gcdOfOddEvenSums(n)

    print("GCD of Odd and Even Sums:", result)