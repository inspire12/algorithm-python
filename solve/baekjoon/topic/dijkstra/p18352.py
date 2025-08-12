import sys
import heapq

def dijkstra(graph, start, N):
    dist = [float('inf')] * (n+1)

    dist[start] = 0
    pq = [(0, start)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > dist[current_node]:
            continue
        for next_node in graph[current_node]:
            if dist[next_node] > current_dist + 1:
                dist[next_node] = current_dist + 1
                heapq.heappush(pq, (dist[next_node], next_node))
    return dist
    

# 최단거리가 X 서 출발 k 인 모든 도시들의 번호를 출력 (개수 x)
# 각 노드마다 모두 최단거리를 계산 -> 다익스트라
if __name__ == '__main__':
    n, m, k, x = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)] # [source, next]
    for i in range(m):
        u, v = list(map(int, sys.stdin.readline().split()))
        graph[u].append(v)

    dist = dijkstra(graph, x, n)
    answer = []
    for i in range(1, n+1):
        if dist[i] == k:
            answer.append(i)
    if answer:
        print(*answer, sep='\n', end='')
    else:
        print(-1)


