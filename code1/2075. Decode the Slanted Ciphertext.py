class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        n = len(encodedText)

        if n == 0:
            return ""

        cols = n // rows

        ans = []

        # Start from every column of the first row
        for col in range(cols):
            r = 0
            c = col

            while r < rows and c < cols:
                index = r * cols + c
                ans.append(encodedText[index])

                r += 1
                c += 1

        # Original text has no trailing spaces
        return ''.join(ans).rstrip()


# Driver Code
if __name__ == "__main__":
    encodedText = input("Enter encoded text: ")
    rows = int(input("Enter number of rows: "))

    sol = Solution()
    result = sol.decodeCiphertext(encodedText, rows)

    print("Original text:", result)