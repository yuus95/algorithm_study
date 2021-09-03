# 엔터키 : +1  방향키 : +1


# 카드하나선택
# 카드 모든방향에 대하여 검사?
# 컨트롤키, 그냥방향키 방법 괄호변환

# 한방향으로 일직선으로가는함수 구현
# 그냥 방향으로 한번 가는거 구현


# 1차 BFS 해서 처음 좌표에서 가까운 카드 구하기?
# 카드로부터 시작해서
# 스타트부터 BFS를시작  BFS는 2개의 함수를 적용

# BFS 3번?
    # 처음 시작점부터 최소거리
        # 최소거리 카드와 일치하는 카드에 대하여 최소거리 찾기
            # 그카드에 대하여 다시 최소거리 카드 찾기


from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(r,c,sx,sy):
    return



def solution(board, r, c):
    answer = 0

    q= deque()
    q.append((r,c))
    d= [[-1] * 4 for _ in range(4)]
    d[r][c] = 0
    while q:
        x,y = q.popleft()
        if  board[x][y] != 0 :
            d[x][y] +=1

        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < 4 and 0<= ny < 4:
                if d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] +1
                    q.append((nx,ny))
                    ok = True

                    for x in range(4):
                        nx += dx[k]
                        ny += dy[k]
                        if 0<= nx < 4 and 0<= ny < 4 and board[nx][ny] != 0 and d[nx][ny] == -1  :
                            q.append((nx,ny))
                            d[nx][ny] = d[x][y] +1
                            ok= False
                            break


    return answer


board=[[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]]
r=[1,0]
c=[0,1]


for i in range(2):
    print(solution(board[i],r[i],c[i]))