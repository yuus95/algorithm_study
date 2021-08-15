import  heapq

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for i in range(len(fares)):
        graph[fares[i][0]].append((fares[i][2],fares[i][1]))
        graph[fares[i][1]].append((fares[i][2],fares[i][0]))

    def dijkstra(graph,start):
        distance = [2147000] * (n+1)
        q = []
        distance[start] =0
        heapq.heappush(q,(0,start))


        while q:
            value , destination  = heapq.heappop(q)

            if distance[destination] < value:
                continue

            for v,e in graph[destination]:
                next_value = value+v
                if next_value < distance[e]:
                    distance[e] = next_value
                    heapq.heappush(q,(next_value,e))


        return distance


    # 모든 지점마다 최소거리 구하기
    temp = [[] for _ in range(n+1)]
    for k in range(1,n+1):
        temp[k] = dijkstra(graph,k)
    result = 21470000
    
    # 시작점부터 다른 하나의지점까지 거리 + 다른하나의 지점으로부터 a,b 까지의거리 구한 뒤 최솟값 출력 
    for x in range(1,n+1):
        if temp[s][x] != 2147000:
            res = temp[s][x]
            if temp[x][a] != 2147000 and temp[x][s] != 2147000:
                res += temp[x][a] + temp[x][b]
            if res < result:
                result = res

    return result





n = [6,7,6] # 지점갯수
s=[4,3,4] # 출발지점
a=[6,4,5] # 도착a
b=[2,1,6] # 도착 b
fares=[[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
       [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
       [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]]


for  i in range(3):
    print(solution(n[i],s[i],a[i],b[i],fares[i]))