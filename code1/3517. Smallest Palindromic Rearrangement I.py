from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        left = []
        middle = ""

        for ch in sorted(freq.keys()):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2 == 1:
                middle = ch

        left = "".join(left)
        return left + middle + left[::-1]


# Driver Code
if __name__ == "__main__":
    s = input("Enter a palindromic string: ")

    sol = Solution()
    result = sol.smallestPalindrome(s)

    print("Lexicographically Smallest Palindromic Rearrangement:", result)