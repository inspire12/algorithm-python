import sys
def main():
    while True:
        line = sys.stdin.readline().strip()
        if line == '0':
            break
        histograms = list(map(int, line.split()))
        n = histograms[0]
        print(solve(histograms[1:]))


def solve(heights):
    stack = []  # 인덱스 저장 (높이는 heights[idx]로 참조)
    max_area = 0
    # 끝에 높이 0을 붙여 남은 막대 처리
    for i, h in enumerate(heights + [0]):
        # 단조 증가가 깨질 때까지 pop 하며 넓이 계산
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            height = heights[top]
            # 왼쪽 경계: 스택이 비면 0, 아니면 스택 top + 1
            left = stack[-1] + 1 if stack else 0
            right = i  # 현재 i가 처음으로 height보다 작은 위치
            width = right - left
            area = height * width
            if area > max_area:
                max_area = area
        stack.append(i)
    return max_area


if __name__ == '__main__':
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
''')
        expected_output = dedent_trim('''8
4000
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''2 1 5 6 2 3
2 4 5 3 1
0
''')
        expected_output = dedent_trim('''10
9''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_3(self):
        test_input = dedent_trim('''1 2 3 4
0
''')
        expected_output = dedent_trim('''6''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
