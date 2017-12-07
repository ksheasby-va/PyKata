import unittest

from day_05_1 import get_hash_with_5_zeros, get_password_from_hash_results


class GetHashWith5ZerosTests(unittest.TestCase):

    def test_first_index_to_produce_5_zeros_is_3231929(self):
        expected = '00000155f8105dff7f56ee10fa9b9abd'
        result = get_hash_with_5_zeros('abc')[0]
        self.assertEqual(expected, result)


class GetLetterFromHashResultTests(unittest.TestCase):

    def test_first_digit_of_password_for_abc_is_8(self):
        expected = '1'
        result = get_password_from_hash_results('abc')
        self.assertEqual(expected, result)

    def test_first_2_digits_of_password_for_abc_are_18(self):
        # Change stop in xrange to 2 to run this test.
        expected = '18'
        result = get_password_from_hash_results('abc')
        self.assertEqual(expected, result)

    def test_password_for_abc_is_18f47a30(self):
        expected = '18f47a30'
        result = get_password_from_hash_results('abc')
        self.assertEqual(expected, result)


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        print get_password_from_hash_results('ugkcyxxp')
