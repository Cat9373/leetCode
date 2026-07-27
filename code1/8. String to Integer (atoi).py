class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # Step 1: Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # If string is empty after removing spaces
        if i == n:
            return 0

        # Step 2: Check sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Step 3: Read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # Overflow check
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num


# Driver Code
if __name__ == "__main__":
    s = input("Enter a string: ")

    sol = Solution()
    result = sol.myAtoi(s)

    print("Converted Integer:", result)