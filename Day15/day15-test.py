import unittest
import day15

class MyTestCase(unittest.TestCase):

    def test_puzzle(self):
        sample_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
        self.assertEqual(40, day15.puzzle1(sample_input.splitlines()))
        self.assertEqual(315, day15.puzzle2(sample_input.splitlines()))



if __name__ == '__main__':
    unittest.main()
