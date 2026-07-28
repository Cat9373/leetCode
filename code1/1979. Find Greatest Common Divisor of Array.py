import math

class Solution:
    def findGCD(self, nums):
        return math.gcd(min(nums), max(nums))


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    print("Enter the elements separated by spaces:")
    nums = list(map(int, input().split()))

    if len(nums) != n:
        print(f"Error: Expected {n} elements, but got {len(nums)}.")
    else:
        sol = Solution()
        result = sol.findGCD(nums)
        print("GCD of the smallest and largest element:", result)