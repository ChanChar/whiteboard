from random import randrange

def quicksort(array, start=0, length=None):
    if length is None:
        length = len(array)

    if length < 2:
        return array

    pivot_idx = partition(array, start, length)
    left_length = pivot_idx - start
    right_length = length - (left_length + 1)

    quicksort(array, start, left_length)
    quicksort(array, pivot_idx + 1, right_length)

    return array

def partition(array, start, length):
    pivot_idx, pivot = start, array[start]
    for i in range(start + 1, start + length):
        val = array[i]
        if val < pivot:
            array[i] = array[pivot_idx + 1]
            array[pivot_idx + 1] = pivot
            array[pivot_idx] = val
            pivot_idx += 1

    return pivot_idx

print(quicksort([1,4,7,3,7,2,1,6,8,4]))
