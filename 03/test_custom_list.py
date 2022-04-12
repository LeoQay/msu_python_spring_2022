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

    def test_str_2(self):
        my_list = cl.CustomList([1])
        self.assertEqual(str(my_list), '[1], sum=1')

    def test_str_3(self):
        my_list = cl.CustomList([1, -23, 0, 122, 2])
        self.assertEqual(str(my_list), '[1, -23, 0, 122, 2], sum=102')


class TestCustomListEQ(TestCustomList):
    def test_eq_simple(self):
        self.assertTrue(cl.CustomList([1, 2]) == cl.CustomList([0, 3]))

    def test_eq_size_1(self):
        self.assertTrue(cl.CustomList([10]) == cl.CustomList([10]))
        self.assertTrue(cl.CustomList([100]) == [100])
        self.assertTrue([-23] == cl.CustomList([-23]))
        self.assertFalse(cl.CustomList([1]) == cl.CustomList([2]))
        self.assertFalse(cl.CustomList([-2]) == [22])
        self.assertFalse([4] == cl.CustomList([3]))

    def test_eq_size_2(self):
        self.assertTrue(cl.CustomList([1, 3]) == cl.CustomList([2, 2]))
        self.assertTrue(cl.CustomList([1, 5]) == [3, 3])
        self.assertTrue([2, -20] == cl.CustomList([-10, -8]))
        self.assertFalse(cl.CustomList([1, 5]) == cl.CustomList([1, 4]))
        self.assertFalse(cl.CustomList([-2, 3]) == [34, -32])
        self.assertFalse([1, 45] == cl.CustomList([5, 23]))

    def test_eq_diff_size(self):
        self.assertTrue(cl.CustomList([1, 2, 0, 0, 0, -1, 0, 1, 0, 3]) == cl.CustomList([1, 2, 3]))
        self.assertTrue(cl.CustomList([2, 10, -8]) == [2, -3, -12, 10, 7])
        self.assertTrue([10] == cl.CustomList([1, 1, 1, 1, 0, -1, 7]))
        self.assertFalse(cl.CustomList([1, 2, 3]) == cl.CustomList([1, 2, 3, 1]))
        self.assertFalse(cl.CustomList([2, 1, -12]) == [1, 2, 1, -12])
        self.assertFalse([2, 3, 1, 2] == cl.CustomList([1, -12, 12, 123, -123, 10]))


class TestCustomListNE(TestCustomList):
    def test_ne_simple(self):
        self.assertFalse(cl.CustomList([1, 2]) != cl.CustomList([0, 3]))

    def test_ne_size_1(self):
        self.assertFalse(cl.CustomList([10]) != cl.CustomList([10]))
        self.assertFalse(cl.CustomList([100]) != [100])
        self.assertFalse([-23] != cl.CustomList([-23]))
        self.assertTrue(cl.CustomList([1]) != cl.CustomList([2]))
        self.assertTrue(cl.CustomList([-2]) != [22])
        self.assertTrue([4] != cl.CustomList([3]))

    def test_ne_size_2(self):
        self.assertFalse(cl.CustomList([1, 3]) != cl.CustomList([2, 2]))
        self.assertFalse(cl.CustomList([1, 5]) != [3, 3])
        self.assertFalse([2, -20] != cl.CustomList([-10, -8]))
        self.assertTrue(cl.CustomList([1, 5]) != cl.CustomList([1, 4]))
        self.assertTrue(cl.CustomList([-2, 3]) != [34, -32])
        self.assertTrue([1, 45] != cl.CustomList([5, 23]))

    def test_ne_diff_size(self):
        self.assertFalse(cl.CustomList([1, 2, 0, 0, 0, -1, 0, 1, 0, 3]) != cl.CustomList([1, 2, 3]))
        self.assertFalse(cl.CustomList([2, 10, -8]) != [2, -3, -12, 10, 7])
        self.assertFalse([10] != cl.CustomList([1, 1, 1, 1, 0, -1, 7]))
        self.assertTrue(cl.CustomList([1, 2, 3]) != cl.CustomList([1, 2, 3, 1]))
        self.assertTrue(cl.CustomList([2, 1, -12]) != [1, 2, 1, -12])
        self.assertTrue([2, 3, 1, 2] != cl.CustomList([1, -12, 12, 123, -123, 10]))


