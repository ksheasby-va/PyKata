import unittest

from day_07_1 import is_abba_set, find_abba_strings, cut_string, supports_tls
from day_07_input import INPUT_07


class IsABBASetTests(unittest.TestCase):

    def test_abba_is_an_ABBA_set(self):
        self.assertTrue(is_abba_set('abba'))

    def test_abab_is_not_an_ABBA_set(self):
        self.assertFalse(is_abba_set('abab'))

    def test_aaaa_is_not_an_ABBA_set(self):
        self.assertFalse(is_abba_set('aaaa'))


class FindABBAStringsTests(unittest.TestCase):

    def test_cabbad_returns_true(self):
        self.assertTrue(find_abba_strings('cabbad'))

    def test_cababd_returns_false(self):
        self.assertFalse(find_abba_strings('cababd'))


class CutStringIntoPiecesTests(unittest.TestCase):

    def test_string_is_cut_into_pieces_with_delimiters_in_place(self):
        input_string = 'abc[def]ghi'
        result = cut_string(input_string)
        self.assertItemsEqual(['abc', '[def]', 'ghi'], result)


class SupportsTLSTests(unittest.TestCase):

    def test_abba_mnop_qrst_does_support_tls(self):
        input_string = 'abba[mnop]qrst'
        self.assertTrue(supports_tls(input_string))

    def test_abcd_bddb_xyyx_does_not_support_tls(self):
        input_string = 'abcd[bddb]xyyx'
        self.assertFalse(supports_tls(input_string))

    def test_aaaa_qwer_tyui_does_not_support_tls(self):
        input_string = 'aaaa[qwer]tyui'
        self.assertFalse(supports_tls(input_string))

    def test_ioxxoj_asdfgh_tyui_does_support_tls(self):
        input_string = 'ioxxoj[asdfgh]zxcvbn'
        self.assertTrue(supports_tls(input_string))


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        print supports_tls(INPUT_07)
