import sys
def main():
    N = int(sys.stdin.readline())
    paper_map = []
    for i in range(N):
        paper_map.append(list(map(int, sys.stdin.readline().split(" "))))
    print(sum([sum(a) for a in paper_map]))


if __name__ == '__main__':
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''4
2 6 5 4
1 5 7 6
9 8 8 7
1 4 7 8
''')
        expected_output = dedent_trim('''88''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
