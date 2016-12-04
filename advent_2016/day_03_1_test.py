import unittest

from day_03_1 import is_valid_triangle, count_triangles
from day_03_input import INPUT


class DetermineValidTriangleTests(unittest.TestCase):

    def test_3_3_3_triangle_is_a_triangle(self):
        self.assertTrue(is_valid_triangle([3, 3, 3]))

    def test_3_3_7_triangle_is_not_a_triangle(self):
        self.assertFalse(is_valid_triangle([3, 3, 7]))

    def test_2_4_5_triangle_is_a_triangle(self):
        self.assertTrue(is_valid_triangle([2, 4, 5]))

    def test_12_3_4_triangle_is_not_a_triangle(self):
        self.assertFalse(is_valid_triangle([12, 3, 4]))

    def test_3_12_4_triangle_is_not_a_triangle(self):
        self.assertFalse(is_valid_triangle([3, 12, 4]))

    def test_5_10_25_triangle_is_not_a_triangle(self):
        self.assertFalse(is_valid_triangle([5, 10, 25]))

    def test_5_10_15_triangle_is_not_a_triangle(self):
        self.assertFalse(is_valid_triangle([5, 10, 15]))


class CountRealTrianglesTests(unittest.TestCase):

    def test_3_3_3_and_2_4_5_returns_two(self):
        sides = '''3 3 3
        2 4 5'''
        self.assertEqual(2, count_triangles(sides))

    def test_3_3_3_and_3_12_4_returns_one(self):
        sides = '''3 3 3
        3 12 4
        5 10 25
        5 10 15'''
        self.assertEqual(1, count_triangles(sides))


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        print count_triangles(INPUT)
