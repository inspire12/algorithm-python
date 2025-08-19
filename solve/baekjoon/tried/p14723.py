import sys

def count_square(loop):
    return int(loop * (loop - 1) / 2) + 1

def main():
    N = int(sys.stdin.readline())
    loop = 2
    K = count_square(loop)
    while K <= N:
        loop+=1
        K = count_square(loop)
    loop -= 1
    a = loop
    K = count_square(loop)
    for _ in range(K, N):
        a -= 1

    print(f"{a} {loop - a + 1}")

if __name__ == '__main__':
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''1
''')
        expected_output = dedent_trim('''1 1
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''2
''')
        expected_output = dedent_trim('''2 1
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_3(self):
        test_input = dedent_trim('''5
''')
        expected_output = dedent_trim('''2 2
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
    def test_4(self):
        test_input = dedent_trim('''13
''')
        expected_output = dedent_trim('''3 3
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)