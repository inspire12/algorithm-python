import sys
import unittest
from unittest import TestCase


def solution(n1, n2, ans, d) -> int:
    # n1
    return 0

def main():
    n1, n2, ans, d = map(int, sys.stdin.readline().split())
    answer = solution(n1, n2, ans, d)
    print(answer)

if __name__ == '__main__':
    main()

import io
class TestSolution(TestCase):
    def test_case1(self):
        test_input = '3 3 2 1'
        expected_output = '5'
        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)