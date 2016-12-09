import unittest

from day_08_1 import identify_command_type, execute_rect_command


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
