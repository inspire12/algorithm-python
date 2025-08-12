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
    min_length = 10 ** 19

    prefix_sums = [0] * (N + 1)
    for idx in range(N):
        prefix_sums[idx + 1] = prefix_sums[idx] + numbers[idx]

    start_idx = 0
    end_idx = 1
    while start_idx < N and end_idx <= N:
        current_sum = prefix_sums[end_idx] - prefix_sums[start_idx]
        if current_sum >= target_sum:
            current_idx = end_idx - start_idx
            min_length = min(min_length, current_idx)
            start_idx += 1
        else:
            end_idx += 1
    return min_length if min_length != 10**19 else 0


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
        N = 10000
        S = 100000000
        expected_output = 10000
        arr_line = [10000]  * N  # 10000을 10000번
        solution(S, arr_line)
        self.assertEqual(sys.stdout.getvalue(), expected_output)
