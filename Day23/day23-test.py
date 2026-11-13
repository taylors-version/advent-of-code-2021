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



if __name__ == '__main__':
    unittest.main()
