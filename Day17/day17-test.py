import unittest
import day17

class MyTestCase(unittest.TestCase):

    def test_puzzle1(self):
        self.assertEqual(45, day17.puzzle1("target area: x=20..30, y=-10..-5"))

    def test_puzzle2(self):
        self.assertEqual(112, day17.puzzle2("target area: x=20..30, y=-10..-5"))



if __name__ == '__main__':
    unittest.main()
