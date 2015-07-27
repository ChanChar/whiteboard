import unittest

def mergesort(array):
    if len(array) <= 1:
        return array
    midpoint = len(array) // 2
    return _merge(mergesort(array[0:midpoint]), mergesort(array[midpoint:]))

def _merge(part1, part2):
    merged = []
    while len(part1) > 0 and len(part2) > 0:
        if part1[0] > part2[0]:
            merged.append(part2.pop(0))
        else:
            merged.append(part1.pop(0))
    return merged + part1 + part2

# Performance of the merge method could be improved if a deque is used.

class TestMergesort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(mergesort([]), [])

    def test_integers(self):
        self.assertEqual(mergesort([5, 9, 8, 4, 10, 6, 7, 2, 3, 1]), sorted([5, 9, 8, 4, 10, 6, 7, 2, 3, 1]))

    def test_strings(self):
        self.assertEqual(mergesort(['zebra', 'penguin', 'aardvark', 'basilisk']), sorted(['zebra', 'penguin', 'aardvark', 'basilisk']))

if __name__ == '__main__':
    unittest.main()
