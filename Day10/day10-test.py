import unittest
import day10

class MyTestCase(unittest.TestCase):
    data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

    def test_puzzle1(self):
        self.assertEqual(0, day10.puzzle1(["()"]))
        self.assertEqual(25137, day10.puzzle1(["(>"]))
        self.assertEqual(1197, day10.puzzle1(["(}"]))
        self.assertEqual(0, day10.puzzle1(["(()"]))
        self.assertEqual(1197, day10.puzzle1(["((}"]))
        self.assertEqual(0, day10.puzzle1(["(())"]))
        self.assertEqual(0, day10.puzzle1(["(())"]))
        self.assertEqual(3, day10.puzzle1(["[[<[([]))<([[{}[[()]]]"]))
        self.assertEqual(26397, day10.puzzle1(self.data.splitlines()))

    def test_puzzle2(self):
        self.assertEqual("", day10.missing_chars(""))
        self.assertEqual(")", day10.missing_chars("("))
        self.assertEqual("]", day10.missing_chars("["))
        self.assertEqual("])", day10.missing_chars("(["))
        self.assertEqual(")", day10.missing_chars("([]"))
        self.assertEqual("", day10.missing_chars("{([(<{}[<>[]}>{[]{[(<()>"))
        self.assertEqual("}}]])})]", day10.missing_chars("[({(<(())[]>[[{[]{<()<>>"))
        self.assertEqual(294, day10.puzzle2(["<{([{{}}[<[[[<>{}]]]>[]]"]))
        self.assertEqual(288957, day10.puzzle2(self.data.splitlines()))


if __name__ == '__main__':
    unittest.main()
