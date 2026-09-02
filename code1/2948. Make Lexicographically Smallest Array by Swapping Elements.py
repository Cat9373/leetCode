def lexicographicallySmallestArray(nums, limit):

    n = len(nums)

    # Store (value, original index)
    arr = sorted((value, i) for i, value in enumerate(nums))

    ans = [0] * n

    start = 0

    while start < n:

        end = start

        # Find the complete connected group
        while end + 1 < n:
            if arr[end + 1][0] - arr[end][0] <= limit:
                end += 1
            else:
                break

        # Get values
        values = [
            arr[i][0]
            for i in range(start, end + 1)
        ]

        # Get and sort original indices
        indices = sorted(
            arr[i][1]
            for i in range(start, end + 1)
        )

        # Put smallest values at smallest indices
        for value, index in zip(values, indices):
            ans[index] = value

        start = end + 1

    return ans


# Test cases

print(lexicographicallySmallestArray(
    [1, 5, 3, 9, 8], 2
))
# [1, 3, 5, 8, 9]

print(lexicographicallySmallestArray(
    [1, 7, 6, 18, 2, 1], 3
))
# [1, 6, 7, 18, 1, 2]

print(lexicographicallySmallestArray(
    [1, 7, 28, 19, 10], 3
))
# [1, 7, 28, 19, 10]