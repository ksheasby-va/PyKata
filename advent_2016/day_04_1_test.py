import unittest

from day_04_1 import separate_parts, count_letters, get_five_most_frequent_letters


class SeparatePartsTests(unittest.TestCase):

    def test_returns_tuple_of_3_parts_of_id(self):
        input = 'aaaaa-bbb-z-y-x-123[abxyz]'
        expected = ('aaaaabbbzyx', '123', '[abxyz]')
        result = separate_parts(input)
        self.assertEqual(expected, result)


class CountLettersTests(unittest.TestCase):

    def test_counts_3_as_in_string(self):
        input_string = 'aaa'
        expected = {'a': 3}
        result = count_letters(input_string)
        self.assertDictEqual(expected, result)

    def test_counts_all_letters_in_string(self):
        input_string = 'aaabbcccdc'
        expected = {'a': 3, 'b': 2, 'c': 4, 'd': 1}
        result = count_letters(input_string)
        self.assertDictEqual(expected, result)


class GetTopFiveMostFrequentLettersTests(unittest.TestCase):

    def test_proper_letters_returned_in_order(self):
        input_dict = {'a': 7, 'b': 2, 'c': 4, 'd': 1, 'e': 4, 'f': 8, 'g': 1}
        expected = 'faceb'
        result = get_five_most_frequent_letters(input_dict)
        self.assertEqual(expected, result)

    def test_proper_letters_returned_in_order_from_unordered_dict(self):
        input_dict = {'a': 7, 'b': 2,  'd': 1, 'e': 4, 'f': 8, 'c': 4, 'g': 1}
        expected = 'faceb'
        result = get_five_most_frequent_letters(input_dict)
        self.assertEqual(expected, result)

    def test_proper_letters_in_order_for_checksum(self):
        parts = separate_parts('hqcfqwydw-fbqijys-whqii-huiuqhsx-660[qhiwf]')
        counts = count_letters(parts[0])
        result = get_five_most_frequent_letters(counts)
        self.assertEqual('qhiwf', result)

