from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums):
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]

            takeLeft = nums[i] - dp(i + 1, j)
            takeRight = nums[j] - dp(i, j - 1)

            return max(takeLeft, takeRight)

        return dp(0, len(nums) - 1) >= 0


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    print("Enter the elements separated by spaces:")
    nums = list(map(int, input().split()))

    if len(nums) != n:
        print(f"Error: Expected {n} elements, but got {len(nums)}.")
    else:
        sol = Solution()
        result = sol.predictTheWinner(nums)

        print("Can Player 1 Win?:", result)