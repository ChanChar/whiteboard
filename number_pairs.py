def num_pairs(arr, target):
    seen = set()
    pairs = []
    for num in arr:
        if target - num in seen:
            pairs.append("{},{}".format(target - num, num))

        seen.add(num)

    # return ";".join(pairs.reverse())
    if len(pairs):
        return ";".join(pairs[::-1])
    else:
        return 'NULL'

# print(num_pairs([2,4,5,6,9,11,15], 20))

test = '2,4,5,6,9,11,15;20'

nums, target = test.strip().split(';')
nums = [int(num) for num in nums.split(',')]

print(num_pairs(nums, int(target)))
