import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_default(self):
        cache = LRUCache(2)

        cache["k1"] = "val1"
        cache["k2"] = "val2"

        self.assertEqual(cache["k3"], None)
        self.assertEqual(cache["k2"], "val2")
        self.assertEqual(cache["k1"], "val1")

        cache["k3"] = "val3"

        self.assertEqual(cache["k3"], "val3")
        self.assertEqual(cache["k2"], None)
        self.assertEqual(cache["k1"], "val1")

    def test_small_size(self):
        cache = LRUCache(1)
        cache["one"] = "value_of_one"
        self.assertEqual(cache["one"], "value_of_one")
        cache["one"] = "another_value"
        self.assertEqual(cache["one"], "another_value")
        cache["two"] = "value_of_two"
        self.assertEqual(cache["one"], None)
        self.assertEqual(cache["two"], "value_of_two")

    def test_del_simple(self):
        cache = LRUCache(10)
        for i in range(10):
            cache[i] = i
        for i in range(10):
            self.assertEqual(cache[i], i)
        cache[11] = 11
        self.assertEqual(cache[0], None)
        self.assertEqual(cache[11], 11)

    def test_last(self):
        cache = LRUCache(3)
        for i in range(3):
            cache[i] = 2 - i
        for i in range(100):
            for j in range(3):
                self.assertEqual(cache[j], 2 - j)

    def test_set_many_times(self):
        cache = LRUCache(5)
        for i in range(10000):
            value = (i * 23456 + 154) % 12435 + 124
            cache[i] = value
            self.assertEqual(cache[i], value)

    def test_full_replacement(self):
        cache = LRUCache(5)

        cache['k1'] = 'val1'
        cache['k2'] = 'val2'
        cache['k3'] = 'val3'
        cache['k4'] = 'val4'
        cache['k5'] = 'val5'

        self.assertEqual(cache['k5'], 'val5')
        self.assertEqual(cache['k4'], 'val4')
        self.assertEqual(cache['k3'], 'val3')
        self.assertEqual(cache['k2'], 'val2')
        self.assertEqual(cache['k1'], 'val1')

        cache['k6'] = 'val6'
        self.assertEqual(cache['k5'], None)
        cache['k7'] = 'val7'
        self.assertEqual(cache['k4'], None)
        cache['k8'] = 'val8'
        self.assertEqual(cache['k3'], None)
        cache['k9'] = 'val9'
        self.assertEqual(cache['k2'], None)
        cache['k10'] = 'val10'
        self.assertEqual(cache['k1'], None)

        self.assertEqual(cache['k6'], 'val6')
        self.assertEqual(cache['k7'], 'val7')
        self.assertEqual(cache['k8'], 'val8')
        self.assertEqual(cache['k9'], 'val9')
        self.assertEqual(cache['k10'], 'val10')

    def test_del_sequence_1(self):
        cache = LRUCache(5)
        for i in range(5):
            cache['key' + str(i)] = 'val' + str(i)
        cache['key0'] = 'Now I am newest'
        cache['key100'] = 'I displace key1'
        self.assertEqual(cache['key0'], 'Now I am newest')
        self.assertEqual(cache['key1'], None)
        self.assertEqual(cache['key100'], 'I displace key1')
        for i in range(2, 4):
            self.assertEqual(cache['key' + str(i)], 'val' + str(i))

    def test_del_sequence_2(self):
        cache = LRUCache(5)
        for i in range(5):
            cache['key' + str(i)] = 'val' + str(i)
        # last used here 0 1 2 3 4 first used here
        for i in range(4, -1, -1):
            cache['key' + str(i)] = 'value' + str(i)
        # last used here 4 3 2 1 0 first used here
        cache['new_key'] = 'I displace key4'



if __name__ == "__main__":
    unittest.main()
