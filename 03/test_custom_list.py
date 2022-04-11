import unittest
import custom_list as cl


class TestCustomList(unittest.TestCase):
    def test_init_and_cast(self):
        py_list = [1, 2]
        my_list = cl.CustomList(py_list)
        py_my_list = list(my_list)
        self.assertEqual(py_list, py_my_list)

    def test_add_simple(self):
        my_list_1 = cl.CustomList([1, 2, 3])
        my_list_2 = cl.CustomList([4, 5, -1])
        result = my_list_1 + my_list_2
        result = list(result)
        self.assertEqual(result, [5, 7, 2])

    def test_add_with_diff_len(self):
        my_list_1 = cl.CustomList([10, 5, 14])
        my_list_2 = cl.CustomList([-4, -2])
        result = my_list_1 + my_list_2
        result = list(result)
        self.assertEqual(result, [6, 3, 14])

    def test_save_add_with_diff_len(self):
        my_list_1 = cl.CustomList([2, 3, 1])
        my_list_2 = cl.CustomList([-1, 10])
        result = my_list_1 + my_list_2
        result = list(result)
        self.assertEqual(result, [1, 13, 1])
        my_list_1 = list(my_list_1)
        my_list_2 = list(my_list_2)
        self.assertEqual(my_list_1, [2, 3, 1])
        self.assertEqual(my_list_2, [-1, 10])


if __name__ == "__main__":
    unittest.main()
