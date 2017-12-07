import unittest

from day_06.day_06_1 import count_memory_reallocations


class CountMemoryReallocationsTests(unittest.TestCase):

    def test_0_2_7_0_returns_5(self):
        self.assertEqual(5, count_memory_reallocations([0, 2, 7, 0]))
