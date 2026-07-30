class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (x.bit_count(), x))


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    print("Enter the elements separated by spaces:")
    arr = list(map(int, input().split()))

    if len(arr) != n:
        print(f"Error: Expected {n} elements, but got {len(arr)}.")
    else:
        sol = Solution()
        result = sol.sortByBits(arr)

        print("Array Sorted by Number of 1 Bits:")
        print(result)