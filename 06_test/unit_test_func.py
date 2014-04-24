#/usr/bin/env python
import unittest
from my_calc import my_add
class test_func(unittest.TestCase):
    def test_my_add(self):
        print("Test begin")
        res = my_add(1, 2)
        self.assertEqual(res, 3)

    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("Tear down")

if __name__ == "__main__":
    unittest.main()

