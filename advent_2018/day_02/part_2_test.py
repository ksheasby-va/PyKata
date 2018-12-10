import unittest

from part_2 import find_ids_1_letter_apart


class FindCorrectBoxIdsTests(unittest.TestCase):

    def test_example_input_finds_example_result(self):
        example = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""
        example_list = example.split("\n")
        result = "fghij", "fguij"

        self.assertEqual(result, find_ids_1_letter_apart(example_list, "fghij"))
