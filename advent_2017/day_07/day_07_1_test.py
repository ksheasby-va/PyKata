from unittest import TestCase

from day_07.day_07_1 import find_bottom_program, first_letters, last_letters


class FirstLettersTests(TestCase):

    def test_line_without_arrow_returns_first_4_letters(self):
        input = "pbga (66)"
        self.assertEqual('pbga', first_letters(input))

    def test_line_with_arrow_returns_first_4_letters(self):
        input = "fwft (72) -> ktlj, cntj, xhth"
        self.assertEqual('fwft', first_letters(input))


class LastLettersTests(TestCase):

    def test_line_with_2_subtrees_returns_proper_last_letters(self):
        input = "cumfrfc (102) -> yjivxcf, swqkqgz"
        expected = ['yjivxcf', 'swqkqgz']
        self.assertEqual(expected, last_letters(input))

    def test_line_with_4_subtrees_returns_proper_last_letters(self):
        input = "iqsztjd (181) -> hovelvz, pndcqot, naglm, oxxlsk"
        expected = ['hovelvz', 'pndcqot', 'naglm', 'oxxlsk']
        self.assertEqual(expected, last_letters(input))


class FindBottomProgramTests(TestCase):
    def test_example_input_returns_tknk(self):
        input = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
        self.assertEqual('tknk', find_bottom_program(input))
