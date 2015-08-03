# Given an array of integers and an integer k, find out whether there there are
# two distinct indices i and j in the array such that nums[i] = nums[j] and the
# difference between i and j is at most k.
def containsNearbyDuplicate(nums, k):
    if len(nums) < 2:
        return False

    values = {}

    for i, num in enumerate(nums):
        if num in values:
            if i - values[num] <= k:
                return True
            else:
                values[num] = i
        else:
            values[num] = i
    return False
