import unittest

from day_04.day_04_1 import is_passphrase_valid, count_valid_passphrases


class IsPassphraseValidTests(unittest.TestCase):
    def test_is_valid_returns_true_for_aa_bb_cc_dd_ee(self):
        self.assertTrue(is_passphrase_valid('aa bb cc dd ee'))

    def test_is_valid_returns_true_for_aa_bb_cc_dd_aaa(self):
        self.assertTrue(is_passphrase_valid('aa bb cc dd aaa'))

    def test_is_valid_returns_false_for_aa_bb_cc_dd_aa(self):
        self.assertFalse(is_passphrase_valid('aa bb cc dd aa'))


class CountUniqueWordsTests(unittest.TestCase):
    def test_count_valid_passphrases_returns_1(self):
        self.assertEqual(1, count_valid_passphrases("""aa bb cc dd ee"""))

    def test_count_valid_passphrases_returns_2(self):
        self.assertEqual(2, count_valid_passphrases("""aa bb cc dd ee
        aa bb cc dd aaa"""))
