import unittest
import day05

class MyTestCase(unittest.TestCase):
    data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    def test_puzzle1(self):
        self.assertEqual(5, day05.puzzle1(self.data.splitlines()))

    def test_puzzle2(self):
        self.assertEqual(12, day05.puzzle2(self.data.splitlines()))


if __name__ == '__main__':
    unittest.main()
