import unittest
from custom_meta import CustomMeta


class TestCustomMeta(unittest.TestCase):
    def test_default(self):
        class CustomClass(metaclass=CustomMeta):
            x = 50

            def __init__(self, val=99):
                self.val = val

            @staticmethod
            def line():
                return 100

            def __str__(self):
                return "Custom_by_metaclass"

        obj = CustomClass(23)

        self.assertRaises((AttributeError,), lambda: obj.x)
        self.assertRaises((AttributeError,), lambda: obj.val)
        self.assertEqual(obj.custom_val, 23)
        self.assertEqual(obj.custom_x, 50)

        self.assertRaises((AttributeError,), lambda: obj.line)
        self.assertEqual(obj.custom_line(), 100)

        self.assertEqual(str(obj), 'Custom_by_metaclass')

        obj.dynamic = 45
        self.assertRaises((AttributeError,), lambda: obj.dynamic)
        self.assertEqual(obj.custom_dynamic, 45)


if __name__ == "__main__":
    unittest.main()
