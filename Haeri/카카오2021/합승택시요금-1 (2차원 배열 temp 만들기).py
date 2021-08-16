# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:33:58 2021

@author: 82103
"""
# 풀이 (1) : distance는 1차원 배열로 매번 초기화 하고, 
# temp에 2차원 배열을 만들어 그 결과값을 받아주기

import heapq

def solution(n, s, a, b, fares):
    
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]

    
    for i in range(len(fares)):
        x, y, z = fares[i][0], fares[i][1], fares[i][2]
        graph[x].append((y, z))
        graph[y].append((x, z))
        
    def dij(s): # 출발 노드에서 다른 모든 지점까지의 최솟값 찾기
        q = []
        distance = [INF] * (n+1)
        distance[s] = 0
        heapq.heappush(q, (0, s))        
        
        while q :
            dist, now = heapq.heappop(q) 
            
            if distance[now] < dist : # 이미 처리된 노드 무시
                continue
            
            for i in graph[now] : # i[0]:노드, i[1]:비용  
                cost = dist + i[1] # i[0] 까지 도달 비용
                
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
        return distance
    temp = [[]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        new_cost = dij(i)
        temp[i] = new_cost
        
    result = INF
    for i in range(1,n+1):
         result = min(result, temp[s][i]+temp[i][a]+temp[i][b])

    return result

print(solution(7, 3, 4, 1, [[5,7,9], [4,6,4], [3,6,1], [3,2,3], [2,1,6]]))