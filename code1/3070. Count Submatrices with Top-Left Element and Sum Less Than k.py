class Solution:
    def countSubmatrices(self, grid, k):
        m, n = len(grid), len(grid[0])

        prefix = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                prefix[i][j] = grid[i][j]

                if i > 0:
                    prefix[i][j] += prefix[i - 1][j]

                if j > 0:
                    prefix[i][j] += prefix[i][j - 1]

                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i - 1][j - 1]

                if prefix[i][j] <= k:
                    ans += 1

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
    result = sol.countSubmatrices(grid, k)

    print("Number of submatrices:", result)