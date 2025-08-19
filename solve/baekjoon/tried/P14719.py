import sys


def main():
    H, W = map(int, sys.stdin.readline().split())

    blocks_input = list(map(int, sys.stdin.readline().split()))
    blocks = [[] for _ in range(W)]
    for idx, block in enumerate(blocks_input):
        blocks[idx].extend([1 for _ in range(block)])
        blocks[idx].extend([0 for _ in range(H - block)])
    state = 0  #
    water = 0
    for hindx in range(H):
        row_water = 0
        row_tmp = 0
        state = 0
        for windx in range(W):
            cur_block = blocks[windx][hindx]
            if cur_block == 1:  # 벽
                if state == 1:  # 이전에 벽이 있었을 경우
                    row_water += row_tmp
                    row_tmp = 0
                state = 1
            else:
                if state == 1:
                    row_tmp += 1

        water += row_water
    print(water)
    return water

if __name__ == '__main__':
    main()

import io
import unittest

from solve.baekjoon.testutil_boj import dedent_trim


class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''4 4
3 0 1 4
''')
        expected_output = dedent_trim('''5''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''4 8
3 1 2 3 4 1 1 2
''')
        expected_output = dedent_trim('''5''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

