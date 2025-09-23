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
        self.assertEqual(0, day10.line_check("()"))
        self.assertEqual(25137, day10.line_check("(>"))
        self.assertEqual(1197, day10.line_check("(}"))
        self.assertEqual(0, day10.line_check("(()"))
        self.assertEqual(1197, day10.line_check("((}"))
        self.assertEqual(0, day10.line_check("(())"))
        self.assertEqual(0, day10.line_check("(())"))
        self.assertEqual(3, day10.line_check("[[<[([]))<([[{}[[()]]]"))
        self.assertEqual(26397, day10.puzzle1(self.data.splitlines()))


if __name__ == '__main__':
    unittest.main()
