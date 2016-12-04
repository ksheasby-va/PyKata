import unittest

from day_04_1 import separate_parts


class SeparatePartsTests(unittest.TestCase):

    def test_returns_tuple_of_3_parts_of_id(self):
        input = 'aaaaa-bbb-z-y-x-123[abxyz]'
        expected = ('aaaaabbbzyx', '123', '[abxyz]')
        result = separate_parts(input)
        self.assertEqual(expected, result)
