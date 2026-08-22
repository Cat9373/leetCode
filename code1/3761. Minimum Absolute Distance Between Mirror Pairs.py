def minMirrorPairDistance(nums):
    pos = {}
    ans = float('inf')

    for i, x in enumerate(nums):

        # Check if a previous number has
        # reverse(previous number) == x
        if x in pos:
            ans = min(ans, i - pos[x])

        # Store the reversed value and its index
        pos[reverse(x)] = i

    return -1 if ans == float('inf') else ans


def reverse(x):
    rev = 0

    while x > 0:
        rev = rev * 10 + (x % 10)
        x //= 10

    return rev


# Test
nums = [12, 21, 45, 33, 54]

print(minMirrorPairDistance(nums))