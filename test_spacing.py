import unittest

from spacing import make_line


class TestMakeLine(unittest.TestCase):
    def test_basic(self):
        input_values = range(0, 10) * 3
        expected = "012 345  678 901  234 567  890 123  456 789"
        self.assertEqual(make_line(input_values), expected)
