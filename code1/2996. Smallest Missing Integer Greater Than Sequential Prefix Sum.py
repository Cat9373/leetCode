class Solution:
    def missingInteger(self, nums):
        # Find the longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find the smallest missing number >= total
        s = set(nums)

        while total in s:
            total += 1

        return total


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements: ").split()))

    sol = Solution()
    result = sol.missingInteger(nums)

    print("Smallest missing integer:", result)