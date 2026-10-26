import unittest
from app import add_numbers


class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -4), -6)

    def test_add_zero(self):
        self.assertEqual(add_numbers(7, 0), 7)


if __name__ == "__main__":
    unittest.main()
