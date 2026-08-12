class Solution:
    def findRotation(self, mat, target):
        n = len(mat)

        for _ in range(4):
            if mat == target:
                return True

            # Rotate mat 90 degrees clockwise
            mat = [
                [mat[n - 1 - j][i] for j in range(n)]
                for i in range(n)
            ]

        return False


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter matrix size: "))

    mat = []
    print("Enter the matrix:")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        mat.append(row)

    target = []
    print("Enter the target matrix:")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        target.append(row)

    sol = Solution()
    result = sol.findRotation(mat, target)

    print("Can matrix be rotated to target?", result)