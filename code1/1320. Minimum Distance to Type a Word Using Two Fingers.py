class Solution:
    def minimumDistance(self, word: str) -> int:

        def pos(ch):
            num = ord(ch) - ord('A')
            return (num // 6, num % 6)

        def distance(a, b):
            if a == 26 or b == 26:
                return 0

            x1, y1 = pos(chr(a + ord('A')))
            x2, y2 = pos(chr(b + ord('A')))

            return abs(x1 - x2) + abs(y1 - y2)

        # 26 represents a finger that has not been used yet.
        dp = [float('inf')] * 27
        dp[26] = 0

        prev = ord(word[0]) - ord('A')

        for i in range(1, len(word)):
            cur = ord(word[i]) - ord('A')

            new_dp = [float('inf')] * 27

            for other in range(27):

                if dp[other] == float('inf'):
                    continue

                # Option 1: move the finger on prev to cur
                cost = dp[other] + distance(prev, cur)

                new_dp[other] = min(
                    new_dp[other],
                    cost
                )

                # Option 2: use the other finger
                cost = dp[other] + distance(other, cur)

                new_dp[prev] = min(
                    new_dp[prev],
                    cost
                )

            dp = new_dp
            prev = cur

        return min(dp)


# Driver Code
if __name__ == "__main__":
    word = input("Enter the word: ").strip().upper()

    sol = Solution()
    result = sol.minimumDistance(word)

    print("Minimum distance:", result)