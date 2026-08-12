class Solution:
    def minAbsDiff(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        ans = []

        for i in range(m - k + 1):
            row = []

            for j in range(n - k + 1):
                values = set()

                # Collect distinct values in the k x k submatrix
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.add(grid[x][y])

                # If all values are the same
                if len(values) <= 1:
                    row.append(0)
                    continue

                # Sort distinct values
                values = sorted(values)

                # Minimum difference will be between
                # two adjacent values after sorting
                minimum = float('inf')

                for p in range(1, len(values)):
                    minimum = min(
                        minimum,
                        values[p] - values[p - 1]
                    )

                row.append(minimum)

            ans.append(row)

        return ans


# Driver Code
if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    grid = []

    print("Enter the grid:")
    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        grid.append(row)

    k = int(input("Enter k: "))

    sol = Solution()
    result = sol.minAbsDiff(grid, k)

    print("Result:")
    for row in result:
        print(row)