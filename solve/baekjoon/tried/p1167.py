import sys
from collections import deque
from unittest import TestCase
import io

def main():
    V = int(sys.stdin.readline())
    graph = [[] for _ in range(V + 1)]
    for _ in range(V):
        data = list(map(int, sys.stdin.readline().split()))
        u = data[0]
        i = 1
        while True:
            v = data[i]
            if v == -1:
                break
            w = data[i + 1]
            graph[u].append((v, w))
            graph[v].append((u, w))
            i += 2
    start_node = 1
    max_d, to_node = bfs(start_node, V, graph)
    max_d2, to_node2 = bfs(to_node, V, graph)
    print(max_d2)


def bfs(start_node, V, graph):
    visited = [False for _ in range(V + 1)]
    visited[start_node] = True
    dist = [0 for _ in range(V + 1)]
    max_node = 0
    queue = deque([start_node])
    while queue:
        current_node = queue.popleft()
        for next_node, next_weight in graph[current_node]:
            if visited[next_node]:
               continue
            visited[next_node] = True
            queue.append(next_node)
            dist[next_node] = dist[current_node] + next_weight
            if dist[next_node] > dist[max_node]:
                max_node = next_node
    return dist[max_node], max_node

if __name__ == '__main__':
    main()


class TestSolution(TestCase):
    def test_case1(self):
        test_input = '''
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
'''.strip()
        expected_output = '11\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

        # expected_value =
    def test_case2(self):
        test_input = '''
2
1 2 1 -1
2 1 1 -1
'''.strip()
        expected_output = '1\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

        # expected_value =


