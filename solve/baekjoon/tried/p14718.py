# testutil_boj.py
import heapq
import io
import sys

# 적어도 K명의 병사를 이길 수 있게 하는 최소의 스탯 포인트
def main():
    N, K = map(int, sys.stdin.readline().split())

    enemies = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    powers = sorted([p for p, _, _ in enemies])
    quicks = sorted([q for _, q, _ in enemies])

    r = 10 ** 19
    for p in powers:
        if sum([i for i in powers if i <= p]) < K:
            continue
        for q in quicks:
            losed_enemies_ints = [c for a, b, c in enemies if a <= p and b <= q]
            if len(losed_enemies_ints) >= K:
                losed_enemies_ints.sort()
                r = min(r, p + q + losed_enemies_ints[K - 1])
    print(r)

if __name__ == '__main__':
    main()

import io
import unittest


from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):

        test_input = dedent_trim('''3 3
10 5 5
5 10 5
5 5 10
''')
        expected_output = dedent_trim('''30''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''3 1
234 23 342
35 4634 34
46334 6 789
''')
        expected_output = dedent_trim('''599''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2_1(self):
        test_input = dedent_trim('''3 1
234 23 342
35 500 34
46334 6 789
''')
        expected_output = dedent_trim('''569''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_3(self):
        test_input = dedent_trim('''3 2
30 30 30
10 500 10
50 10 50
''')
        expected_output = dedent_trim('''130''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
