import unittest

from day_01_2 import calculate_halfway_sum


class DayOneHalfwayAdditionTests(unittest.TestCase):
    def test_calculate_halfway_sum_of_1212(self):
        self.assertEqual(6, calculate_halfway_sum(1212))

    def test_calculate_halfway_sum_of_1221(self):
        self.assertEqual(0, calculate_halfway_sum(1221))

    def test_calculate_halfway_sum_of_123425(self):
        self.assertEqual(4, calculate_halfway_sum(123425))

    def test_calculate_halfway_sum_of_123123(self):
        self.assertEqual(12, calculate_halfway_sum(123123))

    def test_calculate_halfway_sum_of_12131415(self):
        self.assertEqual(4, calculate_halfway_sum(12131415))
