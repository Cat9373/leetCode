class Solution:
    def stoneGameIX(self, stones):
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        zero = count[0]
        one = count[1]
        two = count[2]

        # Alice must start with a 1 or 2.
        if one == 0 and two == 0:
            return False

        # If there are no 0-remainder stones,
        # Alice wins when the counts of 1s and 2s are not equal.
        if zero % 2 == 0:
            return one > 0 and two > 0

        # Odd number of 0s
        return abs(one - two) > 2


# Driver Code
if __name__ == "__main__":
    stones = list(map(int, input("Enter the stones: ").split()))

    sol = Solution()
    result = sol.stoneGameIX(stones)

    print("Can Alice win?", result)