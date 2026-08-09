class Solution:
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])

        # Compute heights
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

        ans = 0

        for i in range(m):
            heights = sorted(matrix[i], reverse=True)

            for j in range(n):
                ans = max(ans, heights[j] * (j + 1))

        return ans


# Driver Code
if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    matrix = []

    print("Enter the matrix row by row:")
    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    sol = Solution()
    result = sol.largestSubmatrix(matrix)

    print("Largest submatrix area:", result)