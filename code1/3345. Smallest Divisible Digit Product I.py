class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def digitProduct(num):
            product = 1

            while num > 0:
                product *= num % 10
                num //= 10

            return product

        while True:
            if digitProduct(n) % t == 0:
                return n

            n += 1


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter n: "))
    t = int(input("Enter t: "))

    sol = Solution()
    result = sol.smallestNumber(n, t)

    print("Smallest number:", result)