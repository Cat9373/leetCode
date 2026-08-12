class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        top = x
        bottom = x + k - 1

        while top < bottom:
            for col in range(y, y + k):
                grid[top][col], grid[bottom][col] = \
                    grid[bottom][col], grid[top][col]

            top += 1
            bottom -= 1

        return grid


# Driver Code
if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    grid = []

    print("Enter the grid:")
    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        grid.append(row)

    x = int(input("Enter x (starting row): "))
    y = int(input("Enter y (starting column): "))
    k = int(input("Enter k (size of submatrix): "))

    sol = Solution()
    result = sol.reverseSubmatrix(grid, x, y, k)

    print("\nUpdated Matrix:")
    for row in result:
        print(*row)