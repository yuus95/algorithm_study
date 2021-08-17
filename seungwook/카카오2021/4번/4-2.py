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
    
    
    for i in range(1, n+1): # 출발점 s일때 다익스트라를 모두 구하고 모든 정점에 대해서 합승 한뒤 a,b 목적지까지에 거리를 더했을때 가장 작은값을 구한다.
        distance_1 = dijkstra(s)
        distance_2 = dijkstra(i)
        answer = min(answer, distance_1[i] + distance_2[a] + distance_2[b])
    return answer