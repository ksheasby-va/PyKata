import unittest

from roman import parse_numeral, add, reconstruct_numeral


class RomanNumeralParserTest(unittest.TestCase):

    def test_I_parses_as_one(self):
        self.assertEqual(1, parse_numeral('I'))

    def test_V_parses_as_five(self):
        self.assertEqual(5, parse_numeral('V'))

    def test_X_parses_as_ten(self):
        self.assertEqual(10, parse_numeral('X'))

    def test_II_parses_as_two(self):
        self.assertEqual(2, parse_numeral('II'))

    def test_III_parses_as_three(self):
        self.assertEqual(3, parse_numeral('III'))

    def test_IV_parses_as_four(self):
        self.assertEqual(4, parse_numeral('IV'))

    def test_XXXVIII_parses_as_38(self):
        self.assertEqual(38, parse_numeral('XXXVIII'))

    def test_XIV_parses_as_14(self):
        self.assertEqual(14, parse_numeral('XIV'))

    def test_I_plus_I_returns_2(self):
        self.assertEqual(2, add('I', 'I'))

    def test_I_plus_II_returns_3(self):
        self.assertEqual(3, add('I', 'II'))

    def test_IV_plus_V_returns_9(self):
        self.assertEqual(9, add('IV', 'V'))

    def test_I_plus_I_returns_II(self):
        self.assertEqual('II', reconstruct_numeral('I', 'I'))

    def test_I_plus_V_returns_VI(self):
        self.assertEqual('VI', reconstruct_numeral('I', 'V'))

    def test_II_plus_V_returns_VII(self):
        self.assertEqual('VII', reconstruct_numeral('II', 'V'))

    def test_VII_plus_V_returns_XII(self):
        self.assertEqual('XII', reconstruct_numeral('VII', 'V'))