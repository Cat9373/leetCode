class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')

        # Minimum possible operations
        t = (z + k - 1) // k

        while t <= n:
            if (t * k - z) % 2 == 0:
                if t % 2 == 0:
                    if t * (n - k) >= z:
                        return t
                else:
                    if t * (n - k) >= n - z:
                        return t
            t += 1

        return -1


# Driver Code
if __name__ == "__main__":
    s = input("Enter the binary string: ")
    k = int(input("Enter the value of k: "))

    sol = Solution()
    result = sol.minOperations(s, k)

    print("Minimum Operations:", result)