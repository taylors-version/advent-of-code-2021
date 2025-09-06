import unittest
import day07

class MyTestCase(unittest.TestCase):
    data = "16,1,2,0,4,2,7,1,2,14"
    def test_puzzle1(self):
        self.assertEqual(37, day07.puzzle1(self.data))

    def test_puzzle2(self):
        self.assertEqual(168, day07.puzzle2(self.data))



if __name__ == '__main__':
    unittest.main()
