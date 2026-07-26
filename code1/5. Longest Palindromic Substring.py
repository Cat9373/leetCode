class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        ans = ""

        for i in range(len(s)):
            # Odd length palindrome
            odd = expand(i, i)

            # Even length palindrome
            even = expand(i, i + 1)

            if len(odd) > len(ans):
                ans = odd

            if len(even) > len(ans):
                ans = even

        return ans


# Driver Code
if __name__ == "__main__":
    s = input("Enter the string: ")

    sol = Solution()
    result = sol.longestPalindrome(s)

    print("Longest Palindromic Substring:", result)