import unittest
import custom_list as cl


class TestCustomList(unittest.TestCase):
    pass


class TestCustomListBase(TestCustomList):
    def test_init_and_cast(self):
        py_list = [1, 2]
        my_list = cl.CustomList(py_list)
        py_my_list = list(my_list)
        self.assertEqual(py_list, py_my_list)


class TestCustomListAdd(TestCustomList):
    def test_add_very_simple(self):
        self.assertEqual(list(cl.CustomList([1]) + cl.CustomList([2])), [3])

    def test_add_simple(self):
        my_list_1 = cl.CustomList([1, 2, 3])
        my_list_2 = cl.CustomList([4, 5, -1])
        result = my_list_1 + my_list_2
        self.assertEqual(type(result), cl.CustomList)
        result = list(result)
        self.assertEqual(result, [5, 7, 2])

    def test_add_with_diff_len(self):
        my_list_1 = cl.CustomList([10, 5, 14])
        my_list_2 = cl.CustomList([-4, -2])
        result = my_list_1 + my_list_2
        self.assertEqual(type(result), cl.CustomList)
        result = list(result)
        self.assertEqual(result, [6, 3, 14])

    def test_save_add_with_diff_len(self):
        my_list_1 = cl.CustomList([2, 3, 1])
        my_list_2 = cl.CustomList([-1, 10])
        result = my_list_1 + my_list_2
        self.assertEqual(type(result), cl.CustomList)
        result = list(result)
        self.assertEqual(result, [1, 13, 1])
        my_list_1 = list(my_list_1)
        my_list_2 = list(my_list_2)
        self.assertEqual(my_list_1, [2, 3, 1])
        self.assertEqual(my_list_2, [-1, 10])

    def test_save_add_with_bigger_diff_len(self):
        my_list_1 = cl.CustomList([2, 4])
        my_list_2 = cl.CustomList([-1, 10, -2, 0, 1, 2, 6])
        result = my_list_1 + my_list_2
        self.assertEqual(type(result), cl.CustomList)
        result = list(result)
        self.assertEqual(result, [1, 14, -2, 0, 1, 2, 6])
        my_list_1 = list(my_list_1)
        my_list_2 = list(my_list_2)
        self.assertEqual(my_list_1, [2, 4])
        self.assertEqual(my_list_2, [-1, 10, -2, 0, 1, 2, 6])

    def test_add_with_common_list_right(self):
        my_list = cl.CustomList([1, 2, 3])
        result = my_list + [1, 2]
        self.assertEqual(list(result), [2, 4, 3])
        self.assertEqual(type(result), cl.CustomList)
        my_list = cl.CustomList([2, 1, 3])
        result = my_list + [1, 2, 4, 1, 4]
        self.assertEqual(type(result), cl.CustomList)
        self.assertEqual(list(result), [3, 3, 7, 1, 4])

    def test_add_with_common_list_left(self):
        my_list = cl.CustomList([1, 2, 3])
        result = [1, 2] + my_list
        self.assertEqual(list(result), [2, 4, 3])
        self.assertEqual(type(result), cl.CustomList)
        my_list = cl.CustomList([4, 5])
        result = [5, 8, -1, 1, 2] + my_list
        self.assertEqual(type(result), cl.CustomList)
        self.assertEqual(list(result), [9, 13, -1, 1, 2])


class TestCustomListSub(TestCustomList):
    def test_sub_very_simple(self):
        self.assertEqual(list(cl.CustomList([1]) - cl.CustomList([2])), [-1])

    def test_sub_simple(self):
        my_list_1 = cl.CustomList([1, 2, 3])
        my_list_2 = cl.CustomList([4, 5, -1])
        result = my_list_1 - my_list_2
        self.assertEqual(type(result), cl.CustomList)
        result = list(result)
        self.assertEqual(result, [-3, -3, 4])

    def test_sub_with_diff_len(self):
        my_list_1 = cl.CustomList([10, 5, 14])
        my_list_2 = cl.CustomList([-4, -2])
        result = my_list_1 - my_list_2
        self.assertEqual(type(result), cl.CustomList)
        result = list(result)
        self.assertEqual(result, [14, 7, 14])

    def test_save_sub_with_diff_len(self):
        my_list_1 = cl.CustomList([2, 3, 1])
        my_list_2 = cl.CustomList([-1, 10])
        result = my_list_1 - my_list_2
        self.assertEqual(type(result), cl.CustomList)
        result = list(result)
        self.assertEqual(result, [3, -7, 1])
        my_list_1 = list(my_list_1)
        my_list_2 = list(my_list_2)
        self.assertEqual(my_list_1, [2, 3, 1])
        self.assertEqual(my_list_2, [-1, 10])

    def test_save_sub_with_bigger_diff_len(self):
        my_list_1 = cl.CustomList([2, 4])
        my_list_2 = cl.CustomList([-1, 10, -2, 0, 1, 2, 6])
        result = my_list_1 - my_list_2
        self.assertEqual(type(result), cl.CustomList)
        result = list(result)
        self.assertEqual(result, [3, -6, 2, 0, -1, -2, -6])
        my_list_1 = list(my_list_1)
        my_list_2 = list(my_list_2)
        self.assertEqual(my_list_1, [2, 4])
        self.assertEqual(my_list_2, [-1, 10, -2, 0, 1, 2, 6])

    def test_sub_with_common_list_right(self):
        my_list = cl.CustomList([1, 2, 3])
        result = my_list - [1, 2]
        self.assertEqual(list(result), [0, 0, 3])
        self.assertEqual(type(result), cl.CustomList)
        my_list = cl.CustomList([2, 1, 3])
        result = my_list - [1, 2, 4, 1, 4]
        self.assertEqual(type(result), cl.CustomList)
        self.assertEqual(list(result), [1, -1, -1, -1, -4])

    def test_sub_with_common_list_left(self):
        my_list = cl.CustomList([1, 2, 3])
        result = [1, 2] - my_list
        self.assertEqual(list(result), [0, 0, -3])
        self.assertEqual(type(result), cl.CustomList)
        my_list = cl.CustomList([4, 5])
        result = [5, 8, -1, 1, 2] - my_list
        self.assertEqual(type(result), cl.CustomList)
        self.assertEqual(list(result), [1, 3, -1, 1, 2])


class TestCustomListStr(TestCustomList):
    def test_str_1(self):
        my_list = cl.CustomList([1, 2, 3, 4])
        self.assertEqual(str(my_list), '[1, 2, 3, 4], sum=10')


if __name__ == "__main__":
    unittest.main()
