import unittest

from day_03_1 import count_triangles
from day_03_2 import split_string_by_columns
from day_03_input import INPUT


class SplitTrianglesByColumn(unittest.TestCase):
    def test_input_returns_proper_list_of_sides(self):
        input = '''2 3 4
        2 3 4
        3 3 10'''
        expected = '''2 2 3\n3 3 3\n4 4 10\n'''
        result = split_string_by_columns(input)
        self.assertEqual(expected, result)


class TestCountTrianglesWithColumnInput(unittest.TestCase):
    def test_3_3_3_and_3_12_4_returns_one(self):
        sides = '''3 3 3
        3 12 4
        5 10 25'''
        self.assertEqual(2, count_triangles(split_string_by_columns(sides)))


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        print count_triangles(split_string_by_columns(INPUT))
