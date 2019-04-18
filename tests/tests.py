import os
import sys
import unittest

sys.path.insert(0, '/Users/apple/Documents/MacBook_Pro/PyCharm/2019_04/TDD/Recipe')
from main import *




class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_mass(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(800), 8)


    def test_nitro_salt_returns_int(self):
        self.assertIsInstance(nitro_salt(1000), int)

    def test_nitro_salt_receives_string_returns_int(self):
        self.assertEqual(nitro_salt('1000'), 10)

    def test_nitro_salt_receives_alpha_string_returns_zero(self):
        self.assertEqual(nitro_salt('asdfadf'), 0)






class TestSalt(unittest.TestCase):
    def test_salt(self):
        self.assertEqual(salt(1000), 15)

class TestActivateCultures(unittest.TestCase):
    def test_cult(self):
        self.assertEqual(cultures(1000), 0.5)

class TestSugar(unittest.TestCase):
    def test_sugar(self):
        self.assertEqual(sugar(1000), 5)

class TestDays(unittest.TestCase):
    def test_days(self):
        self.assertEqual(days(1000), 4)

if __name__ == '__main__':
    unittest.main()
