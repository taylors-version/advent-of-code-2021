import unittest
import day13

class MyTestCase(unittest.TestCase):
    sample_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    def test_puzzle1(self):

        self.assertEqual(2, day13.puzzle1(["0,1","2,0", "", "fold along x=1"]))
        self.assertEqual(17, day13.puzzle1(self.sample_input.splitlines()))



if __name__ == '__main__':
    unittest.main()
