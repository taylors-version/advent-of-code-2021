import unittest
import day03


class MyTestCase(unittest.TestCase):
    data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
    def test_puzzle1(self):
        self.assertEqual(198, day03.puzzle1(self.data))

    def test_puzzle2(self):
        self.assertEqual(230, day03.puzzle2(self.data))




if __name__ == '__main__':
    unittest.main()
