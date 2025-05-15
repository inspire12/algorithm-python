'''
제목: 테트로미노
출처: https://www.acmicpc.net/problem/14500
idea: 
난이도: hard
'''
import unittest
import sys

max_sum = 0
def solution(N, M, paper):
    visited = [[False]*M for _ in range(N)]
    dx = [-1, 1, 0, 0]  # 상하좌우 이동
    dy = [0, 0, -1, 1]
    max_sum = 0

    def dfs(x, y, total, cnt):
        global max_sum
        if cnt == 4:
            max_sum = max(max_sum, total)
            return

        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, total + paper[nx][ny], cnt+1)
                visited[nx][ny] = False

    # 'ㅗ' 모양 예외 처리
    def check_special_shape(x, y):
        global max_sum
        shapes = [
            [(0,0),(-1,0),(1,0),(0,1)],
            [(0,0),(-1,0),(1,0),(0,-1)],
            [(0,0),(0,-1),(0,1),(1,0)],
            [(0,0),(0,-1),(0,1),(-1,0)],
        ]
        for shape in shapes:
            try:
                total = sum(paper[x+dx][y+dy] for dx,dy in shape)
                max_sum = max(max_sum, total)
            except:
                continue

    # 모든 칸에 대해서 시작점으로 탐색
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, paper[i][j], 1)
            visited[i][j] = False
            check_special_shape(i, j)

    return max_sum

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(solution(N, M ,paper))

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        N, M = 5, 5
        paper =[
        list(map(int, '1 2 3 4 5'.split())),
        list(map(int, '5 4 3 2 1'.split())),
        list(map(int, '2 3 4 5 6'.split())),
        list(map(int, '6 5 4 3 2'.split())),
        list(map(int, '1 2 1 2 1'.split()))
    ]
        expected = 19
        self.assertEqual(expected, solution(N,M,paper))

    def test_example_2(self):
        N, M = 4, 5
        paper =[
        list(map(int, '1 2 3 4 5'.split())),
        list(map(int, '1 2 3 4 5'.split())),
        list(map(int, '1 2 3 4 5'.split())),
        list(map(int, '1 2 3 4 5'.split())),
        list(map(int, '1 2 3 4 5'.split()))
    ]
        expected = 20
        self.assertEqual(expected, solution(N,M,paper))

    def test_example_3(self):
        N, M = 4, 10
        paper =[
        list(map(int, '1 2 1 2 1 2 1 2 1 2'.split())),
        list(map(int, '2 1 2 1 2 1 2 1 2 1'.split())),
        list(map(int, '1 2 1 2 1 2 1 2 1 2'.split())),
        list(map(int, '2 1 2 1 2 1 2 1 2 1'.split()))
         ]
        expected = 7
        self.assertEqual(expected, solution(N,M,paper))
