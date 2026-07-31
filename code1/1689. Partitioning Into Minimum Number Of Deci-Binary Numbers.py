class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


# Driver Code
if __name__ == "__main__":
    n = input("Enter the number: ")

    sol = Solution()
    result = sol.minPartitions(n)

    print("Minimum Number of Deci-Binary Numbers:", result)