def missingMultiple(nums, k):
    num_set = set(nums)

    multiple = k

    while multiple in num_set:
        multiple += k

    return multiple


# Test
nums = [8, 2, 3, 4, 6]
k = 2

print(missingMultiple(nums, k))