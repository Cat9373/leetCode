class Solution:
    def minimumDistance(self, nums):
        # Store the last two positions of each number
        positions = {}

        ans = float('inf')

        for i, num in enumerate(nums):

            if num not in positions:
                positions[num] = []

            positions[num].append(i)

            # We only need the latest 3 occurrences
            if len(positions[num]) >= 3:
                a, b, c = positions[num][-3:]

                distance = (
                    abs(a - b)
                    + abs(b - c)
                    + abs(c - a)
                )

                ans = min(ans, distance)

                # Keep only the last two positions
                positions[num] = positions[num][-2:]

        return -1 if ans == float('inf') else ans


# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))

    sol = Solution()
    result = sol.minimumDistance(nums)

    print("Minimum distance:", result)