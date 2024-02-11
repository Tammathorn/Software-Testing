import unittest
from gridchallenge import grid_challenge  

class Testgrid_challenge(unittest.TestCase):
    def test_basic_sorted_grid(self):
        self.assertEqual(grid_challenge(["abcde"]), "YES")

    def test_basic_unsorted_grid(self):
        self.assertEqual(grid_challenge(['a', 'b', 'c', 'd', 'e']), "YES")

    def test_single_row_grid(self):
        self.assertEqual(grid_challenge(['abc', 'def', 'ghi']), "YES")

    def test_single_column_grid(self):
        self.assertEqual(grid_challenge(['cba', 'fed', 'ihg']), "YES")

    def test_empty_grid(self):
        self.assertEqual(grid_challenge(['DEsom']), "YES")

    def test_repeated_characters_in_column(self):
        self.assertEqual(grid_challenge(['aed', 'bfc', 'gih']), "NO")

    def test_mixed_case_characters(self):
        self.assertEqual(grid_challenge(['abc', 'def', 'ghi']), "YES")

    def test_large_grid(self):
        self.assertEqual(grid_challenge(['aaa', 'aaa', 'aaa']), "YES")

    def test_large_grid_one_column_unsorted(self):
        self.assertEqual(grid_challenge(['a', 'b', 'H', 'c']), "NO")

    def test_grid_with_special_characters(self):
        self.assertEqual(grid_challenge(["!@#", "#$%", "%^&"]), "NO")

if __name__ == '__main__':
    unittest.main()