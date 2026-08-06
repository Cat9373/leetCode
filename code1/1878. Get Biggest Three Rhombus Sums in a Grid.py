class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):
                # Rhombus of size 0
                sums.add(grid[i][j])

                maxSize = min(i, m - 1 - i, j, n - 1 - j)

                for k in range(1, maxSize + 1):
                    total = 0

                    # top -> right
                    x, y = i - k, j
                    for t in range(k):
                        total += grid[x + t][y + t]

                    # right -> bottom
                    x, y = i, j + k
                    for t in range(k):
                        total += grid[x + t][y - t]

                    # bottom -> left
                    x, y = i + k, j
                    for t in range(k):
                        total += grid[x - t][y - t]

                    # left -> top
                    x, y = i, j - k
                    for t in range(k):
                        total += grid[x - t][y + t]

                    sums.add(total)

        return sorted(sums, reverse=True)[:3]


# Driver Code
if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter the grid row by row:")
    grid = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        grid.append(row)

    sol = Solution()
    result = sol.getBiggestThree(grid)

    print("\nThe biggest three distinct rhombus sums are:")
    print(result)