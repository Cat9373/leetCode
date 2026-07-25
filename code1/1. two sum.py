class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i


obj = Solution()

print(obj.twoSum([2,7,11,15], 9))