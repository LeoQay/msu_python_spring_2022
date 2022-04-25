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


if __name__ == "__main__":
    unittest.main()