import sys
from collections import deque


def solution_self_dfs(N, graph, V):
    dfs_answer = []
    visited = [False] * (N + 1)
    dfs(V, graph, visited, dfs_answer)
    return dfs_answer

def dfs(current, graph, visited, dfs_answer):
    visited[current] = True
    dfs_answer.append(current)
    for v in graph[current]:
        if not visited[v]:
            dfs(v, graph, visited, dfs_answer)

def solution_dfs(N, graph, V):
    answer = []
    visited = [False] * (N+1)
    stack = deque([V])

    while stack:
        current = stack.pop()
        if visited[current]:
            continue
        visited[current] = True
        answer.append(current)
        for v in reversed(graph[current]):
            if not visited[v]:
                stack.append(v)

    return answer

def solution_bfs(N, graph, V):
    answer = []
    q = [V]
    seen = [False] * (N+1)
    seen[V] = True
    front = 0
    while front < len(seen) - 1 :
        if front >= len(q):
            break
        current = q[front]
        front += 1
        answer.append(current)
        graph[current].sort()
        for v in graph[current]:
            if seen[v]:
                continue
            q.append(v)
            seen[v] = True
    return answer


if __name__ == '__main__':
    N, M, V = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        source, target = map(int, sys.stdin.readline().split())
        graph[source].append(target)
        graph[target].append(source)

    for adj in graph:
        adj.sort()

    dfs = solution_self_dfs(N, graph, V)
    print(*dfs, sep=' ')
    bfs = solution_bfs(N, graph, V)
    print(*bfs, sep=' ')
