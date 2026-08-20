class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7

        for l, r, k, v in queries:
            idx = l

            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        ans = 0

        for num in nums:
            ans ^= num

        return ans


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter nums: ").split()))

    q = int(input("Enter number of queries: "))

    queries = []

    print("Enter each query as: l r k v")

    for _ in range(q):
        query = list(map(int, input().split()))
        queries.append(query)

    sol = Solution()
    result = sol.xorAfterQueries(nums, queries)

    print("XOR after all queries:", result)