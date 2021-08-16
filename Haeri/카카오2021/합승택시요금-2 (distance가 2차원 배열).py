# 풀이 (2) : distance 배열을 2차원으로 만들기
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:05:45 2021

@author: 82103
"""

import heapq

def solution(n, s, a, b, fares):
    
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(len(fares)):
        x, y, z = fares[i][0], fares[i][1], fares[i][2]
        graph[x].append((y, z))
        graph[y].append((x, z))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    def dij(s): # 출발 노드에서 다른 모든 지점까지의 최솟값 찾기
        q = []
        
        distance[s][s] = 0
        heapq.heappush(q, (0, s))        
        
        while q :
            dist, now = heapq.heappop(q) 
            
            if distance[s][now] < dist : # 이미 처리된 노드 무시
                continue
            
            for i in graph[now] : # i[0]:노드, i[1]:비용  
                cost = dist + i[1] # i[0] 까지 도달 비용
                
                if cost < distance[s][i[0]]:
                    distance[s][i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
        return distance

    for i in range(1, n+1):
        distance = dij(i)
        
    result = INF
    
    for i in range(1,n+1):
         result = min(result, distance[s][i]+distance[i][a]+distance[i][b])

    return result

print(solution(7, 3, 4, 1, [[5,7,9], [4,6,4], [3,6,1], [3,2,3], [2,1,6]]))