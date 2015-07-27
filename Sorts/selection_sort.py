import unittest

# O(n^2) time
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


class TestSelectionSort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(selection_sort([]), [])

    def test_integers(self):
        self.assertEqual(selection_sort([4, 7, 1, 8, 4, 2, 7, 2, 1, 0]), sorted([4, 7, 1, 8, 4, 2, 7, 2, 1, 0]))

    def test_strings(self):
        self.assertEqual(selection_sort(['zebra', 'penguin', 'aardvark', 'basilisk']), sorted(['zebra', 'penguin', 'aardvark', 'basilisk']))

if __name__ == '__main__':
    unittest.main()
