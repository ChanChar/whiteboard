import mmh3
import unittest

# Notes
# Usually constructed to have in front of a db to filter out a higher chance of negative searches
# Usually saved in memory, and a backup is saved in DB.

class BloomFilter:
    def __init__(self, size=100):
        self.filter = [0] * size
        self.size = size

    def add(self, val):
        pos1, pos2 = self.get_hashed(val)
        self.filter[pos1], self.filter[pos2] = 1, 1

    def has_key(self, val):
        pos1, pos2 = self.get_hashed(val)
        return self.filter[pos1] and self.filter[pos2]

    def get_hashed(self, val):
        hash1, hash2 = mmh3.hash(val) % self.size, hash(val) % self.size
        return (hash1, hash2)

class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bloom_filter = BloomFilter()
        self.bloom_filter.add('hello')
        self.bloom_filter.add('and')
        self.bloom_filter.add('goodbye')

    def test_existing_key(self):
        self.assertTrue(self.bloom_filter.has_key('hello'))
        self.assertTrue(self.bloom_filter.has_key('and'))
        self.assertTrue(self.bloom_filter.has_key('goodbye'))

    def test_nonexistant_key(self):
        self.assertFalse(self.bloom_filter.has_key('goodbyes'))
        self.assertFalse(self.bloom_filter.has_key('python'))

if __name__ == '__main__':
    unittest.main()
