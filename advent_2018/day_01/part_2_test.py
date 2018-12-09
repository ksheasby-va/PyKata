import unittest

from part_2 import find_first_repeated_frequency


class DayOneFirstRepeatedFrequenctTests(unittest.TestCase):

    def test_first_example_returns_0(self):
        example = "+1, -1"
        self.assertEqual(0, find_first_repeated_frequency(example))

    def test_second_example_returns_10(self):
        example = "+3, +3, +4, -2, -4"
        self.assertEqual(10, find_first_repeated_frequency(example))

    def test_third_example_returns_5(self):
        example = "-6, +3, +8, +5, -6"
        self.assertEqual(5, find_first_repeated_frequency(example))

    def test_fourth_example_returns_14(self):
        example = "+7, +7, -2, -7, -4"
        self.assertEqual(14, find_first_repeated_frequency(example))
