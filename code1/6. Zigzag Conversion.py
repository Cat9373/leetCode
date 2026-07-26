class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        current_row = 0
        direction = 1

        for ch in s:
            rows[current_row] += ch

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)


# Driver Code
if __name__ == "__main__":
    s = input("Enter the string: ")
    numRows = int(input("Enter the number of rows: "))

    sol = Solution()
    result = sol.convert(s, numRows)

    print("Converted Zigzag String:", result)