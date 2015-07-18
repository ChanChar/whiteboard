# Kadane's Algorithm: Solve for max subsum for an array.

def max_subarray(arr):
    current_max, highest_max = arr[0], arr[0]
    for x in arr[1:]:
        current_max = max(x, current_max + x)
        highest_max = max(highest_max, current_max)
    return highest_max

# print(max_subarray([2, 3, -2, -1, 10]))
print(max_subarray([-10, 2, 3, -2, 0, 5, -15]))
