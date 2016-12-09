import unittest

from day_08_1 import identify_command_type, COMMANDS


class IdentifyCommandTypeTests(unittest.TestCase):

    def test_rect_command_returns_rect(self):
        command = 'rect 3x2'
        expected = COMMANDS['RECT']
        result = identify_command_type(command)
        self.assertEqual(expected, result)
