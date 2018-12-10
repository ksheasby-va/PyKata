import unittest

from part_1 import does_id_have_2_or_3_repeating_letters, calculate_checksum


class DoesIdHave2Or3RepeatingLettersTests(unittest.TestCase):

    def test_abcdef_returns_0s(self):
        example = "abcdef"
        expected = False, False
        result = does_id_have_2_or_3_repeating_letters(example)

        self.assertEqual(result, expected)

    def test_bababc_returns_1_and_1(self):
        example = "bababc"
        expected = True, True
        result = does_id_have_2_or_3_repeating_letters(example)

        self.assertEqual(result, expected)

    def test_abbcde_returns_1_and_0(self):
        example = "abbcde"
        expected = True, False
        result = does_id_have_2_or_3_repeating_letters(example)

        self.assertEqual(result, expected)

    def test_abcccd_returns_0_and_1(self):
        example = "abcccd"
        expected = False, True
        result = does_id_have_2_or_3_repeating_letters(example)

        self.assertEqual(result, expected)

    def test_aabcdd_returns_1_and_0(self):
        example = "aabcdd"
        expected = True, False
        result = does_id_have_2_or_3_repeating_letters(example)

        self.assertEqual(result, expected)

    def test_abcdee_returns_1_and_0(self):
        example = "aabcdd"
        expected = True, False
        result = does_id_have_2_or_3_repeating_letters(example)

        self.assertEqual(result, expected)

    def test_ababab_returns_0_and_1(self):
        example = "ababab"
        expected = False, True
        result = does_id_have_2_or_3_repeating_letters(example)

        self.assertEqual(result, expected)


class CalculateChecksumTests(unittest.TestCase):

    def test_example_ids_return_12(self):
        example = """
        abcdef
        ababab
        abcdee
        aabcdd
        abcccd
        abbcde
        bababc
        """
        self.assertEqual(12, calculate_checksum(example))
