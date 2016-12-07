import unittest

from day_06_1 import get_most_common_letter_in_column, get_most_common_letters
from day_06_input import INPUT


class GetMostCommonInColumnTests(unittest.TestCase):

    def test_most_common_letter_in_one_letter_rows(self):
        input_string = '''e
        f
        e'''
        expected = 'e'
        result = get_most_common_letter_in_column(input_string)
        self.assertEqual(expected, result)


class GetMostCommonLettersTests(unittest.TestCase):

    def test_most_common_letters_in_two_columns_are_a_b(self):
        input_string = '''ab
        cb
        ac
        ab'''
        expected = 'ab'
        result = get_most_common_letters(input_string)
        self.assertEqual(expected, result)

    def test_most_common_letters_are_easter(self):
        input_string = '''eedadn
            drvtee
            eandsr
            raavrd
            atevrs
            tsrnev
            sdttsa
            rasrtv
            nssdts
            ntnada
            svetve
            tesnvt
            vntsnd
            vrdear
            dvrsen
            enarar'''
        expected = 'easter'
        result = get_most_common_letters(input_string)
        self.assertEqual(expected, result)


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        print get_most_common_letters(INPUT)
