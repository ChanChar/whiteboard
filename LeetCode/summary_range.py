def summary_range(nums):
    if len(nums) < 2:
        return [str(num) for num in nums]
    ranges = []
    start, end = None, None
    for num in nums:
        if start is None:
            start, end = num, num
        elif num == end + 1:
            end += 1
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append("{}->{}".format(start, end))
            start, end = num, num

        if num == nums[-1]:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append("{}->{}".format(start, end))

    return ranges

# Awesome and cleaner method.
def summary_range(nums):
    ranges = []
    for n in nums:
        if not ranges or n > ranges[-1][-1] + 1:
            ranges += [[]]
        # After creating an empty placeholder array, set or replace the second element.
        ranges[-1][1:] = [n]

    # Only subarrays with 2 elements will get joined with the delimiter.
    return ['->'.join(map(str, r)) for r in ranges]
