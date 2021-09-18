# 출력도 안됨 다시풀어보기

import collections
def solution(m, n, board):
    answer = 0
    dx, dy = [1,0,1],[0,1,1] # 아래, 오른쪽, 아래오른쪽 대각선
    queue = collections.deque()
    graph = []
    
    for i in board:
        graph.append(list(i))
    #print(graph)
    demo = []
    def bfs(x,y):
        cnt = 0
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y]:
                    cnt += 1
                    
        if cnt == 3:
            if (x,y) not in demo:
                demo.append((x,y))
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if (nx,ny) not in demo:
                    demo.append((nx,ny))
        
                    
    def down():
        for i in range(m-1, -1 , -1):
            for j in range(n):
                queue.append((i,j))
        
        # while queue:
        #     x,y = queue.popleft()
        #     temp_x, temp_y = x,y
        #     while True:
        #         nx = temp_x + dx[0]
        #         ny = temp_y + dy[0]
        #         if 0 <= nx < m and 0 <= ny < n:
        #             if graph[nx][ny] != 0:
        #                 graph[nx-1][ny] = graph[x][y]
        #                 graph[x][y] = 0
        #                 break
        #             temp_x, temp_y = nx,ny
        #         else:
        #             break
                    
                
            
    
    def check():
        while True:
            for i in range(m):
                for j in range(n):
                    bfs(i,j)
            if demo:
                for a,b in demo:
                    graph[a][b] = 0
            else:
                return
            #down()
            #print(graph)
    check()
    #print(graph)
    #print(demo)
    
    return answer