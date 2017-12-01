import unittest

from day_01_1 import calculate_sum


class DayOneAdditionTests(unittest.TestCase):
    def test_calculate_sum_of_1122(self):
        self.assertEqual(3, calculate_sum(1122))

    def test_calculate_sum_1234(self):
        self.assertEqual(0, calculate_sum(1234))

    def test_calculate_sum_1111(self):
        self.assertEqual(4, calculate_sum(1111))

    def test_calculate_sum_91212129(self):
        self.assertEqual(9, calculate_sum(91212129))
