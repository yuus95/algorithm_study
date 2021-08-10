import sys

def floyd(distance, n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance
    
def solution(n, s, a, b, fares):
    INF = sys.maxsize
    answer = INF
    distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
    
    for edge in fares:
        distance[edge[0]][edge[1]] = edge[2]
        distance[edge[1]][edge[0]] = edge[2]
    
    for i in range(1, n+1):
        distance[i][i] = 0
    
    distance = floyd(distance, n)
    
    for k in range(1, n+1): # 합승지점 k 까지 간후 a,b 목적지 갈때 제일 작은값
        answer = min(answer, distance[s][k] + distance[k][a] + distance[k][b])
    
    return answer