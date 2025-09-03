import unittest
import day02


class MyTestCase(unittest.TestCase):
    data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    def test_puzzle1(self):
        self.assertEqual(150, day02.puzzle1(self.data))

    def test_puzzle2(self):
        self.assertEqual(900, day02.puzzle2(self.data))



if __name__ == '__main__':
    unittest.main()
