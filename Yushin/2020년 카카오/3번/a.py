#  열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다.

# 이동 400 * 회전 4
from collections import deque

dx =[0,0,1,-1]
dy = [1,-1,0,0]


# 배열이랑 회전번호 넣기
def rotate_arr(d,lock,ans):
    print(d)
    return




def solution(key, lock):
    answer = True
    m = len(key)
    n = len(lock)
    ans = []
    d = [[0] * n for _ in range(n)]
    check= [[False] * m for _ in range(m)]
    q = deque()
    for x in range(m):
        for y in range(m):
            if key[x][y] == 1:
                q.append((x,y,0))
                d[x][y] = 1

    for x in range(n):
        for y in range(n):
            if lock[x][y] == 0:
                ans.append((x,y))

    while q:
        x,y,cnt = q.popleft()
        check[x][y] = True
        if len(q) != 0 :
            if q[0][2] != cnt :
                rotate_arr(d,lock,ans)

        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 > nx or  m <=  nx or 0 > ny or m <= ny:
                d[x][y] = 0
            elif 0<= nx < m and 0<= ny < m and  check[nx][ny]  == False:
                d[x][y] =  0
                d[nx][ny] = 1
                q.append((nx,ny,cnt+1))



    return answer



key =[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock =[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))