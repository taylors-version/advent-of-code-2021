import unittest
import Day23.day23


class MyTestCase(unittest.TestCase):

    def test_puzzle1(self):
        sample_input = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""
        self.assertEqual(12521, Day23.day23.puzzle1(sample_input.splitlines()))
        end_input = """#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########"""
        self.assertEqual(2003+7000+8, Day23.day23.puzzle1(end_input.splitlines()))
        end_input_2 = """#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########"""
        self.assertEqual(7000+8, Day23.day23.puzzle1(end_input_2.splitlines()))

    def test_puzzle2(self):
        sample_input = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""
        self.assertEqual(44169, Day23.day23.puzzle2(sample_input.splitlines()))

if __name__ == '__main__':
    unittest.main()
