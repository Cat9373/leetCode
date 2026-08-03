class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0

        for i in range(len(word)):
            ans += i // 8 + 1

        return ans


# Driver Code
if __name__ == "__main__":
    word = input("Enter the word: ")

    sol = Solution()
    result = sol.minimumPushes(word)

    print("Minimum Pushes Required:", result)