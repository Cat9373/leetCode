class Solution:
    def findDifferentBinaryString(self, nums):
        ans = []

        for i in range(len(nums)):
            if nums[i][i] == '0':
                ans.append('1')
            else:
                ans.append('0')

        return "".join(ans)


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of binary strings: "))

    print("Enter the binary strings:")
    nums = []
    for _ in range(n):
        nums.append(input().strip())

    sol = Solution()
    result = sol.findDifferentBinaryString(nums)

    print("Different Binary String:", result)