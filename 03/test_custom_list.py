import unittest
import custom_list as cl
import random


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
        for _ in range(10):
            value = random.randint(-1000000, 1000000)
            self.assertTrue(cl.CustomList([value]) == cl.CustomList([value]))
            self.assertTrue(cl.CustomList([value]) == [value])
            self.assertTrue([value] == cl.CustomList([value]))
            value2 = value
            while value2 == value:
                value2 = random.randint(-1000000, 1000000)
            self.assertFalse(cl.CustomList([value]) == cl.CustomList([value2]))
            self.assertFalse(cl.CustomList([value2]) == [value])
            self.assertFalse([value2] == cl.CustomList([value]))

    def test_eq_size_2(self):
        for _ in range(10):
            value_list1 = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
            self.assertTrue(cl.CustomList(value_list1) == cl.CustomList(value_list1))
            self.assertTrue(cl.CustomList(value_list1) == value_list1)
            self.assertTrue(value_list1 == cl.CustomList(value_list1))
            value_list2 = value_list1
            while sum(value_list2) == sum(value_list1):
                value_list2 = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
            self.assertFalse(cl.CustomList(value_list1) == cl.CustomList(value_list2))
            self.assertFalse(cl.CustomList(value_list1) == value_list2)
            self.assertFalse(value_list2 == cl.CustomList(value_list1))

    def test_eq_rand_size(self):
        for _ in range(10):
            sizes = [random.randint(1, 100), random.randint(1, 100)]
            lists = [[random.randint(-100000, 100000) for _ in range(sizes[i])] for i in range(2)]
            if sum(lists[0]) == sum(lists[1]):
                self.assertTrue(cl.CustomList(lists[0]) == cl.CustomList(lists[1]))
                self.assertTrue(cl.CustomList(lists[0]) == lists[1])
                self.assertTrue(lists[0] == cl.CustomList(lists[1]))
            else:
                self.assertFalse(cl.CustomList(lists[0]) == cl.CustomList(lists[1]))
                self.assertFalse(cl.CustomList(lists[0]) == lists[1])
                self.assertFalse(lists[0] == cl.CustomList(lists[1]))


class TestCustomListNE(TestCustomList):
    def test_ne_simple(self):
        self.assertFalse(cl.CustomList([1, 2]) != cl.CustomList([0, 3]))

    def test_eq_size_1(self):
        for _ in range(10):
            value = random.randint(-1000000, 1000000)
            self.assertFalse(cl.CustomList([value]) != cl.CustomList([value]))
            self.assertFalse(cl.CustomList([value]) != [value])
            self.assertFalse([value] != cl.CustomList([value]))
            value2 = value
            while value2 == value:
                value2 = random.randint(-1000000, 1000000)
            self.assertTrue(cl.CustomList([value]) != cl.CustomList([value2]))
            self.assertTrue(cl.CustomList([value2]) != [value])
            self.assertTrue([value2] != cl.CustomList([value]))

    def test_eq_size_2(self):
        for _ in range(10):
            value_list1 = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
            self.assertFalse(cl.CustomList(value_list1) != cl.CustomList(value_list1))
            self.assertFalse(cl.CustomList(value_list1) != value_list1)
            self.assertFalse(value_list1 != cl.CustomList(value_list1))
            value_list2 = value_list1
            while sum(value_list2) == sum(value_list1):
                value_list2 = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
            self.assertTrue(cl.CustomList(value_list1) != cl.CustomList(value_list2))
            self.assertTrue(cl.CustomList(value_list1) != value_list2)
            self.assertTrue(value_list2 != cl.CustomList(value_list1))

    def test_eq_rand_size(self):
        for _ in range(10):
            sizes = [random.randint(1, 100), random.randint(1, 100)]
            lists = [[random.randint(-100000, 100000) for _ in range(sizes[i])] for i in range(2)]
            if sum(lists[0]) == sum(lists[1]):
                self.assertFalse(cl.CustomList(lists[0]) != cl.CustomList(lists[1]))
                self.assertFalse(cl.CustomList(lists[0]) != lists[1])
                self.assertFalse(lists[0] != cl.CustomList(lists[1]))
            else:
                self.assertTrue(cl.CustomList(lists[0]) != cl.CustomList(lists[1]))
                self.assertTrue(cl.CustomList(lists[0]) != lists[1])
                self.assertTrue(lists[0] != cl.CustomList(lists[1]))


if __name__ == "__main__":
    unittest.main()
