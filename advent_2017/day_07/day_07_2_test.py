from unittest import TestCase

from day_07.day_07_2 import find_balanced_weight, single_weight, get_sub_weights


class SingleWeightTests(TestCase):

    def test_line_without_arrow_returns_proper_weight(self):
        self.assertEqual(66, single_weight('pbga (66)'))

    def test_line_with_arrow_returns_proper_weight(self):
        self.assertEqual(72, single_weight('fwft (72) -> ktlj, cntj, xhth'))


class GetAllWeightsTests(TestCase):

    def test_example_input_returns_proper_subweights(self):
        single_weights = {'havc': 66, 'ebii': 61, 'fwft': 72, 'jptl': 61, 'tknk': 41, 'cntj': 57, 'xhth': 57, 'ugml': 68, 'qoyq': 66, 'pbga': 66, 'ktlj': 57, 'padx': 45, 'gyxo': 61}
        children = {'padx': ['pbga', 'havc', 'qoyq'], 'fwft': ['ktlj', 'cntj', 'xhth'], 'tknk': ['ugml', 'padx', 'fwft'], 'ugml': ['gyxo', 'ebii', 'jptl']}
        program = 'padx'
        result = get_sub_weights(single_weights, program, children)
        self.assertEqual([66, 66, 66], result)

class FindBalancedWeightTests(TestCase):

    def test_example_input_returns_the_proper_weight(self):
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
        self.assertEqual(60, find_balanced_weight(input))
