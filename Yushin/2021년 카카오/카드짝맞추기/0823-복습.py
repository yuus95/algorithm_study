from collections import deque
from itertools import permutations

size =4
myboard =[[] for i in range(4)]

card_pos = {}

dx = [0,0,1,-1]
dy = [1,-1,0,0]

INF = int(1e4)
answer =INF

orders =[]



def init(board):
    global myboard,card_pos,orders
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0 :
                card = board[i][j]
                if card not in card_pos.keys():
                    card_pos[card] = [[i,j]]
                else :
                    card_pos[card].append([i,j])

            myboard[i].append(board[i][j])

    orders = [key for key in card_pos.keys()]
    orders = list(permutations(orders))
def remove(card):
    global myboard,card_pos
    for x,y in card_pos[card]:
        myboard[y][x] = 0

def restore(card):
    global myboard,card_pos
    for x,y in card_pos[card]:
        myboard[y][x] = card

def bfs(sx,sy,ex,ey):
    if [sx,sy] == [ex,ey] :
        return sx,sy,1
    global myboard
    q = deque()

    table = [[0] * 4 for _ in range(4)]
    d=[[False] * size for _ in range(size)]
    q.append([sx,sy])
    d[sx][sy] = True

    while q:
        x,y = q.popleft()

        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]

            if 0<= nx < size and 0<= ny < size:
                if not d[nx][ny] :
                    d[nx][ny] = True
                    table[nx][ny] = table[x][y]+1
                    if [nx,ny] == [ex,ey] :
                        return nx,ny,table[nx][ny] +1

                    q.append([nx,ny])
                nx_,ny_ = nx,ny

                while True:
                    if 0 <=  nx_ + dx[k] < size and 0 <= ny_ + dy[k] < size:
                        nx_+= dx[k]
                        ny_+=dy[k]
                        if myboard[nx_][ny_] != 0 :
                            nx,ny = nx_,ny_
                            break
                    else:
                        print("aaa",nx, ny)
                        break

                if not d[nx][ny]:
                    d[nx][ny] = True
                    table[nx][ny] = table[x][y] +1
                    if [nx,ny] == [ex,ey]:
                        return nx,ny,table[nx][ny] +1
                    q.append([nx,ny])
    return sx,sy,INF






def backtrack(sy,sx,k,m,count):

    global orders,myboard,answer,card_pos

    if k == len(card_pos.keys()):
        if answer> count :
            answer= count
            return


    # 순열에리스트중 m번째 순서에있는 순열배열에서 K번째에 해당하는 숫자
    card = orders[m][k]

    left_x , left_y = card_pos[card][0][0],card_pos[card][0][1]
    right_x, right_y = card_pos[card][1][0],card_pos[card][1][1]

    rx1,ry1,res1 = bfs(sx,sy,left_x,left_y)
    rx2,ry2,res2 = bfs(rx1,ry1,right_x,right_y)

    remove(card)
    backtrack(rx2,ry2,k+1,m,count+res1,res2)
    restore(card)

    rx1,ry1 ,res1 = bfs(sx,sy,right_x,right_y)
    rx2,ry2,res2 = bfs(rx1,ry1,left_x,left_y)

    remove(card)
    backtrack(rx1,ry2,k+1,m,count+res1,res2)
    restore(card)



def solution(board,r,c):
    global answer
    init(board)
    for i in range(len(orders)):
        backtrack(r,c,0,i,0)

    return answer


board=[[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]]
r=[1,0]
c=[0,1]


for i in range(2):
    print(solution(board[i],r[i],c[i]))
