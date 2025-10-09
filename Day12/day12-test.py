import unittest
import day12

class MyTestCase(unittest.TestCase):
    data = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

    def test_puzzle1(self):
        simple_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
        self.assertEqual(1, day12.puzzle1(["start-end"]))
        self.assertEqual(2, day12.puzzle1(["start-end", "start-a", "a-end"]))
        self.assertEqual(10, day12.puzzle1(simple_input.splitlines()))

    def test_puzzle2(self):
        simple_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
        self.assertEqual(36, day12.puzzle2(simple_input.splitlines()))


if __name__ == '__main__':
    unittest.main()
