import unittest
import Receiver
from Receiver.receiver import remove_invalid_reading, get_valid_reading, get_data_from_sender_stream, get_range_reading


class ReceiverTesting(unittest.TestCase):

    def test_remove_invalid_reading_contain_InvalidRange(self):
        self.assertEqual(remove_invalid_reading(["12", "0", "InvalidRange", "-1", "InvalidRange"]), ["12", "0", "-1"])

    def test_remove_invalid_reading(self):
        self.assertEqual(remove_invalid_reading(["-1", "0", "2"]), ["-1", "0", "2"])

    def test_get_valid_reading_Equal(self):
        self.assertEqual(get_valid_reading(["Temperature", "67", "-3", "0", "InvalidRange"]), ('Temperature', [67, -3, 0]))

    def test_get_valid_reading_notEqual(self):
        self.assertNotEqual(get_valid_reading(["Temperature", "67", "-3", "0", "InvalidRange"]), (["Temperature", "67", "-3", "0"]))

    def test_get_data_with_valid_reading(self):
        self.assertEqual(
            get_data_from_sender_stream(['Temperature, SOC\n', '45,0\n', '-1,5\n', '80,-2\n', '37,8\n', '23,-4\n']),
            ("Temperature", [45, -1, 80, 37, 23], "SOC", [0, 5, -2, 8, -4]))

    def test_get_data_with_invalid_range(self):
        self.assertEqual(get_data_from_sender_stream(
            ['Temperature, SOC\n', 'Invalid Range,0\n', '45,Invalid Range\n', '-1,5\n', 'Invalid Range,Invalid Range\n', '23,-4\n',
             '80,0\n']), ("Temperature", [45, -1, 23, 80], "SOC", [0, 5, -4, 0]))

    def test_get_range_reading_list(self):
        self.assertEqual(get_range_reading([-1, 0, 3, -5]), (-5, 3))

    def test_get_range_reading_empty_list(self):
        self.assertEqual(get_range_reading([]), (None, None))






