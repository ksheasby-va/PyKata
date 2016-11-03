import unittest

from game_of_life import make_grid_from_list


class MakeGridFromListTests(unittest.TestCase):

    def test_returns_2_by_2_grid_of_dots(self):
        grid = make_grid_from_list(2, ['.', '.', '.', '.'])
        self.assertEqual(grid, '..\n..\n')
