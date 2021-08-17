import heapq
import sys


def solution(n, s, a, b, fares):
    answer = sys.maxsize
    
    def dijkstra(start):
        INF = sys.maxsize
        distance = [INF for _ in range(n+1)]
        distance[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            wei, now = heapq.heappop(heap)
            if distance[now] < wei:
                continue
            for w, next_node in graph[now]:
                next_wei = w + wei
                if next_wei < distance[next_node]:
                    distance[next_node] = next_wei
                    heapq.heappush(heap, (next_wei, next_node))
        return distance
    
    graph = [[] for _ in range(n+1)]
    for i in range(len(fares)):
        graph[fares[i][0]].append((fares[i][2], fares[i][1]))
        graph[fares[i][1]].append((fares[i][2], fares[i][0]))
    
    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    
    for i in range(1, n+1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)
    
    return answer