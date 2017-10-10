import unittest

from helpers import split


class TestSplit(unittest.TestCase):
    def test_50_element_list(self):
        input_s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwx"
        expected = [
            input_s[:30],
            input_s[30:]
        ]
        self.assertEqual(list(split(input_s, 30)), expected) 
