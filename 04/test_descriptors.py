import unittest
from descriptors import Integer
from descriptors import PositiveInteger
from descriptors import String


class TestDescriptors(unittest.TestCase):
    @staticmethod
    def get_int_class():
        class Data:
            val = Integer()

            def method_1(self):
                pass

            def method_2(self):
                pass

            def __init__(self, val):
                self.val = val
        return Data

    @staticmethod
    def get_pos_int_class():
        class Data:
            val = PositiveInteger()

            def method_1(self):
                pass

            def method_2(self):
                pass

            def __init__(self, val):
                self.val = val

        return Data

    @staticmethod
    def get_string_class():
        class Data:
            val = String()

            def method_1(self):
                pass

            def method_2(self):
                pass

            def __init__(self, val):
                self.val = val

        return Data

    def test_int(self):
        class_data = TestDescriptors.get_int_class()

        self.assertRaises((ValueError,), lambda: class_data(1.2))
        self.assertRaises((ValueError,), lambda: class_data('12'))
        self.assertEqual(class_data(123).val, 123)
        self.assertEqual(class_data(-21).val, -21)

    def test_pos_int(self):
        class_data = TestDescriptors.get_pos_int_class()

        self.assertRaises((ValueError,), lambda: class_data(-2.2))
        self.assertRaises((ValueError,), lambda: class_data('4312'))
        self.assertRaises((ValueError,), lambda: class_data(0))
        self.assertRaises((ValueError,), lambda: class_data(-1))
        self.assertEqual(class_data(1234).val, 1234)
        self.assertEqual(class_data(1).val, 1)

        data = class_data(2)
        self.assertEqual(data.val, 2)
        data.val = 123
        self.assertEqual(data.val, 123)
        self.assertRaises((ValueError,), lambda: data.__setattr__('val', 0))

    def test_string(self):
        class_data = TestDescriptors.get_string_class()

        self.assertRaises((ValueError,), lambda: class_data(1))
        self.assertRaises((ValueError,), lambda: class_data(-1))
        self.assertRaises((ValueError,), lambda: class_data([]))
        self.assertEqual(class_data('Some string').val, 'Some string')
        self.assertEqual(class_data('').val, '')


if __name__ == "__main__":
    unittest.main()
