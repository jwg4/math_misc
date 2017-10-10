import unittest

from hints import make_hints_text


class TestMakeHintsText(unittest.TestCase):
    def test_9_digits(self):
        expected = """141 - Foo
592 - Bar

635 - Baz
"""
        digits = [1, 4, 1, 5, 9, 2, 6, 3, 5]
        lookup = {
            '141': "Foo",
            '592': "Bar",
            '635': "Baz",
        }
        self.assertEqual(make_hints_text(digits, lookup), expected)
