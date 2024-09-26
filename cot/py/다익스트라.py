import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def main():
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    r_graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        i, j, t = map(int, input().split())
        graph[i].append((j, t))
        r_graph[j].append((i, t))

    from_x = dijkstra(graph, x, n)
    to_x = dijkstra(r_graph, x, n)

    long_dis = 0
    for i in range(1, n + 1):
        a = from_x[i] + to_x[i]
        long_dis = max(a, long_dis)
    
    print(long_dis)

def dijkstra(graph, start, n):
    dis = [INF] * (n + 1)
    dis[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dis[now] < dist:
            continue
        for next, cost in graph[now]:
            if dist + cost < dis[next]:
                dis[next] = dist + cost
                heapq.heappush(q, (dist + cost, next))
    return dis
    
main()
