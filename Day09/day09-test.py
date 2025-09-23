import unittest
import day09

class MyTestCase(unittest.TestCase):
    data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    def test_puzzle1(self):
        self.assertEqual(15, day09.puzzle1(self.data.splitlines()))
        ben = """123
456
789"""
        self.assertEqual(2, day09.puzzle1(ben.splitlines()))


    def test_puzzle2(self):
        self.assertEqual(1134, day09.puzzle2(self.data.splitlines()))


if __name__ == '__main__':
    unittest.main()
