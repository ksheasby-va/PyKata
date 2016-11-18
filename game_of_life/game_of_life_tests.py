import unittest

from game_of_life import make_grid_from_list, get_neighbours


class MakeGridFromListTests(unittest.TestCase):

    def test_returns_3_by_3_grid_of_dots(self):
        grid = make_grid_from_list(3, ['.', '.', '.', '.', '.', '.', '.', '.', '.'])
        print 'Grid: \n' + grid
        self.assertEqual(grid, '...\n...\n...\n')

    def test_check_neighbours_gets_proper_3_neighbours_for_top_corner(self):
        expected = [2, 4, 5]
        neighbours = get_neighbours(1, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertItemsEqual(expected, neighbours)

    def test_check_neighbours_gets_proper_8_neighbours_for_center_position(self):
        expected = [1, 2, 3, 4, 6, 7, 8, 9]
        neighbours = get_neighbours(5, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertItemsEqual(expected, neighbours)
