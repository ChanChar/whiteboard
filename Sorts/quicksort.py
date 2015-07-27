from random import randrange
import unittest

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


class TestQuicksort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(quicksort([]), [])

    def test_integers(self):
        self.assertEqual(quicksort([5, 9, 8, 4, 10, 6, 7, 2, 3, 1]), sorted([5, 9, 8, 4, 10, 6, 7, 2, 3, 1]))

    def test_strings(self):
        self.assertEqual(quicksort(['zebra', 'penguin', 'aardvark', 'basilisk']), sorted(['zebra', 'penguin', 'aardvark', 'basilisk']))

if __name__ == '__main__':
    unittest.main()
