from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        total = m * n
        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                old_index = i * n + j
                new_index = (old_index + k) % total

                new_row = new_index // n
                new_col = new_index % n

                ans[new_row][new_col] = grid[i][j]

        return ans


# Driver Code
if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter the grid row by row:")
    grid = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        grid.append(row)

    k = int(input("Enter value of k: "))

    sol = Solution()
    result = sol.shiftGrid(grid, k)

    print("\nShifted Grid:")
    for row in result:
        print(*row)