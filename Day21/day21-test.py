import unittest
import Day21.day21


class MyTestCase(unittest.TestCase):

    def test_puzzle1(self):
        sample_input = """Player 1 starting position: 4
Player 2 starting position: 8
"""
        self.assertEqual(739785, Day21.day21.puzzle1(sample_input.splitlines()))
        self.assertEqual(444356092776315, Day21.day21.puzzle2(sample_input.splitlines()))


if __name__ == '__main__':
    unittest.main()
