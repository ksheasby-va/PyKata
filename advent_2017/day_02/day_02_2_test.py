import unittest

from day_02.day_02_2 import calculate_divisible_numbers


class CalculateDivisibleNumbersTests(unittest.TestCase):

    def test_calculate_divisible_numbers_example(self):
        self.assertEqual(9, calculate_divisible_numbers(['5 9 2 8','9 4 7 3','3 8 6 5']))
