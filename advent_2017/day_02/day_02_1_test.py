import unittest

from day_02.day_02_1 import calculate_checksum


class CalculateChecksumTests(unittest.TestCase):
    def test_example_input_is_18(self):
        self.assertEqual(18, calculate_checksum(['5 1 9 5','7 5 3','2 4 6 8',]))
