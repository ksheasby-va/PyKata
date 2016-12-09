import unittest

from day_08_1 import identify_command_type, execute_rect_command, execute_roty_command, execute_rotx_command, \
    count_octothorps_in_screen, count_pixels
from day_08_input import INPUT_08


class IdentifyCommandTypeTests(unittest.TestCase):

    def test_rect_command_returns_rect(self):
        command = 'rect 3x2'
        expected = 'rect'
        result = identify_command_type(command)
        self.assertEqual(expected, result)

    def test_rotate_x_returns_rotx(self):
        command = 'rotate column x=A by B'
        expected = 'rotx'
        result = identify_command_type(command)
        self.assertEqual(expected, result)

    def test_rotate_y_returns_roty(self):
        command = 'rotate row y=A by B'
        expected = 'roty'
        result = identify_command_type(command)
        self.assertEqual(expected, result)


class ExecuteRectCommandTests(unittest.TestCase):

    def test_rect_1_x_1_turns_on_top_corner(self):
        screen = [
            ['.'] * 5,
            ['.'] * 5,
            ['.'] * 5,
            ['.'] * 5,
            ['.'] * 5,
            ['.'] * 5,
        ]
        command = 'rect 1x1'
        screen = execute_rect_command(screen, command)
        expected = [
            ['#', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
        ]
        self.assertEqual(screen, expected)

    def test_rect_4_x_3_turns_on_top_corner(self):
        screen = [
            ['.'] * 5,
            ['.'] * 5,
            ['.'] * 5,
            ['.'] * 5,
            ['.'] * 5,
            ['.'] * 5,
        ]
        command = 'rect 4x3'
        screen = execute_rect_command(screen, command)
        expected = [
            ['#', '#', '#', '#', '.'],
            ['#', '#', '#', '#', '.'],
            ['#', '#', '#', '#', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
        ]
        self.assertEqual(screen, expected)


class ExecuteRotyCommandTests(unittest.TestCase):

    def test_rotate_top_row_by_1(self):
        screen = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        command = 'rotate row y=0 by 1'
        expected = [
            [3, 1, 2],
            [4, 5, 6],
            [7, 8, 9]
        ]
        result = execute_roty_command(screen, command)
        self.assertEqual(expected, result)

    def test_rotate_bottom_row_by_2(self):
        screen = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        command = 'rotate row y=2 by 2'
        expected = [
            [1, 2, 3],
            [4, 5, 6],
            [8, 9, 7]
        ]
        result = execute_roty_command(screen, command)
        self.assertEqual(expected, result)


class ExecuteRotxCommandTests(unittest.TestCase):

    def test_rotate_left_column_by_1(self):
        screen = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        command = 'rotate column y=0 by 1'
        expected = [
            [7, 2, 3],
            [1, 5, 6],
            [4, 8, 9]
        ]
        result = execute_rotx_command(screen, command)
        self.assertEqual(expected, result)

    def test_rotate_left_column_by_1(self):
        screen = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        command = 'rotate column y=1 by 2'
        expected = [
            [1, 5, 3],
            [4, 8, 6],
            [7, 2, 9]
        ]
        result = execute_rotx_command(screen, command)
        self.assertEqual(expected, result)


class CountOctothorpsTests(unittest.TestCase):

    def test_returns_3_otcothorps(self):
        screen = [
            ['#', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '#', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '#', '.'],
            ['.', '.', '.', '.', '.'],
        ]
        self.assertEqual(3, count_octothorps_in_screen(screen))

    def test_returns_7_otcothorps(self):
        screen = [
            ['#', '.', '.', '#', '.'],
            ['.', '#', '.', '.', '.'],
            ['.', '#', '.', '.', '.'],
            ['.', '#', '#', '.', '.'],
            ['.', '.', '.', '#', '.'],
            ['.', '.', '.', '.', '.'],
        ]
        self.assertEqual(7, count_octothorps_in_screen(screen))


class CountPixelsTests(unittest.TestCase):

    def test_case_from_site(self):
        screen = [
            ['.'] * 8,
            ['.'] * 8,
            ['.'] * 8,
        ]
        commands = '''rect 3x2
        rotate column x=1 by 1
        rotate row y=0 by 4
        rotate column x=1 by 1'''
        self.assertEqual(6, count_pixels(screen, commands))


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        screen = [
            ['.'] * 50,
            ['.'] * 50,
            ['.'] * 50,
            ['.'] * 50,
            ['.'] * 50,
            ['.'] * 50,
        ]
        print count_pixels(screen, INPUT_08)
