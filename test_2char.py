import unittest
from two_characters import two_characters

class Testtwo_characters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(two_characters(""), 0)

    def test_string_three_unique_char_no_alternating(self):
        self.assertEqual(two_characters("abcabcabc"), 0)

    def test_string_one_unique_char(self):
        self.assertEqual(two_characters("aaaa"), 0)

    def test_string_two_unique_char_no_alternating(self):
        self.assertEqual(two_characters("aabbcc"), 0)

    def test_string_two_unique_char_alternating(self):
        self.assertEqual(two_characters("ababab"), 6)

    def test_string_three_unique_char_no_alternating(self):
        self.assertEqual(two_characters("abcabcabc"), 6)

    def test_string_three_unique_char_alternating(self):
        self.assertEqual(two_characters("abababab"), 8)

    def test_string_mixed_char_alternating(self):
        self.assertEqual(two_characters("a1b2c3d4e5"), 2)

    def test_string_special_characters(self):
        self.assertEqual(two_characters("!@#$%^&*()"), 2)

    def test_string_numbers(self):
        self.assertEqual(two_characters("123456789"), 2)

    def test_string_mixed_case(self):
        self.assertEqual(two_characters("AbCdEfGhIjK"), 2)

if __name__ == '__main__':
    unittest.main()