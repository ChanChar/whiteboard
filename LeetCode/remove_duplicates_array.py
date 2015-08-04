# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
def remove_duplicates(nums):
    if len(nums) < 2:
        return len(nums)

    current = nums[0]
    count = 1

    for num in nums:
        if num != current:
            nums[count] = num
            count += 1
            current = num

    return count
