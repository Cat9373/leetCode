class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = s.find('0')

        if i == -1:
            return True

        return '1' not in s[i:]


# Driver Code
if __name__ == "__main__":
    s = input("Enter the binary string: ")

    sol = Solution()
    result = sol.checkOnesSegment(s)

    print("Contains at most one contiguous segment of ones:", result)