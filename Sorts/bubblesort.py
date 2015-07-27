import unittest

# O(n^2) time
def bubblesort(array):
    if len(array) <= 1:
        return array
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

class TestBubblesort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(bubblesort([]), [])

    def test_integers(self):
        self.assertEqual(bubblesort([4, 7, 1, 8, 4, 2, 7, 2, 1, 0]), sorted([4, 7, 1, 8, 4, 2, 7, 2, 1, 0]))

    def test_strings(self):
        self.assertEqual(bubblesort(['zebra', 'penguin', 'aardvark', 'basilisk']), sorted(['zebra', 'penguin', 'aardvark', 'basilisk']))

if __name__ == '__main__':
    unittest.main()
