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


if __name__ == "__main__":
    unittest.main()
