import unittest

# O(log(n)) time, O(1) space.
def binary_search(array, target):
    start, stop = 0, len(array)
    while stop != start:
        midpoint = (start + stop) // 2
        current = array[midpoint]
        if current == target:
            return midpoint
        elif current < target:
            start = midpoint + 1
        else:
            stop = midpoint
    return -1

class TestBinarySearch(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(binary_search([], 6), -1)

    def test_normal_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8), 7)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5), 4)

    def test_out_of_bounds(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 9), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8], -5), -1)

if __name__ == '__main__':
    unittest.main()
