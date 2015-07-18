def subsets(arr):
    if len(arr) == 0:
        return [[]]
    val = arr[0]
    subs = subsets(arr[1:])
    new_subs = [sub + [val] for sub in subs]
    return subs + new_subs

print(subsets([1, 2, 3, 4, 5]))
