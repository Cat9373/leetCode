class Solution:
    def findMissingElements(self, nums):
        s = set(nums)

        ans = []

        for x in range(min(nums), max(nums) + 1):
            if x not in s:
                ans.append(x)

        return ans


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))

    sol = Solution()
    result = sol.findMissingElements(nums)

    print("Missing elements:", result)