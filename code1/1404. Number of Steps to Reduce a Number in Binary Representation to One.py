class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        # Traverse from right to left (ignore the leftmost bit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry

            if bit == 1:
                # Odd: add 1 then divide by 2
                steps += 2
                carry = 1
            else:
                # Even: divide by 2
                steps += 1

        # If there is a carry left, one extra step is needed
        return steps + carry


# Driver Code
if __name__ == "__main__":
    s = input("Enter a binary string: ")

    sol = Solution()
    result = sol.numSteps(s)

    print("Number of Steps:", result)