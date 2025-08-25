import sys
from collections import deque
import sys
from collections import deque
from collections import deque

def main():
    # 입력 처리
    N, M, K = input().split()
    N, M = int(N), int(M)
    K = float(K)

    grid = [list(input().strip()) for _ in range(2 * M + 1)]

    # 실제 격자 좌표 (M행 N열)
    cell = [[''] * N for _ in range(M)]

    for row in range(M):
        for col in range(N):
            char = grid[2 * row + 1][2 * col + 1]
            cell[row][col] = char  # 'B' 또는 'O'

    # 블록 연결 관계 만들기
    block_id = [[-1] * N for _ in range(M)]
    block_counter = 0

    for row in range(M):
        for col in range(N):
            if cell[row][col] == 'B' and block_id[row][col] == -1:
                block_counter += 1
                q = deque([(row, col)])
                block_id[row][col] = block_counter

                while q:
                    r, c = q.popleft()
                    # 4방향 탐색
                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < M and 0 <= nc < N:
                            if cell[nr][nc] == 'B' and block_id[nr][nc] == -1:
                                # grid 상에서 . 로 연결되어 있어야 함
                                if dr == 0:  # 좌우
                                    wall = grid[2*r+1][2*min(c,nc)+2]
                                else:  # 상하
                                    wall = grid[2*min(r,nr)+2][2*c+1]
                                if wall == '.':
                                    block_id[nr][nc] = block_counter
                                    q.append((nr,nc))

    # 공 경로 시뮬레이션
    x = K
    y = 0.0
    dx, dy = -1, 1   # 왼쪽 위 (↖) 방향

    destroyed_blocks = set()

    while True:
        x += dx * 0.5
        y += dy * 0.5

        # 벽 충돌 체크
        if x <= 0 or x >= N:
            dx *= -1
            x = max(0, min(N, x))
        if y >= M:
            dy *= -1
            y = M
        if y <= 0:  # 다시 바닥 도착
            break

        # 현재 위치에 블록이 있으면 파괴 처리
        cx, cy = int(x), int(y)
        if 0 <= cx < N and 0 <= cy < M:
            if cell[cy][cx] == 'B':
                destroyed_blocks.add(block_id[cy][cx])

    print(len(destroyed_blocks))

if __name__ == "__main__":
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim


class TestSolution(unittest.TestCase):

    def test_1(self):
        test_input = dedent_trim('''9 4 2
+-+-+-+-+-+-+-+-+-+
|B.B|O|B|O|B.B.B|B|
+-+.+-+-+-+-+-+-+-+
|O|B.B|O|B.B|O|B.B|
+-+-+-+-+-+.+-+-+-+
|B|O|B.B.B|B|B.B.B|
+-+-+-+-+-+-+-+-+-+
|O|O|O|O|O|O|O|O|O|
+-+-+-+-+-+-+-+-+-+
''')
        expected_output = dedent_trim('''3''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''3 3 2.5
+-+-+-+
|O|B.B|
+-+-+-+
|B|O|O|
+-+-+-+
|B|B.B|
+-+-+-+
''')
        expected_output = dedent_trim('''3
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_3(self):
        test_input = dedent_trim('''3 2 1
+-+-+-+
|B|O|O|
+-+-+-+
|O|O|O|
+-+-+-+
''')
        expected_output = dedent_trim('''1
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
