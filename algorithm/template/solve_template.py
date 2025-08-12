'''
    제목:
    출처:
    idea:
    난이도: [Easy | Medium | Hard | Expert]
'''

import sys
import unittest

def input_template():
    a, b, c = map(int, sys.stdin.readline().split())
    pass

def solve(a: str):
    return a


if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().split())
    m = solve(a)
    print(m)

import unittest
class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        input = 'edeaaabbccd'
        answer = 'de'
        self.assertEqual(solve(input), answer)