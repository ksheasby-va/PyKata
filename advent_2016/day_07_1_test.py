import unittest

from day_07_1 import is_abba_set, find_abba_strings, cut_string


class IsABBASetTests(unittest.TestCase):

    def test_abba_is_an_ABBA_set(self):
        self.assertTrue(is_abba_set('abba'))

    def test_abab_is_not_an_ABBA_set(self):
        self.assertFalse(is_abba_set('abab'))


class FindABBASetTests(unittest.TestCase):

    def test_cabbad_returns_one(self):
        self.assertEqual(1, find_abba_strings('cabbad'))


class CutStringIntoPiecesTests(unittest.TestCase):

    def test_string_is_cut_into_pieces_with_delimiters_in_place(self):
        input_string = 'abc[def]ghi'
        result = cut_string(input_string)
        self.assertItemsEqual(['abc', '[def]', 'ghi'], result)