class TestCustomListLT(TestCustomList):
    def test_lt_simple(self):
        my_list_1 = cl.CustomList([2])
        my_list_2 = cl.CustomList([1])
        self.assertFalse(my_list_1 < my_list_2)
        self.assertTrue(my_list_2 < my_list_1)

    def test_lt_diff_len(self):
        my_list_1 = cl.CustomList([1, 4, 3, 2])
        my_list_2 = cl.CustomList([4, 2, 1])
        self.assertFalse(my_list_1 < my_list_2)
        self.assertTrue(my_list_2 < my_list_1)

    def test_lt_near_value(self):
        my_list_1 = cl.CustomList([1, 2])
        my_list_2 = cl.CustomList([-1, 2, 3])
        self.assertTrue(my_list_1 < my_list_2)
        self.assertFalse(my_list_2 < my_list_1)

    def test_lt_equal_value(self):
        my_list_1 = cl.CustomList([4, 2])
        my_list_2 = cl.CustomList([-3, 6, 3])
        self.assertFalse(my_list_1 < my_list_2)
        self.assertFalse(my_list_2 < my_list_1)


class TestCustomListLE(TestCustomList):
    def test_le_simple(self):
        my_list_1 = cl.CustomList([2])
        my_list_2 = cl.CustomList([1])
        self.assertFalse(my_list_1 <= my_list_2)
        self.assertTrue(my_list_2 <= my_list_1)

    def test_le_diff_len(self):
        my_list_1 = cl.CustomList([1, 4, 3, 2])
        my_list_2 = cl.CustomList([4, 2, 1])
        self.assertFalse(my_list_1 <= my_list_2)
        self.assertTrue(my_list_2 <= my_list_1)

    def test_le_near_value(self):
        my_list_1 = cl.CustomList([1, 2])
        my_list_2 = cl.CustomList([-1, 2, 3])
        self.assertTrue(my_list_1 <= my_list_2)
        self.assertFalse(my_list_2 <= my_list_1)

    def test_le_equal_value(self):
        my_list_1 = cl.CustomList([4, 2])
        my_list_2 = cl.CustomList([-3, 6, 3])
        self.assertTrue(my_list_1 <= my_list_2)
        self.assertTrue(my_list_2 <= my_list_1)


class TestCustomListGT(TestCustomList):
    def test_gt_simple(self):
        my_list_1 = cl.CustomList([2])
        my_list_2 = cl.CustomList([1])
        self.assertTrue(my_list_1 > my_list_2)
        self.assertFalse(my_list_2 > my_list_1)

    def test_gt_diff_len(self):
        my_list_1 = cl.CustomList([10, 2, 3, 2])
        my_list_2 = cl.CustomList([-2, 1, 1])
        self.assertTrue(my_list_1 > my_list_2)
        self.assertFalse(my_list_2 > my_list_1)

    def test_gt_near_value(self):
        my_list_1 = cl.CustomList([-21, 22])
        my_list_2 = cl.CustomList([-1, 20, -19])
        self.assertTrue(my_list_1 > my_list_2)
        self.assertFalse(my_list_2 > my_list_1)

    def test_gt_equal_value(self):
        my_list_1 = cl.CustomList([40, 22])
        my_list_2 = cl.CustomList([-28, 85, 5])
        self.assertFalse(my_list_1 > my_list_2)
        self.assertFalse(my_list_2 > my_list_1)


class TestCustomListGE(TestCustomList):
    def test_ge_simple(self):
        my_list_1 = cl.CustomList([2])
        my_list_2 = cl.CustomList([1])
        self.assertTrue(my_list_1 >= my_list_2)
        self.assertFalse(my_list_2 >= my_list_1)

    def test_ge_diff_len(self):
        my_list_1 = cl.CustomList([10, 2, 3, 2])
        my_list_2 = cl.CustomList([-2, 1, 1])
        self.assertTrue(my_list_1 >= my_list_2)
        self.assertFalse(my_list_2 >= my_list_1)

    def test_ge_near_value(self):
        my_list_1 = cl.CustomList([-21, 22])
        my_list_2 = cl.CustomList([-1, 20, -19])
        self.assertTrue(my_list_1 >= my_list_2)
        self.assertFalse(my_list_2 >= my_list_1)

    def test_ge_equal_value(self):
        my_list_1 = cl.CustomList([40, 22])
        my_list_2 = cl.CustomList([-28, 85, 5])
        self.assertTrue(my_list_1 >= my_list_2)
        self.assertTrue(my_list_2 >= my_list_1)


if __name__ == "__main__":
    unittest.main()
