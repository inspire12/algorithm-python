import sys


def main():
    N = int(input())
    data_set = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        data_set.append((x , y))
    best_a = 1
    best_b = 1
    best_rss = 10**19
    rss = 0
    for a in range(1, 101):
        for b in range(1, 101):
            for x, y in data_set:
                f = a * x + b
                rss += (y - f) ** 2
                if rss >= best_rss:
                    break
            if rss < best_rss:
                best_rss = rss
                best_a = a
                best_b = b
            rss = 0
    print(best_a, best_b)
    return best_a, best_b, best_rss

if __name__ == '__main__':
    main()


import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''4
1 2
2 3
3 4
4 5
        ''')
        expected_output = dedent_trim('''1 1''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''5
1 5
2 7
3 9
4 11
5 13
        ''')
        expected_output = dedent_trim('''2 3''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_3(self):
        test_input = dedent_trim('''4
10 105
20 205
30 305
40 405
        ''')
        expected_output = dedent_trim('''10 5''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
