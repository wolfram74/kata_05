import unittest
import bloom_filter

class BloomTest(unittest.TestCase):
    def setUp(self):
        self.filter = bloom_filter.BloomFilter()

    def test_existence(self):
        self.assertEqual(type(self.filter), bloom_filter.BloomFilter)

    def test_not_included(self):
        self.assertFalse(self.filter.inlucdes('nothing'))

    def test_addition(self):
        self.assertTrue(self.filter.add('something'))
        self.assertTrue(self.filter.includes('something'))
        self.assertFalse(self.filter.includes('nothing'))#may sometimes fail

    @unittest.skip('optional feature')
    def test_size_of_set(self):
        self.assertEqual(0, self.filter.elements())
        self.fillter.add('something')
        self.assertEqual(1, self.filter.elements())

    @unittest.skip('optional feature')
    def test_expected_size(self):
        small_filter = bloom_filter.BloomFilter(size=10)
        self.assertNotEqual(small_filter.size(), self.filter.size())

    @unittest.skip('optional feature')
    def test_custom_hash_iterations(self):
        hashy_filter = bloom_filter.BloomFilter(hashes=1000)
        self.assertNotEqual(small_filter.hashings(), self.filter.hashings())

    @unittest.skip('optional feature')
    def test_false_positive_rate(self):
        pass

