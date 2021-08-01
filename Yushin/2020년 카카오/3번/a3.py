#  열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다.

# 이동 400 * 회전 4
from collections import deque

dx =[0,0,1,-1]
dy = [1,-1,0,0]

# arr[c][n-1-r]

def solution(key, lock):
    answer = False
    m =len(key)
    n = len(lock)
    q = deque()
    ok = False
    ans = []

    for x in range(m):
        for y in range(m):
            if key[x][y] == 1:
                q.append((x,y))
    for x in range(n):
        for y in range(n):
            if lock[x][y] == 0:
                ans.append((x,y))

    ans.sort()

    while q:
        x,y = q.popleft()
        for i in range(4):
            d = [[0] * n for _ in range(n)]
            d_ans = []
            for ax in range(m):
                for ay in range(m):
                    if i == 0:
                        d[ay][m-ax-1] = key[ax][ay]
                    elif i == 1:
                        d[m-1-ay][m - ax - 1] = key[ax][ay]
                    elif i == 2 :
                        d[m-1-ay][ax]=key[ax][ay]
                    elif i == 3:
                        d[ax][ay]= key[ax][ay]
            for kx in range(m):
                for ky in range(m):
                    if d[kx][ky] == 1:
                        d_ans.append((kx,ky))
            d_ans.sort()
            if d_ans == ans:
                answer=True
            ok = True

        if ok == True:
            break

        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<= nx < m and 0<= ny < m and key[nx][ny] == 0:
                q.append((nx,ny))
                key[nx][ny] = 1
                key[x][y] = 0




    return answer



key =[[0, 0, 0], [1, 0, 0], [0, 1, 1]]



lock =[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))