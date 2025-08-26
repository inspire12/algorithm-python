import sys
from collections import deque
direction = [(1,0), (0,1)]
milk_types = [0, 1, 2]

def next_milk_type(milk_type):
    return (milk_type + 1) % len(milk_types)

def main():
    milk_city = []
    N = int(input())
    drink_count = [[[0,0,0] for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        milk_city.append(list(map(int, sys.stdin.readline().split())))

    start_x, start_y = 0, 0
    # 시작 칸 초기화
    if milk_city[start_x][start_y] == 0:
        drink_count[start_x][start_y][1] = 1
    else:
        drink_count[start_x][start_y][0] = 0

    p = deque([(start_x, start_y)])
    a = 0
    max_k = 0

    for x_idx in range(N):
        for y_idx in range(N):
            if x_idx == start_x and y_idx == start_y:
                # 시작칸은 이미 초기화됨
                pass
            else:
                # 위/왼쪽에서 상태별 최댓값을 당겨오기
                for k in milk_types:
                    if x_idx > 0 and drink_count[x_idx-1][y_idx][k] > drink_count[x_idx][y_idx][k]:
                        drink_count[x_idx][y_idx][k] = drink_count[x_idx-1][y_idx][k]
                    if y_idx > 0 and drink_count[x_idx][y_idx-1][k] > drink_count[x_idx][y_idx][k]:
                        drink_count[x_idx][y_idx][k] = drink_count[x_idx][y_idx-1][k]

            # 현재 칸에서 마실 수 있으면
            t = milk_city[x_idx][y_idx]
            take = drink_count[x_idx][y_idx][t] + 1
            nxt = next_milk_type(t)
            if take > drink_count[x_idx][y_idx][nxt]:
                drink_count[x_idx][y_idx][nxt] = take

    max_k = max(drink_count[N-1][N-1])
    print(max_k)

if __name__ == "__main__":
    main()



import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''4
0 1 2 2
1 1 1 1
2 2 2 2
0 0 1 0
        ''')
        expected_output = dedent_trim('''5''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''5
0 1 0 0 0
1 2 1 1 1
2 0 1 2 0
0 0 0 0 1
1 1 1 1 2
        ''')
        expected_output = dedent_trim('''9''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
