class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        ans = float('inf')

        for i in range(n):
            if words[i] == target:
                distance = abs(i - startIndex)
                distance = min(distance, n - distance)

                ans = min(ans, distance)

        return -1 if ans == float('inf') else ans


# Driver Code
if __name__ == "__main__":
    words = input("Enter words separated by spaces: ").split()
    target = input("Enter target: ")
    startIndex = int(input("Enter start index: "))

    sol = Solution()
    result = sol.closestTarget(words, target, startIndex)

    print("Shortest distance:", result)