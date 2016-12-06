import unittest

from day_05_2 import calculate_password_dict


class CalculatePasswordDictTests(unittest.TestCase):

    def test_digit_1_for_abc_is_5(self):
        # change while loop comparison to be < 1 to run this test.
        expected = {1: '5'}
        result = calculate_password_dict('abc')
        self.assertDictEqual(expected, result)

    def test_dict_for_abc_contains_05ace8e3(self):
        expected = {
            0: '0',
            1: '5',
            2: 'a',
            3: 'c',
            4: 'e',
            5: '8',
            6: 'e',
            7: '3',
        }
        result = calculate_password_dict('abc')
        self.assertDictEqual(expected, result)


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        print calculate_password_dict('cxdnnyjw')