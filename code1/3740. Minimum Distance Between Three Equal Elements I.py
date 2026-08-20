class Solution:
    def minimumDistance(self, nums):
        positions = {}

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []

            positions[num].append(i)

        ans = float('inf')

        for indices in positions.values():

            if len(indices) < 3:
                continue

            for i in range(len(indices) - 2):
                a = indices[i]
                c = indices[i + 2]

                distance = 2 * (c - a)

                ans = min(ans, distance)

        return -1 if ans == float('inf') else ans


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))

    sol = Solution()
    result = sol.minimumDistance(nums)

    print("Minimum distance:", result)