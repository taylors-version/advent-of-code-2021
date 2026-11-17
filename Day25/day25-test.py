import unittest
import Day25.day25


class MyTestCase(unittest.TestCase):

    def test_puzzle1(self):
        sample_input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""
        self.assertEqual(58, Day25.day25.puzzle1(sample_input.splitlines()))


if __name__ == '__main__':
    unittest.main()
