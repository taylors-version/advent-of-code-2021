import unittest
import day06

class MyTestCase(unittest.TestCase):
    data = "3,4,3,1,2"
    def test_puzzle1(self):
        self.assertEqual(5934, day06.puzzle1(self.data))

    def test_puzzle2(self):
        self.assertEqual(26984457539, day06.puzzle2(self.data))


if __name__ == '__main__':
    unittest.main()
