import unittest

from day_06.day_06_2 import count_memory_reallocations


class CountMemoryReallocationsTests(unittest.TestCase):

    def test_0_2_7_0_returns_4(self):
        self.assertEqual(4, count_memory_reallocations([0, 2, 7, 0]))
