import collections
from itertools import permutations
import sys
def solution(board, r, c):
    answer = 0
    queue = collections.deque()
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    result = []
    for x in range(4):
        for y in range(4):
            if board[x][y] >= 1:
                result.append((x,y))
    
    def bfs(a,b):
        queue.append((a,b))
        while queue:
            x,y = queue.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < 4 and 0 <= ny < 4:
                    if visited[nx][ny] == False:
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx,ny))
    
    per = list(permutations(result, len(result)))
    for i in per:
        total = 0
        answer = sys.maxsize
        temp_r, temp_c = r, c
        for x,y in i:
            visited = [[False]*4 for _ in range(4)]
            distance = [[0]*4 for _ in range(4)]
            bfs(temp_r,temp_c)
            
            if distance[x][y] > 1:
                if x == temp_r or y == temp_c:
                    total += 3 # ctrl, enter, 이동한번
                elif distance[x][y] == 2:
                    total += 3 # 이동, 이동, enter
                else:
                    total += 4 # 이동, ctrl, 이동, enter
            elif distance[x][y] == 1:
                total += 2 # 이동, enter
            else:
                total += 1 # enter
            temp_r, temp_c =  x, y
        answer = min(answer, total)
        
    
    return answer