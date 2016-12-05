import unittest

from day_04_1 import separate_parts
from day_04_2 import decrypt_room_name
from day_04_input import INPUT


class DecryptRoomTests(unittest.TestCase):

    def test_abc_3_returns_def(self):
        result = decrypt_room_name('abc', 3)
        self.assertEqual('def', result)

    def test_xyz_3_returns_abc(self):
        result = decrypt_room_name('xyz', 3)
        self.assertEqual('abc', result)

    def test_yza_5_returns_def(self):
        result = decrypt_room_name('yza', 5)
        self.assertEqual('def', result)

    def test_yza_26_returns_yza(self):
        result = decrypt_room_name('yza', 26)
        self.assertEqual('yza', result)

    def test_qzmt_343_returns_very(self):
        result = decrypt_room_name('qzmt', 343)
        self.assertEqual('very', result)


class RunWithInput(unittest.TestCase):

    def test_run_with_input(self):
        for room in INPUT.splitlines():
            result_tuple = separate_parts(room)
            room_name = decrypt_room_name(result_tuple[0], int(result_tuple[1]))
            if room_name == 'northpoleobjectstorage':
                print result_tuple[1]
