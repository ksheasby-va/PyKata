import unittest

from bowling_v2 import calc_score


class BowlingCalcTests(unittest.TestCase):

    def test_gutter_ball(self):
        self.assertEqual(0, calc_score([0]))

    def test_corner_pin(self):
        self.assertEqual(2, calc_score([2]))

    def test_open_frame(self):
        self.assertEqual(13, calc_score([2,3,8]))

    def test_closed_frames(self):
        self.assertEqual(30, calc_score([5,5,5,2,8,5]))

    def test_spare_and_open_frame(self):
        self.assertEqual(30, calc_score([3,12,5,2,3]))

    def test_spare_spare_and_open_frame(self):
        self.assertEqual(46, calc_score([2, 13, 8, 7, 3, 2, 0]))

    def test_strike_open_frame(self):
        self.assertEqual(30, calc_score([15, 2, 3, 5]))

    def test_strike_strike_open_frame(self):
        self.assertEqual(62, calc_score([15, 15, 2, 3, 5]))

    def test_strike_spare_and_open_frame(self):
        self.assertEqual(57, calc_score([15, 5, 10, 2, 3, 5]))

    def test_spare_strike_and_open_frame(self):
        self.assertEqual(60, calc_score([5, 10, 15, 2, 3, 5]))

    def test_turkey_open_frame(self):
        self.assertEqual(105, calc_score([15, 15, 15, 2, 3, 3]))
