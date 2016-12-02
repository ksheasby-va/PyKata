import unittest

from day_01_2 import calculate_positions


class CalculateLocationTests(unittest.TestCase):

    def test_location_list_for_one_movement(self):
        result = calculate_positions(['L1'])
        self.assertEqual([(0, 0), (-1, 0)], result)

    def test_location_list_for_long_movement(self):
        result = calculate_positions(['L4'])
        self.assertEqual([(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0)], result)

    def test_location_list_for_many_movements(self):
        result = calculate_positions(['L1', 'R3', 'R2', 'L1'])
        self.assertEqual([(0, 0), (-1, 0), (-1, 1), (-1, 2), (-1, 3), (0, 3), (1, 3), (1, 4)], result)

    def test_location_list_for_duplicate_locations(self):
        result = calculate_positions(['R1', 'R1', 'R1', 'R3', 'L1', 'L4'])
        print result
        self.assertEqual([(0, 0), (1, 0), (1, -1), (0, -1), (0, 0)], result)


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        text = 'L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4'
        raw_movements = text.split()
        movements = []
        for item in raw_movements:
            movements.append(item.rstrip(','))
        positions = calculate_positions(movements)
        duplicate_point = positions[-1]
        print abs(duplicate_point[0]) + abs(duplicate_point[1])
