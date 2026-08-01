class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[0] * nums[1] * nums[-1])


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    print("Enter the elements separated by spaces:")
    nums = list(map(int, input().split()))

    if len(nums) != n:
        print(f"Error: Expected {n} elements, but got {len(nums)}.")
    else:
        sol = Solution()
        result = sol.maximumProduct(nums)

        print("Maximum Product of Three Numbers:", result)