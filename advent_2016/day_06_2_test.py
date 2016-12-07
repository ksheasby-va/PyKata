import unittest

from day_06_2 import get_least_common_letter_in_column, get_least_common_letters
from day_06_input import INPUT


class GetMostCommonInColumnTests(unittest.TestCase):

    def test_most_common_letter_in_one_letter_rows(self):
        input_string = '''e
        f
        e'''
        expected = 'f'
        result = get_least_common_letter_in_column(input_string)
        self.assertEqual(expected, result)


class GetLeastCommonLettersTests(unittest.TestCase):

    def test_least_common_letters_in_two_columns_are_c_c(self):
        input_string = '''ab
        cb
        ac
        ab'''
        expected = 'cc'
        result = get_least_common_letters(input_string)
        self.assertEqual(expected, result)

    def test_least_common_letters_are_advent(self):
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
        expected = 'advent'
        result = get_least_common_letters(input_string)
        self.assertEqual(expected, result)


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        print get_least_common_letters(INPUT)
