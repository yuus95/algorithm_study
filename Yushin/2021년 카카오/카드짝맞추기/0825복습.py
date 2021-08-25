import copy
from collections import deque
from itertools import permutations

n = 4
# 카드마다 갖고있는 좌표 저장
card_pos = {}
num_box = []
answer = 0
myboard = [[0] * 4 for _ in range(4)]

dx=[0,0,-1,1]
dy= [1,-1,0,0]

def init(board):
    global card_pos,num_box,myboard
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 :
                if not board[i][j] in card_pos.keys():
                    card_pos[board[i][j]] = [[i,j]]
                else:
                    card_pos[board[i][j]].append([i,j])
            myboard[i].append(board[i][j])
    num_box = list(range(1,max(card_pos.keys())+1))
    num_box = list(permutations(num_box))


def check(x,y):
    if 0<= x < 4  and 0<= y <4 :
        return True
    return False

def c_move(x,y,k):
    global myboard
    nx,ny = x,y

    while True:
        _nx = nx +dx[k]
        _ny = ny +dy[k]
        if not check(_ny,_nx):
            return nx,ny

        if myboard[_nx][_ny] != 0 :
            return _nx,_ny
        nx = _nx
        ny = _ny

def bfs(sx,sy,ex,ey):
    if [sx,sy] == [ex,ey]:
        return [sx,sy,1]
    q = deque()
    d = [[-1] * 4 for _ in range(4)]
    d[sx][sy] = 1
    q.append((sx,sy))

    while q:
        x,y = q.popleft()

        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if check(nx,ny):
                if d[nx][ny]  == -1:
                    d[nx][ny] = d[x][y]+1
                    if [nx,ny] == [ex,ey] :
                        return [nx,ny,d[nx][ny]+1]
                    q.append((nx,ny))

            nx,ny = c_move(x,y,k)
            if d[nx][ny] == -1 :
                d[nx][ny] = d[x][y] +1
                if [nx,ny] == [ex,ey]:
                    return [nx,ny,d[nx][ny]+1]
                q.append((nx,ny))
    return sx,sy,2147000000


def discard(card):
    global card_pos,myboard

    for x,y in card_pos[card]:
        myboard[x][y] = 0

def restore(card):
    global card_pos
    for x,y in card_pos[card]:
        myboard[x][y] = card




def backtrack(st,et,idx,card_idx,num):
    global card_pos,num_box,answer
    if card_idx == len(card_pos.keys()):
        if answer > num:
            answer = num
        return


    card = num_box[idx][card_idx]
    lx,ly = card_pos[card][0][0],card_pos[card][0][1]
    rx,ry = card_pos[card][1][0],card_pos[card][1][1]



    left_start = bfs(st,et,lx,ly)
    left_start2 = bfs(left_start[0],left_start[1],rx,ry)


    discard(card)
    backtrack(left_start2[0],left_start2[1],idx,card_idx+1,num+left_start[2]+left_start2[2])
    restore(card)

    right_start = bfs(st,et,rx,ry)
    right_start2 = bfs(right_start[0],right_start[1],lx,ly)

    discard(card)
    backtrack(right_start2[0],right_start2[1],idx,card_idx+1,num+right_start[2]+right_start2[2])
    restore(card)



def solution(board,r,c):
    global card_pos,num_box,answer
    answer=2147000000
    num_box=[]
    card_pos={}
    init(board)

    for i in range(len(num_box)):
        backtrack(r,c,i,0,0)


    return answer


board=[[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]]
r=[1,0]
c=[0,1]


for i in range(2):
    print(solution(board[i],r[i],c[i]))
