def minimumDeletions(nums):
    n = len(nums)

    minIndex = nums.index(min(nums))
    maxIndex = nums.index(max(nums))

    if minIndex > maxIndex:
        minIndex, maxIndex = maxIndex, minIndex

    front = maxIndex + 1
    back = n - minIndex
    both = (minIndex + 1) + (n - maxIndex)

    return min(front, back, both)


print(minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]))
# 5

print(minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5]))
# 3

print(minimumDeletions([101]))
# 1