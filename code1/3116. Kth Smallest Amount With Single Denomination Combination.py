from math import gcd


class Solution:
    def findKthSmallest(self, coins, k):

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                value = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        value = lcm(value, coins[i])

                        if value > x:
                            valid = False
                            break

                if not valid:
                    continue

                if bits % 2 == 1:
                    total += x // value
                else:
                    total -= x // value

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left


# Driver Code
if __name__ == "__main__":
    coins = list(map(int, input("Enter coins: ").split()))
    k = int(input("Enter k: "))

    sol = Solution()
    result = sol.findKthSmallest(coins, k)

    print("Kth smallest amount:", result)