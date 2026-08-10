class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])

        preX = [[0] * (n + 1) for _ in range(m + 1)]
        preY = [[0] * (n + 1) for _ in range(m + 1)]

        ans = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                preX[i][j] = (
                    preX[i - 1][j]
                    + preX[i][j - 1]
                    - preX[i - 1][j - 1]
                )

                preY[i][j] = (
                    preY[i - 1][j]
                    + preY[i][j - 1]
                    - preY[i - 1][j - 1]
                )

                if grid[i - 1][j - 1] == 'X':
                    preX[i][j] += 1
                elif grid[i - 1][j - 1] == 'Y':
                    preY[i][j] += 1

                if preX[i][j] > 0 and preX[i][j] == preY[i][j]:
                    ans += 1

        return ans


# Driver Code
if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    grid = []

    print("Enter the grid using X, Y, and .")
    for i in range(m):
        row = input(f"Row {i + 1}: ").split()
        grid.append(row)

    sol = Solution()
    result = sol.numberOfSubmatrices(grid)

    print("Number of valid submatrices:", result)