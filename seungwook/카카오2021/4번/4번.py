import heapq
import sys

def dijkstra(start, graph, n):
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

def solution(n, s, a, b, fares):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for i in range(len(fares)):
        graph[fares[i][0]].append((fares[i][2], fares[i][1]))
        graph[fares[i][1]].append((fares[i][2], fares[i][0]))
    #print(graph)
    #fares.sort(key = lambda x : x[2])
    distance_a = dijkstra(s, graph, n)
    dij_a = distance_a[a]
    distance_b = dijkstra(a, graph, n)
    dij_b = min(distance_a[b], distance_b[b])
    
    return dij_a + dij_b