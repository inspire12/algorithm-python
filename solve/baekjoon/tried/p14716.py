import sys
from collections import deque
from unittest import TestCase


def main():
    M, N = map(int, sys.stdin.readline().split())
    band_map = []
    for _ in range(M):
        band_map.append(list(map(int, sys.stdin.readline().split())))
    c = 0
    for y in range(M):
        for x in range(N):
            if band_map[y][x] == 1:
                c += bfs(band_map, x, y)
    print(c)


direct_x = [1, -1, 0, 0, 1, 1, -1, -1]
direct_y = [0, 0, 1, -1, 1, -1, -1, 1]


def bfs(band_map, x, y):
    q = deque([(x, y)])
    while q:
        current_x, current_y = q.popleft()
        for x, y in zip(direct_x, direct_y):
            next_x = current_x + x
            next_y = current_y + y
            if (0 <= next_x < len(band_map[0])) and (0 <= next_y < len(band_map)):
                if band_map[next_y][next_x] == 1:
                    band_map[next_y][next_x] = 0
                    q.append((next_x, next_y))
    return 1


if __name__ == '__main__':
    main()

import io


class TestSoultion(TestCase):
    def test_case1(self):
        test_input = '''8 19
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 0
0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 1 1 1 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 1 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'''
        expected_output = '3\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
