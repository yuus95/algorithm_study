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
    d= [[0]* n for _ in range(n)]
    q = deque()
    ok = False

    ans = []
    for x in range(m):
        for y in range(m):
            if key[x][y] == 1:
                q.append((x,y))
                d[x][y] = 1
    for x in range(n):
        for y in range(n):
            if lock[x][y] == 0:
                ans.append((x,y))

    ans.sort()

    while q:
        x,y = q.popleft()
        if ok == True :
            break
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<= nx< m and 0< ny < m and d[nx][ny] == 0:
                d[nx][ny] = 1
                q.append((nx,ny))
            d[x][y] = 2

            for _ in range(4):
                compare_box=[]
                for ax in range(m):
                    for ay in range(m):
                        d[ay][m-1-ax] = d[ax][ay]

                        if d[ay][m-1-ax] == 1:
                            compare_box.append((ay,m-1-ax))
                print(d)
                compare_box.sort()
                if compare_box == ans:
                    answer = True
                    ok = True

                if ok == True:
                    break

    return answer



key =[[0, 0, 0], [1, 0, 0], [0, 1, 1]]



lock =[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))