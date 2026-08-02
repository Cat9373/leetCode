import collections

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)

        if not self._isPalindromePossible(count):
            return ""

        halfCount, midLetter = self._getHalfCountAndMidLetter(count)

        totalPerm = self._countArrangements(halfCount)
        if k > totalPerm:
            return ""

        left = self._generateLeftHalf(halfCount, k)

        return "".join(left) + midLetter + "".join(reversed(left))

    def _isPalindromePossible(self, count):
        odd = 0
        for v in count.values():
            if v % 2:
                odd += 1
        return odd <= 1

    def _getHalfCountAndMidLetter(self, count):
        half = [0] * 26
        mid = ""

        for c, f in count.items():
            half[ord(c) - ord("a")] = f // 2
            if f % 2:
                mid = c

        return half, mid

    def _generateLeftHalf(self, halfCount, k):
        left = []
        length = sum(halfCount)

        for _ in range(length):
            for i in range(26):
                if halfCount[i] == 0:
                    continue

                halfCount[i] -= 1

                ways = self._countArrangements(halfCount)

                if ways >= k:
                    left.append(chr(i + ord("a")))
                    break

                k -= ways
                halfCount[i] += 1

        return left

    def _countArrangements(self, cnt):
        total = sum(cnt)
        ans = 1

        for x in cnt:
            ans *= self._nCk(total, x)
            if ans >= self.MAX:
                return self.MAX
            total -= x

        return ans

    def _nCk(self, n, k):
        if k < 0 or k > n:
            return 0

        k = min(k, n - k)
        res = 1

        for i in range(1, k + 1):
            res = res * (n - i + 1) // i
            if res >= self.MAX:
                return self.MAX

        return res


# Driver Code
if __name__ == "__main__":
    s = input("Enter the palindromic string: ")
    k = int(input("Enter the value of k: "))

    sol = Solution()
    result = sol.smallestPalindrome(s, k)

    if result:
        print("K-th Lexicographically Smallest Palindrome:", result)
    else:
        print("No such palindrome exists.")