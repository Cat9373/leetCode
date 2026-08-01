class Solution:
    def minSwaps(self, grid):
        n = len(grid)

        # Last position of 1 in each row
        last = []
        for row in grid:
            pos = -1
            for j in range(n):
                if row[j] == 1:
                    pos = j
            last.append(pos)

        ans = 0

        for i in range(n):
            j = i

            # Find a row that can be placed at position i
            while j < n and last[j] > i:
                j += 1

            if j == n:
                return -1

            # Bring it up using adjacent swaps
            while j > i:
                last[j], last[j - 1] = last[j - 1], last[j]
                ans += 1
                j -= 1

        return ans


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the size of the grid (n): "))

    print("Enter the binary grid row by row:")
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    sol = Solution()
    result = sol.minSwaps(grid)

    print("Minimum Adjacent Swaps Required:", result)