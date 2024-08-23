import unittest
from main import divide

class TestDivide(unittest.TestCase):
    def test_divide_success(self):
            self.assertEqual(divide(10, 2), 5)
            self.assertEqual(divide(10, 0), 0)
            self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
                self.assertRaises(TypeError, divide, 10, 0)



if __name__ == '__main__':
		unittest.main()