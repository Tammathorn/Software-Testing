import unittest
from alternatingCharacters import alternatingCharacters

class TestalternatingCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(alternatingCharacters(""), 0)

    def test_no_repeated_characters(self):
        self.assertEqual(alternatingCharacters("abcdef"), 0)

    def test_all_characters_repeated_once(self):
        self.assertEqual(alternatingCharacters("aabbcc"), 3)

    def test_repeated_characters_at_beginning(self):
        self.assertEqual(alternatingCharacters("aaabbbcc"), 5)

    def test_repeated_characters_at_end(self):
        self.assertEqual(alternatingCharacters("aabbccccc"), 6)

    def test_repeated_characters_in_middle(self):
        self.assertEqual(alternatingCharacters("abcddcba"), 1)

    def test_only_one_character(self):
        self.assertEqual(alternatingCharacters("aaaa"), 3)

    def test_multiple_repeated_characters(self):
        self.assertEqual(alternatingCharacters("aabbaabbccdd"), 6)

    def test_alternating_characters(self):
        self.assertEqual(alternatingCharacters("abababab"), 0)

    def test_maximum_length_string(self):
        self.assertEqual(alternatingCharacters("a" * 100000), 99999)

if __name__ == '__main__':
    unittest.main()
