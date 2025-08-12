import sys
from collections import deque

def solution_dfs(N, graph, V) -> list:
    # stack
    # 탐색과 동시에 방문
    stack = []
    visited = [False] * (1000 + 1)

    stack.append(V)
    order = []
    while stack:
        current_node = stack.pop()
        if visited[current_node] == True:
            continue
        visited[current_node] = True
        order.append(current_node)
        # print(current_node, result, visited)
        adj = graph[current_node]
        for next_node in reversed(adj):
            if not visited[next_node]:
                stack.append(next_node)
    return order

def solution_dfs_push_visit(N, graph, V) -> list:
    # stack
    # 탐색과 동시에 방문
    stack = []
    visited = [False] * (N + 1)

    stack.append(V)
    visited[V] = True
    result = []
    while stack:
        current_node = stack.pop()
        result.append(current_node)
        # print(current_node, result, visited)
        adj = graph[current_node]
        for next_node in reversed(adj):
            if not visited[next_node]:
                stack.append(next_node)
                visited[next_node] = True
    return result


def solution_bfs(N, graph, V) -> list:
    order = []
    seen = [False] * (1000 + 1)
    q = deque([V])
    seen[V] = True
    while q:
        current_node = q.popleft()
        order.append(current_node)
        for next_node in graph[current_node]:
            if seen[next_node]:
                continue
            seen[next_node] = True
            q.append(next_node)
    return order


def main():
    N, M, V = map(int, sys.stdin.readline().split())
    # graph = [[]] * 10
    graph  = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for adj in graph:
        adj.sort()

    dfs_result = solution_dfs(N, graph, V)
    print(*dfs_result, sep=' ')

    bfs_result = solution_bfs(N, graph, V)
    print(*bfs_result, sep=' ')

if __name__ == '__main__':
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim

class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''
            4 5 1
            1 2
            1 3
            1 4
            2 4
            3 4
        ''')
        expected_output = dedent_trim('''
            1 2 4 3
            1 2 3 4
        ''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''
            5 5 3
5 4
5 2
1 2
3 4
3 1
        ''')
        expected_output = dedent_trim('''
            3 1 2 5 4
            3 1 4 2 5
        ''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)