import sys
import unittest



def input_template():
    a, b, c = map(int, sys.stdin.readline().split())


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        input = 'edeaaabbccd'
        answer = 'de'
        self.assertEqual(input, answer)