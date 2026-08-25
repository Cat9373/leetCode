def maxDistance(nums1, nums2):
    i = 0
    j = 0
    ans = 0

    while i < len(nums1) and j < len(nums2):

        if nums1[i] <= nums2[j]:
            ans = max(ans, j - i)
            j += 1
        else:
            i += 1

    return ans


print(maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))
# 2

print(maxDistance([2, 2, 2], [10, 10, 1]))
# 1

print(maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]))
# 2