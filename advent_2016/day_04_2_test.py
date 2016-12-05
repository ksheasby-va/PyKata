import unittest

from day_04_2 import decrypt_room_name


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



