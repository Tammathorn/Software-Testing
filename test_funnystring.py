import unittest
from funny_string import funnyString

class TestFunnyString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(funnyString(""), "Funny")

    def test_single_character(self):
        self.assertEqual(funnyString("a"), "Funny")

    def test_two_characters(self):
        self.assertEqual(funnyString("ab"), "Funny")

    def test_three_characters(self):
        self.assertEqual(funnyString("abc"), "Funny")

    def test_characters_ascending_order(self):
        self.assertEqual(funnyString("abcd"), "Funny")

    def test_characters_descending_order(self):
        self.assertEqual(funnyString("dcba"), "Funny")

    def test_characters_random_order_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_characters_random_order_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_special_characters(self):
        self.assertEqual(funnyString("!@#$"), "Not Funny")

    def test_numbers(self):
        self.assertEqual(funnyString("1234"), "Funny")

if __name__ == '__main__':
    unittest.main()