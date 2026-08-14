class Solution:
    def areSimilar(self, mat, k):
        m = len(mat)
        n = len(mat[0])

        shift = k % n

        for i in range(m):
            if i % 2 == 0:
                # Even row → left shift
                shifted = mat[i][shift:] + mat[i][:shift]
            else:
                # Odd row → right shift
                shifted = mat[i][-shift:] + mat[i][:-shift]

            if shifted != mat[i]:
                return False

        return True


# Driver Code
if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    mat = []

    print("Enter the matrix:")
    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        mat.append(row)

    k = int(input("Enter k: "))

    sol = Solution()
    result = sol.areSimilar(mat, k)

    print("Are the matrices similar?", result)