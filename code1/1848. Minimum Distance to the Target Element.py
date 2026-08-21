class Solution:
    def getMinDistance(self, nums, target, start):
        return min(
            abs(i - start)
            for i in range(len(nums))
            if nums[i] == target
        )


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    target = int(input("Enter target: "))
    start = int(input("Enter start index: "))

    sol = Solution()
    result = sol.getMinDistance(nums, target, start)

    print("Minimum distance:", result)