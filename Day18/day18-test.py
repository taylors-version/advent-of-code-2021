import unittest
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
        a = SnailFish.from_string("[[3,[2,[1,[17,13]]]]")
        b = SnailFish.from_string("[6,[5,[4,3]]]")
        added = a.add(b) #[[3,[2,[1,[17,13]]]],[6,[5,[4,3]]]]
        #self.assertEqual("[[3,[2,[18,0]]],[19,[5,[4,3]]]]", str(added))

if __name__ == '__main__':
    unittest.main()
