#/usr/bin/env python
import unittest
class my_calc:
    def my_add(self, x, y):
        return x + y
    def my_sub(self, x, y):
        return x - y
    def my_mul(self, x, y):
        return x * y
    def my_div(self, x, y):
        return x / y

class test_func(unittest.TestCase):
    def setUp(self):
        self.mycalc = my_calc()

    def test_my_add(self):
        res = self.mycalc.my_add(1, 2)
        self.assertEqual(res, 3)

    def test_my_sub(self):
        res = self.mycalc.my_sub(2, 1)
        self.assertEqual(res, 1)

    def test_my_mul(self):
        res = self.mycalc.my_mul(2, 2)
        self.assertEqual(res, 4)

    def test_my_div(self):
        res = self.mycalc.my_div(2, 1)
        self.assertEqual(res, 2)

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(test_func('test_my_add'))
    suite.addTest(test_func('test_my_sub'))
    unittest.TextTestRunner().run(suite)
