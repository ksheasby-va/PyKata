import unittest

from part_1 import calculate_frequency


class DayOneAdditionTests(unittest.TestCase):
    def test_first_example_results_in_3(self):
        example = "+1, +1, +1"
        self.assertEqual(3, calculate_frequency(example))

    def test_second_example_results_in_0(self):
        example = "+1, +1, -2"
        self.assertEqual(0, calculate_frequency(example))

    def test_third_example_results_in_minus_6(self):
        example = "-1, -2, -3"
        self.assertEqual(-6, calculate_frequency(example))
