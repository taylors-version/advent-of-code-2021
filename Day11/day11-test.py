import unittest
import day11
from day11 import Point

class MyTestCase(unittest.TestCase):
    data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

    def test_puzzle1(self):
        self.assertEqual(1656, day11.puzzle1(self.data.splitlines()))

    def test_puzzle2(self):
        self.assertEqual(195, day11.puzzle2(self.data.splitlines()))


    def test_neighbours(self):
        expected_easy = {Point(0, 0), Point(1, 0), Point(2, 0), Point(0, 1), Point(2, 1), Point(0, 2), Point(1, 2), Point(2, 2)}
        self.assertEqual(expected_easy, day11.neighbours(Point(1,1)))
        expected_top_left = {Point(1, 0), Point(1, 1), Point(0, 1)}
        self.assertEqual(expected_top_left, day11.neighbours(Point(0,0)))
        expected_bottom_left = {Point(0,8), Point(1,8), Point(1,9)}
        self.assertEqual(expected_bottom_left, day11.neighbours(Point(0,9)))


if __name__ == '__main__':
    unittest.main()
