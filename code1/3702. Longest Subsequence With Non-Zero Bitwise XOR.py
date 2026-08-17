class Solution:
    def longestSubsequence(self, nums):
        xor = 0

        for num in nums:
            xor ^= num

        # XOR of the entire array is non-zero
        if xor != 0:
            return len(nums)

        # Total XOR is zero.
        # If there is a non-zero element, remove it.
        for num in nums:
            if num != 0:
                return len(nums) - 1

        # All elements are zero
        return 0


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))

    sol = Solution()
    result = sol.longestSubsequence(nums)

    print("Longest subsequence length:", result)