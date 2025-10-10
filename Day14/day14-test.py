import unittest
import day14

class MyTestCase(unittest.TestCase):

    def test_puzzle1(self):
        sample_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
        self.assertEqual(1588, day14.puzzle1(sample_input.splitlines()))
        self.assertEqual(2188189693529, day14.puzzle2(sample_input.splitlines()))



if __name__ == '__main__':
    unittest.main()
