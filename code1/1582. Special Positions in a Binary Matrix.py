class Solution:
    def numSpecial(self, mat):
        m = len(mat)
        n = len(mat[0])

        rowCount = [0] * m
        colCount = [0] * n

        # Count 1's in each row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1

        # Count special positions
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    ans += 1

        return ans


# Driver Code
if __name__ == "__main__":
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))

    print("Enter the binary matrix row by row:")

    mat = []
    for i in range(m):
        row = list(map(int, input().split()))

        if len(row) != n:
            print(f"Error: Expected {n} elements in row {i + 1}, but got {len(row)}.")
            exit()

        mat.append(row)

    sol = Solution()
    result = sol.numSpecial(mat)

    print("Number of Special Positions:", result)