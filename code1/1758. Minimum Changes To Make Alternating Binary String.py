class Solution:
    def minOperations(self, s: str) -> int:
        startWith0 = 0
        startWith1 = 0

        for i, ch in enumerate(s):
            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'

            if ch != expected0:
                startWith0 += 1

            if ch != expected1:
                startWith1 += 1

        return min(startWith0, startWith1)


# Driver Code
if __name__ == "__main__":
    s = input("Enter the binary string: ")

    sol = Solution()
    result = sol.minOperations(s)

    print("Minimum Operations Required:", result)