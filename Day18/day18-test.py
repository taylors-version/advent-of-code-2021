import unittest
import Day18.day18
from Day18.day18 import SnailFish


class MyTestCase(unittest.TestCase):

    def test_snailfish_parse(self):
        sf = SnailFish.from_string("[9,1]")
        self.assertEqual(9, sf.a)
        self.assertEqual(1, sf.b)
        sf = SnailFish.from_string("[[9,1],1]")
        self.assertEqual(9, sf.a.a)
        self.assertEqual(1, sf.a.b)
        self.assertEqual(1, sf.b)
        sf = SnailFish.from_string("[[9,1],[1,9]]")
        self.assertEqual(9, sf.a.a)
        self.assertEqual(1, sf.a.b)
        self.assertEqual(1, sf.b.a)
        self.assertEqual(9, sf.b.b)
        sf = SnailFish.from_string("[[12,13],[14,15]]")
        self.assertEqual(12, sf.a.a)
        self.assertEqual(13, sf.a.b)
        self.assertEqual(14, sf.b.a)
        self.assertEqual(15, sf.b.b)

    def test_magnitude(self):
        self.assertEqual(29, SnailFish(9,1).magnitude())
        self.assertEqual(129, SnailFish(SnailFish(9,1), SnailFish(1,9)).magnitude())
        self.assertEqual(3488, SnailFish.from_string("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]").magnitude())

    def test_adding(self):
        a = SnailFish.from_string("[1,2]")
        b = SnailFish.from_string("[[3,4],5]")
        added = a.add(b)
        self.assertEqual("[[1,2],[[3,4],5]]", str(added))
        a = SnailFish.from_string("[[[[4,3],4],4],[7,[[8,4],9]]]")
        b = SnailFish.from_string("[1,1]")
        added = a.add(b)
        self.assertEqual("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", str(added))
        a = SnailFish.from_string("[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]")
        b = SnailFish.from_string("[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]")
        added = a.add(b)
        self.assertEqual("[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]", str(added))

    def many_adding(self):
        sf = SnailFish.from_string("[1,1]")
        sf = sf.add(SnailFish.from_string("[2,2]"))
        sf = sf.add(SnailFish.from_string("[3,3]"))
        sf = sf.add(SnailFish.from_string("[4,4]"))
        sf = sf.add(SnailFish.from_string("[5,5]"))
        sf = sf.add(SnailFish.from_string("[6,6]"))
        self.assertEqual("[[[[5,0],[7,4]],[5,5]],[6,6]]", str(sf))

        sf = SnailFish.from_string("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")
        sf = sf.add(SnailFish.from_string("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"))
        sf = sf.add(SnailFish.from_string("[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]"))
        sf = sf.add(SnailFish.from_string("[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]"))
        sf = sf.add(SnailFish.from_string("[7,[5,[[3,8],[1,4]]]]"))
        sf = sf.add(SnailFish.from_string("[[2,[2,2]],[8,[8,1]]]"))
        sf = sf.add(SnailFish.from_string("[2,9]"))
        sf = sf.add(SnailFish.from_string("[1,[[[9,3],9],[[9,0],[0,7]]]]"))
        sf = sf.add(SnailFish.from_string("[[[5,[7,4]],7],1]"))
        sf = sf.add(SnailFish.from_string("[[[[4,2],2],6],[8,7]]"))
        self.assertEqual("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", str(sf))

    def test_puzzle1(self):
        sample_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
        self.assertEqual(4140, Day18.day18.puzzle1(sample_input.splitlines()))

    def test_puzzle2(self):
        sample = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
        self.assertEqual(3993, Day18.day18.puzzle2(sample.splitlines()))

if __name__ == '__main__':
    unittest.main()
