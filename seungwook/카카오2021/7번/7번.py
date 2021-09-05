# 트리 DP 문제같은데 DP 구현 못하겠다.

import collections
import sys
def solution(sales, links):
    INF = sys.maxsize
    answer = 0
    leng = len(sales)
    graph = [[] for _ in range(leng+1)]
    visited = [False for _ in range(leng+1)]
    distance = [0 for _ in range(leng+1)]
    dp = [[0, 0] for _ in range(leng+1)]
    # for i in range(leng):
    #     graph[i+1].append(sales[i])
    for a,b in links:
        graph[a].append(b)
    
    def dfs(cur):
        visited[cur] = True
        dp[cur][1] = sales[cur-1]
        dp[cur]
        result = []
        demo = 0
        for next in graph[cur]:
            if visited[next] == False:
                dfs(next)
                dp[cur][1] += min(dp[next][0], dp[next][1])
                result.append(dp[next][1])
                print(result)
                if len(result) == len(graph[cur]):
                    dp[cur][0] += min(result)
            
    dfs(1)
    print(dp)
    print(min(dp[1][1], dp[1][0]))
                    
        
    return answer