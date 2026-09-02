def uniformArray(nums1):
    odd = 0

    for x in nums1:
        if x % 2 == 1:
            odd += 1

    even = len(nums1) - odd

    if odd == 0 or even == 0:
        return True

    return odd >= 2 or even >= 2


# Test cases
print(uniformArray([2, 3]))  # True
print(uniformArray([4, 6]))  # True
print(uniformArray([2, 4, 6, 7]))  # True
print(uniformArray([2, 3]))  # True