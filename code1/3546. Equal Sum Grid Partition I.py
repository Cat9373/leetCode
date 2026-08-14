class Solution:
    def canPartitionGrid(self, grid):
        m = len(grid)
        n = len(grid[0])

        total = sum(map(sum, grid))

        # Horizontal cut
        current = 0

        for i in range(m - 1):
            current += sum(grid[i])

            if current * 2 == total:
                return True

        # Vertical cut
        current = 0

        for j in range(n - 1):
            for i in range(m):
                current += grid[i][j]

            if current * 2 == total:
                return True

        return False


# Driver Code
if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    grid = []

    print("Enter the grid:")
    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        grid.append(row)

    sol = Solution()
    result = sol.canPartitionGrid(grid)

    print("Can partition equally:", result)