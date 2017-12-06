import unittest

from day_04.day_04_2 import is_passphrase_valid


class IsPassphraseValidTests(unittest.TestCase):
    def test_is_valid_returns_true_for_abcde_fghij(self):
        self.assertTrue(is_passphrase_valid('abcde fghij'))

    def test_is_valid_returns_false_for_abcde_xyz_ecdab(self):
        self.assertFalse(is_passphrase_valid('abcde xyz ecdab'))

    def test_is_valid_returns_true_for_a_ab_abc_abd_abf_abj(self):
        self.assertTrue(is_passphrase_valid('a ab abc abd abf abj'))

    def test_is_valid_returns_true_for_iiii_oiii_ooii_oooi_oooo(self):
        self.assertTrue(is_passphrase_valid('iiii oiii ooii oooi oooo'))

    def test_is_valid_returns_false_for_oiii_ioii_iioi_iiio(self):
        self.assertFalse(is_passphrase_valid('oiii ioii iioi iiio'))
