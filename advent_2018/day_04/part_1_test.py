import unittest

from part_1 import map_sleeping_minutes, get_total_asleep_time, most_asleep, most_slept_minute, foo


class MapSleepingMinutesTests(unittest.TestCase):

    def test_example_input_returns_240(self):
        self.maxDiff = None
        expected = EXPECTED_MAPPING

        result = map_sleeping_minutes(EXAMPLE_INPUT)
        self.assertDictEqual(expected, result)

    def test_calc_total_minutes_asleep_returns_expected_dict(self):
        expected = {10: 50, 99: 30}
        result = get_total_asleep_time(EXPECTED_MAPPING)
        self.assertDictEqual(expected, result)

    def test_find_max_slept_minutes_returns_guard_10(self):
        result = most_asleep({10: 50, 99: 30})
        self.assertEqual(10, result)

    def test_most_slept_minute_returns_24_for_guard_10(self):
        result = most_slept_minute(EXPECTED_MAPPING, 10)
        self.assertEqual(24, result)

    def test_most_slept_minute_returns_45(self):
        result = most_slept_minute(EXPECTED_MAPPING, 99)
        self.assertEqual(45, result)

    def test_foo_returns_the_proper_result(self):
        result = foo(EXAMPLE_INPUT)
        self.assertEqual(240, result)


EXPECTED_MAPPING = {10: {5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:1, 20:1, 21:1, 22:1, 23:1, 24:2, 25:1, 26:1, 27:1, 28:1, 30:1, 31:1, 32:1, 33:1, 34:1, 35:1, 36:1, 37:1, 38:1, 39:1, 40:1, 41:1, 42:1, 43:1, 44:1, 45:1, 46:1, 47:1, 48:1, 49:1, 50:1, 51:1, 52:1, 53:1, 54:1},
                    99: {36:1, 37:1, 38:1, 39:1, 40:2, 41:2, 42:2, 43:2, 44:2, 45:3, 46:2, 47:2, 48:2, 49:2, 50:1, 51:1, 52:1, 53:1, 54:1}}


EXAMPLE_INPUT = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:25] wakes up
[1518-11-01 00:05] falls asleep
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-02 00:40] falls asleep
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-03 00:29] wakes up
[1518-11-04 00:36] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-04 00:46] wakes up
[1518-11-05 00:55] wakes up"""
