class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345

        n = len(grid)
        m = len(grid[0])

        # Answer matrix
        ans = [[0] * m for _ in range(n)]

        # Prefix product
        prefix = 1

        for i in range(n):
            for j in range(m):
                ans[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD

        # Suffix product
        suffix = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                ans[i][j] = (ans[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD

        return ans


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    m = int(input("Enter number of columns: "))

    grid = []

    print("Enter the grid:")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        grid.append(row)

    sol = Solution()
    result = sol.constructProductMatrix(grid)

    print("\nProduct Matrix:")
    for row in result:
        print(*row)