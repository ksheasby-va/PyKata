import unittest

from part_2 import find_missing_number, make_grid


class FindMissingNumberTests(unittest.TestCase):

    def test_number_two_is_missing(self):
        self.assertEqual(2, find_missing_number([3, 1]))

    def test_number_three_is_missing(self):
        self.assertEqual(3, find_missing_number([2, 1]))


class MakeGridTests(unittest.TestCase):

    def test_three_is_only_unoverlapped(self):

        grid, overlapped = make_grid("""#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2""", 10)
        self.assertEqual({1, 2}, set(overlapped))
