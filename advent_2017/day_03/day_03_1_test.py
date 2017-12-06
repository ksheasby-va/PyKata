import unittest

from day_03.day_03_1 import build_spiral


class BuildSpiralTests(unittest.TestCase):

    def test_build_spiral_of_5_returns_proper_matrix(self):
        expected = [[5, 4, 3], [None, 1, 2], [None, None, None]]
        result = build_spiral(5)
        self.assertEqual(expected, result)

    def test_build_spiral_of_12_returns_proper_matrix(self):
        expected = [[None, None, None, None], [5, 4, 3, 12], [6, 1, 2, 11], [7, 8, 9, 10]]
        result = build_spiral(14)
        self.assertEqual(expected, result)
