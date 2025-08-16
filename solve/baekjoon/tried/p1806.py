import sys
import unittest


# 부분합
# 합이 S 이상 중 길이가 가장 짧은 것
# 완전 탐색 형태 -> 최적화 -> 투포인터 형태
def main():
    N, S = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))

    result = solution(S, numbers)
    print(result)


def solution(target_sum, numbers) -> int:
    N = len(numbers)
    prefix_sum = [0] * (N + 1)
    prefix_sum[0] = numbers[0]
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + numbers[i]

    start_idx = 0
    end_idx = 1

    current_sum = 0
    min_length = 10**18
    #  이분 탐색
    while start_idx < N and end_idx <= N:
        current_sum = prefix_sum[end_idx] - prefix_sum[start_idx]
        if current_sum >= target_sum:
            min_length = min(end_idx - start_idx, min_length)
            start_idx+=1
        else:
            end_idx+=1
    return min_length if min_length != 10**18 else 0

if __name__ ==  '__main__':
    main()

import io
from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''
10 15
5 1 3 5 10 7 4 9 2 8
        ''')
        expected_output = '2\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''
5 10
2 10 1 1 1
        ''')
        expected_output = '1\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_3(self):
        test_input = dedent_trim('''
3 100
20 30 40
        ''')
        expected_output = '0\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_4(self):
        test_input = dedent_trim('''
8 15
2 2 2 2 2 2 2 2
        ''')
        expected_output = '8\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)