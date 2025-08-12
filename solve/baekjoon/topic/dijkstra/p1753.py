# https://www.acmicpc.net/problem/1753
import sys
import heapq


def main(V, graph, K):
    INF = 10 ** 18
    dist = [INF] * (V + 1)  # 최소
    dist[K] = 0
    pq = [(0, K)]
    heappush = heapq.heappush
    heappop = heapq.heappop
    while pq:
        current_dist, current_node = heappop(pq)
        # 여러번 들어가는 것 방지
        if dist[current_node] < current_dist:
            continue

        for next_node, next_dist in graph[current_node]:
            if dist[next_node] > current_dist + next_dist:
                dist[next_node] = current_dist + next_dist
                heappush(pq, (dist[next_node], next_node))
    out = []
    for i in range(1, V + 1):
        if dist[i] == INF:
            out.append("INF")
        else:
            out.append(str(dist[i]))
    print("\n".join(out))


if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())  # start
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
    main(V, graph, K)
