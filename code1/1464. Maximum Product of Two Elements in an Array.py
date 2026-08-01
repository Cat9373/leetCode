class Solution:
    def maxProduct(self, nums):
        first = second = 0

        for num in nums:
            if num >= first:
                second = first
                first = num
            elif num > second:
                second = num

        return (first - 1) * (second - 1)


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    print("Enter the elements separated by spaces:")
    nums = list(map(int, input().split()))

    if len(nums) != n:
        print(f"Error: Expected {n} elements, but got {len(nums)}.")
    else:
        sol = Solution()
        result = sol.maxProduct(nums)

        print("Maximum Product:", result)