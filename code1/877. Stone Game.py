class Solution:
    def stoneGame(self, piles):
        return True


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of piles (even): "))

    print("Enter the stones in each pile:")
    piles = list(map(int, input().split()))

    if len(piles) != n:
        print(f"Error: Expected {n} piles, but got {len(piles)}.")
    else:
        sol = Solution()
        result = sol.stoneGame(piles)

        print("Does Alice win?", result)