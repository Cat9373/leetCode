class Solution:
    def uniqueXorTriplets(self, nums):
        mx = max(nums) << 1

        # all possible XORs of two elements
        pair = [False] * mx
        for a in nums:
            for b in nums:
                pair[a ^ b] = True

        # XOR each pair-XOR with a third element
        ans = [False] * mx
        for x in range(mx):
            if pair[x]:
                for c in nums:
                    ans[x ^ c] = True

        return sum(ans)


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    print("Enter the elements separated by spaces:")
    nums = list(map(int, input().split()))

    if len(nums) != n:
        print(f"Error: Expected {n} elements, but got {len(nums)}.")
    else:
        sol = Solution()
        result = sol.uniqueXorTriplets(nums)

        print("Number of Unique XOR Triplets:", result)