# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n)
# to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

# Strategy
# Since we're told that the first array has space for the second array. We can work backworks grabbing the larger of the two
# and build the list

def merge(nums1, m, nums2, n):
    # need to grab the last index of each array
    n, m, last = n - 1, m - 1, n + m - 1

    while m >= 0 or n >= 0:
        if nums1[m] > nums2[n]:
            nums1[last] = nums1[m]
            m -= 1
            last -= 1
        else:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1

    # For arrays where the second array's max is less than the first array's min.
    # [4, 5, 6], [1, 2, 3]
    while n >= 0:
        nums1[pos] = nums2[n]
        n -= 1
        pos -= 1

    # Challenge did not have you return anything.
    # return nums1
