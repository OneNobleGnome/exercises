from ex_5_13 import find_falling_distance
import unittest

class TestFallingDistance(unittest.TestCase):
    
    def test_one_second(self):
        expected = 4.9
        actual = find_falling_distance(1)
        self.assertEqual(expected, actual)
        print(find_falling_distance(1))

    def test_zero_seconds(self):
        expected = 0
        actual = find_falling_distance(0)
        self.assertEqual(expected, actual)
        print(find_falling_distance(0))



unittest.main()


