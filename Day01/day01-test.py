import unittest
import day01


class MyTestCase(unittest.TestCase):
    data = """199
200
208
210
200
207
240
269
260
263"""
    def test_puzzle1(self):
        self.assertEqual(7, day01.puzzle1(self.data))  # add assertion here

    def test_puzzle2(self):
        self.assertEqual(5, day01.puzzle2(self.data))


if __name__ == '__main__':
    unittest.main()
