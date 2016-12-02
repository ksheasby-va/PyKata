import unittest

from game_of_life import make_grid_from_list, get_neighbours


class MakeGridFromListTests(unittest.TestCase):

    def test_returns_3_by_3_grid_of_dots(self):
        grid = make_grid_from_list(3, ['.', '.', '.', '.', '.', '.', '.', '.', '.'])
        print 'Grid: \n' + grid
        self.assertEqual(grid, '...\n...\n...\n')


class GetNeighboursTests(unittest.TestCase):

    def test_check_neighbours_gets_proper_3_neighbours_for_top_corner(self):
        expected = [2, 4, 5]
        neighbours = get_neighbours(1, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        print neighbours
        self.assertItemsEqual(expected, neighbours)

    def test_check_neighbours_gets_proper_8_neighbours_for_center_position(self):
        expected = [1, 2, 3, 4, 6, 7, 8, 9]
        neighbours = get_neighbours(5, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertItemsEqual(expected, neighbours)

    def test_check_for_neighbours_for_11_in_4_by_4_grid(self):
        expected = [6, 7, 8, 10, 12, 14, 15, 16]
        neighbours = get_neighbours(11, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertItemsEqual(expected, neighbours)

    def test_check_for_neighbours_for_15_in_4_by_4_grid(self):
        expected = [10, 11, 12, 14, 16]
        neighbours = get_neighbours(15, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertItemsEqual(expected, neighbours)

    def test_check_for_neighbours_for_9_in_4_by_4_grid(self):
        expected = [5, 6, 10, 13, 14]
        neighbours = get_neighbours(9, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertItemsEqual(expected, neighbours)

    def test_check_for_neighbours_for_12_in_4_by_4_grid(self):
        expected = [7, 8, 11, 15, 16]
        neighbours = get_neighbours(12, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertItemsEqual(expected, neighbours)
