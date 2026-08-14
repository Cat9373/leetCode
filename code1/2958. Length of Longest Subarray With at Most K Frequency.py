class Solution:
    def maxSubarrayLength(self, nums, k):
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # If the current element occurs more than k times,
            # shrink the window from the left.
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    k = int(input("Enter k: "))

    sol = Solution()
    result = sol.maxSubarrayLength(nums, k)

    print("Longest good subarray length:", result)