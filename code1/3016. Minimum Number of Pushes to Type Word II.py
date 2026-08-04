from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)

        ans = 0

        for i, f in enumerate(freq):
            ans += (i // 8 + 1) * f

        return ans


# Driver Code
if __name__ == "__main__":
    word = input("Enter the word: ")

    sol = Solution()
    result = sol.minimumPushes(word)

    print("Minimum Pushes Required:", result)