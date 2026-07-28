from math import gcd

class Solution:
    def gcdSum(self, nums):
        prefixGcd = []

        mx = 0
        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(gcd(x, mx))

        prefixGcd.sort()

        ans = 0
        i, j = 0, len(prefixGcd) - 1

        while i < j:
            ans += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    print("Enter the elements separated by spaces:")
    nums = list(map(int, input().split()))

    if len(nums) != n:
        print(f"Error: Expected {n} elements, but got {len(nums)}.")
    else:
        sol = Solution()
        result = sol.gcdSum(nums)

        print("GCD Sum:", result)