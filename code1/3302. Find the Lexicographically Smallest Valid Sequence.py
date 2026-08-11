class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # last[j] = latest index in word1 where word2[j]
        # can be matched while still matching word2[j+1:]
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        canSkip = True

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch
            elif canSkip:
                # We can use i as the mismatching character if
                # the rest of word2 can still be matched.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    canSkip = False

        return ans if j == m else []


# Driver Code
if __name__ == "__main__":
    word1 = input("Enter word1: ")
    word2 = input("Enter word2: ")

    sol = Solution()
    result = sol.validSequence(word1, word2)

    print("Valid sequence:", result)