class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s

        alt1 = []
        alt2 = []

        for i in range(2 * n):
            if i % 2 == 0:
                alt1.append('0')
                alt2.append('1')
            else:
                alt1.append('1')
                alt2.append('0')

        diff1 = diff2 = 0
        left = 0
        ans = float('inf')

        for right in range(2 * n):
            if s[right] != alt1[right]:
                diff1 += 1
            if s[right] != alt2[right]:
                diff2 += 1

            if right - left + 1 > n:
                if s[left] != alt1[left]:
                    diff1 -= 1
                if s[left] != alt2[left]:
                    diff2 -= 1
                left += 1

            if right - left + 1 == n:
                ans = min(ans, diff1, diff2)

        return ans


# Driver Code
if __name__ == "__main__":
    s = input("Enter the binary string: ")

    sol = Solution()
    result = sol.minFlips(s)

    print("Minimum Flips Required:", result)