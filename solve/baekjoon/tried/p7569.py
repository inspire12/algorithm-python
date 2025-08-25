import sys
from collections import deque

directions = [[0, 1, 0],[0, -1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]

def main():
    M, N, H = map(int, sys.stdin.readline().split())
    tomatos = [ [] for _ in range(H)]

    step = 0
    rippen_tomatos = []
    for idx_level in range(H):
        for idx in range(N):
            tomatos[idx_level].append(list(map(int, sys.stdin.readline().split())))
            for i, r in enumerate(tomatos[idx_level][idx]):
                if r == 1:
                    rippen_tomatos.append([idx_level, idx, i, step])
    q = deque(rippen_tomatos)

    while q:
        rippen_tomato_location = q.popleft()
        step = max(step, rippen_tomato_location[3])
        for direction in directions:
            next_tomato, next_tomato_location = get_next_tomato(tomatos, rippen_tomato_location, direction, rippen_tomato_location[3])
            if next_tomato == 0:
                tomatos[next_tomato_location[0]][next_tomato_location[1]][next_tomato_location[2]] = 1
                q.append(next_tomato_location)

    result = is_all_rippen_tomatos(H, N, M, tomatos, step)
    print(result)


def is_all_rippen_tomatos(H, N, M, rippen_tomatos, step):
    for idx_level in range(H):
        for idx in range(N):
            for i in range(M):
                if rippen_tomatos[idx_level][idx][i] == 0:
                    return -1
    return step

def get_next_tomato(tomatos, rippen_tomato_location, direction, step):
    next_tomato_location = []
    for i, d in enumerate(direction):
        next_tomato_location.append(d + rippen_tomato_location[i])
    next_tomato_location.append(step + 1)
    tomato = safe_get(tomatos, next_tomato_location)
    return tomato, next_tomato_location


def safe_get(tomatos, next_tomato_location):
    if 0 <= next_tomato_location[0] < len(tomatos) and 0 <= next_tomato_location[1] < len(tomatos[0]) and 0 <= next_tomato_location[2] < len(tomatos[0][0]):
        return tomatos[next_tomato_location[0]][next_tomato_location[1]][next_tomato_location[2]]
    else:
        return -1

if __name__ == '__main__':
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim


class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
''')
        expected_output = dedent_trim('''-1''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
''')
        expected_output = dedent_trim('''4''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_3(self):
        test_input = dedent_trim('''4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
''')
        expected_output = dedent_trim('''0''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

