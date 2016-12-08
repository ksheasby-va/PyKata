import unittest

from day_07_2 import get_bab, is_aba, separate_different_ip_pieces, supports_ssl, find_aba_strings
from day_07_input import INPUT_07


class GetBABTests(unittest.TestCase):

    def test_ghg_has_bab_of_hgh(self):
        aba = 'ghg'
        expected = 'hgh'
        result = get_bab(aba)
        self.assertEqual(expected, result)


class IsABATests(unittest.TestCase):

    def test_ghg_is_an_aba(self):
        aba = 'ghg'
        self.assertTrue(is_aba(aba))

    def test_ghj_is_not_an_aba(self):
        not_aba = 'ghj'
        self.assertFalse(is_aba(not_aba))

    def test_ggg_is_not_an_aba(self):
        not_aba = 'ggg'
        self.assertFalse(is_aba(not_aba))


class SeparateDifferentIPPiecesTests(unittest.TestCase):

    def test_foo(self):
        pieces = ['abc', '[def]', 'ghi']
        expected = (['abc', 'ghi'], ['[def]'])
        result = separate_different_ip_pieces(pieces)
        self.assertTupleEqual(expected, result)


class FindABAStringsTests(unittest.TestCase):

    def test_ghg_finds_single_aba(self):
        input_string = 'ghg'
        expected = ['ghg']
        result = find_aba_strings(input_string)
        self.assertListEqual(expected, result)

    def test_ghghg_finds_three_abas(self):
        input_string = 'ghghg'
        expected = ['ghg', 'hgh', 'ghg']
        result = find_aba_strings(input_string)
        self.assertListEqual(expected, result)

    def test_ghgdftyt_finds_two_abas(self):
        input_string = 'ghgdftyt'
        expected = ['ghg', 'tyt']
        result = find_aba_strings(input_string)
        self.assertListEqual(expected, result)


class SupportsSSLTests(unittest.TestCase):

    def test_aba_bab_xyz_does_support_SSL(self):
        ip = 'aba[bab]xyz'
        self.assertTrue(supports_ssl(ip))

    def test_xyz_xyz_xyz_does_not_support_SSL(self):
        ip = 'xyx[xyx]xyx'
        self.assertFalse(supports_ssl(ip))

    def test_aaa_kek_eke_does_support_SSL(self):
        ip = 'aaa[kek]eke'
        self.assertTrue(supports_ssl(ip))

    def test_zazbz_bzb_cdb_does_support_SSL(self):
        ip = 'zazbz[bzb]cdb'
        self.assertTrue(supports_ssl(ip))


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        count = 0
        for line in INPUT_07.splitlines():
            if supports_ssl(line):
                count += 1

        print count
