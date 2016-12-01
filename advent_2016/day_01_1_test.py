import unittest

from day_01_1 import calculate_distance


class CalculateDistanceTests(unittest.TestCase):

    def test_calculate_distance_basic(self):
        result = calculate_distance(['L1', 'R1'])

        self.assertEqual(2, result)

    def test_calculate_distance_3(self):
        result = calculate_distance(['L1', 'R2'])

        self.assertEqual(3, result)
