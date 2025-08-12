import heapq



# 다익스트라(Dijkstra) 알고리즘 설명:
# - 음수 가중치가 없는 그래프에서
#   한 시작점으로부터 모든 노드까지의 최단 거리 계산
# - 우선순위 큐(heapq)로 구현하면 O(E log V)
# 각 점에선 지금까지 검색한 곳에서 최소 접근이 저장된다

# graph: 전체 그래프
# source: 출발점
def dijkstra(graph, source, N):
    dist = [float('inf')] * (N + 1) # dist는 지점
    dist[source] = 0

    pq = [(0, source)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > dist[current_node]:
            continue
        for next_node, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[next_node]:
                dist[next_node] = distance
                heapq.heappush(pq, (distance, next_node))
    return dist

def bfs():
    return


def network_delay_time(times, N, K):
    # times: list of [u, v, w] edges
    # Build adjacency list graph where graph[u] = list of (v, w)
    graph = [[] for _ in range(N + 1)]
    for u, v, w in times:
        graph[u].append((v, w))

    dist = dijkstra(graph, K, N)
    max_dist = max(dist[1:])
    return max_dist if max_dist != float('inf') else -1

if __name__ == '__main__':
    #
    times = [[2,1,1], [2,3,1], [3,4,1]]
    N = 4
    K = 2
    result = network_delay_time(times, N, K)
    print(result)
    #
