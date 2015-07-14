def max_range_sum(limit, arr):
    i = 0
    max_profit = 0
    while i + limit <= len(arr):
        current = sum(arr[i:i+limit])
        if current > max_profit:
            max_profit = current
        i += 1
    return max_profit


print(max_range_sum(5, [7, -3, -10, 4, 2, 8, -2, 4, -5, -2]))
print(max_range_sum(6, [-4, 3, -10, 5, 3, -7, -3, 7, -6, 3]))
