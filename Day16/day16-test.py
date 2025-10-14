import unittest
import day16

class MyTestCase(unittest.TestCase):

    def test_puzzle(self):
        self.assertEqual(6, day16.puzzle1("D2FE28"))
        self.assertEqual(9, day16.puzzle1("38006F45291200"))
        self.assertEqual(14, day16.puzzle1("EE00D40C823060"))
        self.assertEqual(16, day16.puzzle1("8A004A801A8002F478"))
        self.assertEqual(12, day16.puzzle1("620080001611562C8802118E34"))
        self.assertEqual(23, day16.puzzle1("C0015000016115A2E0802F182340"))
        self.assertEqual(31, day16.puzzle1("A0016C880162017C3686B18A3D4780"))



if __name__ == '__main__':
    unittest.main()
