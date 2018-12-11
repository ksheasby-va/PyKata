import unittest

from part_1 import add_square_to_grid, make_grid


class AddSquareToGridTests(unittest.TestCase):

    def test_puts_single_point_in_top_left_corner(self):
        example = "#1 @ 0,0: 1x1"
        start_grid = [[".", "."], [".", "."]]
        expected = [["1", "."],
                    [".", "."]]

        result = add_square_to_grid(example, start_grid)
        self.assertEqual(expected, result)

    def test_puts_single_point_in_top_right_corner(self):
        example = "#1 @ 1,0: 1x1"
        start_grid = [[".", "."], [".", "."]]
        expected = [[".", "1"],
                    [".", "."]]

        result = add_square_to_grid(example, start_grid)
        self.assertEqual(expected, result)

    def test_puts_single_point_in_bottom_right_corner(self):
        example = "#1 @ 1,1: 1x1"
        start_grid = [[".", "."], [".", "."]]
        expected = [[".", "."],
                    [".", "1"]]

        result = add_square_to_grid(example, start_grid)
        self.assertEqual(expected, result)

    def test_puts_2_by_2_in_top_left_corner(self):
        example = "#1 @ 0,0: 2x2"
        start_grid = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        expected = [["1", "1", "."],
                    ["1", "1", "."],
                    [".", ".", "."]]

        result = add_square_to_grid(example, start_grid)
        self.assertEqual(expected, result)

    def test_puts_1_by_3_in_middle_row(self):
        example = "#1 @ 0,1: 3x1"
        start_grid = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        expected = [[".", ".", "."],
                    ["1", "1", "1"],
                    [".", ".", "."]]

        result = add_square_to_grid(example, start_grid)
        self.assertEqual(expected, result)

    def test_puts_1_by_3_in_second_row(self):
        example = "#1 @ 0,1: 3x1"
        start_grid = [[".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."]]
        expected = [[".", ".", ".", "."],
                    ["1", "1", "1", "."],
                    [".", ".", ".", "."],
                    [".", ".", ".", "."]]

        result = add_square_to_grid(example, start_grid)
        self.assertEqual(expected, result)


class MakeGridTests(unittest.TestCase):

    def test_puts_1_by_3_in_second_row(self):
        example = "#1 @ 0,1: 3x1"
        expected = [[".", ".", ".", "."],
                    ["1", "1", "1", "."],
                    [".", ".", ".", "."],
                    [".", ".", ".", "."]]

        result = make_grid(example, 4)
        self.assertEqual(expected, result)

    def test_puts_1_by_3_in_second_and_third_row(self):
        example = """#1 @ 0,1: 3x1
#2 @ 1,2: 3x1"""
        expected = [[".", ".", ".", "."],
                    ["1", "1", "1", "."],
                    [".", "2", "2", "2"],
                    [".", ".", ".", "."]]

        result = make_grid(example, 4)
        self.assertEqual(expected, result)

    def test_puts_overlapping_2x3_in_proper_places(self):
        example = """#1 @ 0,1: 3x2
#2 @ 1,2: 3x2"""
        expected = [[".", ".", ".", "."],
                    ["1", "1", "1", "."],
                    ["1", "X", "X", "2"],
                    [".", "2", "2", "2"]]

        result = make_grid(example, 4)
        self.assertEqual(expected, result)
