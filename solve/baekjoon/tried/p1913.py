import io
import sys

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_in_smail_map(x, y, N):
    return (0 <= x < N) and (0 <= y < N)

def next_direction(d_index):
    return (d_index + 1) % len(direction)

def main():
    target_cur = ()
    N = int(sys.stdin.readline())
    target_count = int(sys.stdin.readline())
    snail = [['0' for _ in range(N)] for _ in range(N)]
    current_x = int((N / 2))
    current_y = int((N / 2))
    if target_count == 1:
        target_cur = (current_y + 1, current_x + 1)

    d_index = 0  # now_direction = direction[d_index]]
    snail[current_y][current_x] = str(1)
    for prev_idx in range(2, 5):
        current_x = current_x + direction[d_index][0]
        current_y = current_y + direction[d_index][1]
        snail[current_y][current_x] = str(prev_idx)
        d_index = next_direction(d_index)
        if prev_idx == target_count:
            target_cur = N - current_y, current_x + 1
    d_index = 2

    for idx in range(5, N * N + 1):
        current_direct = direction[d_index]
        right_direct = direction[next_direction(d_index)]

        right_x = current_x + right_direct[0]
        right_y = current_y + right_direct[1]

        if snail[right_y][right_x] == '0':
            d_index = next_direction(d_index)
            current_x = right_x
            current_y = right_y
        else:
            current_x = current_x + current_direct[0]
            current_y = current_y + current_direct[1]
        snail[current_y][current_x] = str(idx)
        if idx == target_count:
            target_cur = N - current_y, current_x + 1

    for s in reversed(snail):
        print(' '.join(s))
    print(target_cur[0], target_cur[1])

if __name__ == '__main__':
    main()

from unittest import TestCase


class TestSolution(TestCase):
    def test_case0(self):
        test_input = '''5
    6'''
        expected_output = '''25 10 11 12 13
24 9 2 3 14
23 8 1 4 15
22 7 6 5 16
21 20 19 18 17
4 3
'''
        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(expected_output, sys.stdout.getvalue())

    def test_case1(self):
        test_input = '''7
35'''
        expected_output = '''49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24 9 2 3 14 33
46 23 8 1 4 15 34
45 22 7 6 5 16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37
5 7
'''

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(expected_output, sys.stdout.getvalue())

    def test_case2(self):
        test_input = '''7
        1'''
        expected_output = '''49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24 9 2 3 14 33
46 23 8 1 4 15 34
45 22 7 6 5 16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37
3 3
'''
        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(expected_output, sys.stdout.getvalue())

    def test_case3(self):
        test_input = '''7
        2'''
        expected_output = '''49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24 9 2 3 14 33
46 23 8 1 4 15 34
45 22 7 6 5 16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37
3 2
'''
        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(expected_output, sys.stdout.getvalue())