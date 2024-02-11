import unittest
from caesarcipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    def test_basic_encryption_positive_shift(self):
        self.assertEqual(caesarCipher("abc", 1), "bcd")

    def test_basic_encryption_negative_shift(self):
        self.assertEqual(caesarCipher("abc", -1), "zab")

    def test_encryption_with_spaces(self):
        self.assertEqual(caesarCipher("hello world", 5), "mjqqt btwqi")

    def test_encryption_with_punctuation(self):
        self.assertEqual(caesarCipher("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_large_positive_shift(self):
        self.assertEqual(caesarCipher("abc", 27), "bcd")

    def test_large_negative_shift(self):
        self.assertEqual(caesarCipher("abc", -27), "zab")

    def test_empty_string(self):
        self.assertEqual(caesarCipher("", 3), "")

    def test_string_with_only_spaces(self):
        self.assertEqual(caesarCipher("   ", 2), "   ")

    def test_zero_shift(self):
        self.assertEqual(caesarCipher("abc", 0), "abc")

    def test_large_shift_greater_than_alphabet_size(self):
        self.assertEqual(caesarCipher("abC", 30), "efG")

if __name__ == '__main__':
    unittest.main()