class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)

        positions = {}

        # Store all positions of each number
        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []

            positions[num].append(i)

        # nearest[i] = minimum circular distance
        # from i to another equal element
        nearest = [-1] * n

        for arr in positions.values():

            # No other equal element
            if len(arr) == 1:
                continue

            m = len(arr)

            for i in range(m):
                curr = arr[i]

                # Previous occurrence
                prev_idx = arr[(i - 1) % m]

                # Next occurrence
                next_idx = arr[(i + 1) % m]

                # Distance to previous
                d1 = abs(curr - prev_idx)
                d1 = min(d1, n - d1)

                # Distance to next
                d2 = abs(curr - next_idx)
                d2 = min(d2, n - d2)

                nearest[curr] = min(d1, d2)

        return [nearest[q] for q in queries]


# Driver Code
if __name__ == "__main__":

    nums = list(
        map(int, input("Enter nums: ").split())
    )

    queries = list(
        map(int, input("Enter queries: ").split())
    )

    sol = Solution()

    result = sol.solveQueries(nums, queries)

    print("Answer:", result)