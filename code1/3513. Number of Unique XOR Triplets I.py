class Solution:
    def uniqueXorTriplets(self, nums):
        n = len(nums)

        if n < 3:
            return n

        return 1 << n.bit_length()


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