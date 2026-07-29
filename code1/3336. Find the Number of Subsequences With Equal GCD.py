from math import gcd
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def subsequencePairCount(self, nums):
        @lru_cache(None)
        def dp(i, g1, g2):
            if i == len(nums):
                return 1 if g1 == g2 and g1 != 0 else 0

            # Skip current element
            ans = dp(i + 1, g1, g2)

            # Put in first subsequence
            ng1 = nums[i] if g1 == 0 else gcd(g1, nums[i])
            ans += dp(i + 1, ng1, g2)

            # Put in second subsequence
            ng2 = nums[i] if g2 == 0 else gcd(g2, nums[i])
            ans += dp(i + 1, g1, ng2)

            return ans % MOD

        return dp(0, 0, 0)


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    print("Enter the elements separated by spaces:")
    nums = list(map(int, input().split()))

    if len(nums) != n:
        print(f"Error: Expected {n} elements, but got {len(nums)}.")
    else:
        sol = Solution()
        result = sol.subsequencePairCount(nums)

        print("Number of Valid Subsequence Pairs:", result)