import unittest

from day_01_1 import calculate_distance


class CalculateDistanceTests(unittest.TestCase):

    def test_calculate_distance_basic(self):
        calculate_distance(['L1', 'R1'])
