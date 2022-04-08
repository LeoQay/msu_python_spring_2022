import unittest
import custom_list as cl


class TestCustomList(unittest.TestCase):
    def test_simple(self):
        c1 = cl.CustomList([1, 2])
        c2 = cl.CustomList([3, 4])
        self.assertEqual(c2 - c1, [2, 2])


if __name__ == "__main__":
    unittest.main()