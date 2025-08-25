import sys

def calc(a, b, o1) -> int:
    if o1 == '+':
        return a + b
    elif o1 == '-':
        return a - b
    elif o1 == '*':
        return int(a * b)
    elif o1 == '/':
        return int(a / b)
    return None

def main():
    # raw = list(sys.stdin.readline().split(" "))
    a, o1, b, o2, c = sys.stdin.readline().split(" ")
    a1 = int(a)
    b1 = int(b)
    c1 = int(c)

    r1 = calc(calc(a1,b1,o1), c1, o2)
    r2 = calc(a1, calc(b1, c1, o2), o1)
    if r1 < r2:
        print(f'{r1}\n{r2}')
    else:
        print(f'{r2}\n{r1}')

if __name__ == '__main__':
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''2 + 3 * 4''')
        expected_output = dedent_trim('''14
20
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''6 / 2 * 3''')
        expected_output = dedent_trim('''1
9
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)