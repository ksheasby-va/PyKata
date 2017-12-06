import unittest

from day_05.day_05_2 import count_steps_to_reach_exit


class CountStepsToReachExitTests(unittest.TestCase):
    def test_count_steps_returns_5_for_0_3_0_1_negative_3(self):
        self.assertEqual(10, count_steps_to_reach_exit("""0\n3\n0\n1\n-3"""))
