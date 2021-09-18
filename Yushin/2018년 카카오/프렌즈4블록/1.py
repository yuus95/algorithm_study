from collections import deque
import copy

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def change_board(board,d,x1,y1,x2,y2):
    box = copy.deepcopy(board)
    check = [[0] * len(board[x2]) for _ in range(x1)]
    # print(check)
    # print(len(board))
    # print(len(board[x2]))


    for i in range(x2,x1-1,-1):
        for j in range(len(board[x2])-1,-1,-1):
            if d[i][j] == 1:
                for i2 in range(0,x1+1):
                    if d[i2][j] == 0 :
                        d[i2][j] = -1
                        box[i][j] = board[i2][j]
                        box[i2][j] = '-'
    print(box)
    return  box


def bfs(x,y,board):
    if board[x][y] == '-':
        return 0,board
    q = deque()
    q.append((x,y))
    d = [[0] * len(board[x]) for _ in range(len(board))]
    d[x][y] = 1
    num = 0
    x1,y1 = x,y

    while q:
        x,y = q.popleft()
        tt= 1
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<= nx < len(board)  and 0<= ny < len(board[x]) and board[nx][ny] == board[x][y]:
                if d[nx][ny] == 0 :
                    d[nx][ny] = 1
                    tt +=1
            if tt >= 4 :
                print(d)
                for k1 in range(4):
                    nx,ny =x +dx[k1],y+dy[k1]
                    q.append((nx,ny))
                num += 4
                print(d)

    if num >= 4 :
        for i in range(len(board)):
            for j in range(len(board[x])):
                if d[i][j] ==1 :
                    x2 ,y2 = i,j
        board = change_board(board,d,x1,y1,x2,y2)
    return num , board

def solution(m, n, board):
    cnt = 0
    temp = [[] for _ in range(m)]


    for x in range(len(board)):
        for y in range(len(board[x])):
            temp[x].append(board[x][y])

    test = copy.deepcopy(temp)
    print(test)
    for x in range(len(temp)):
        for y in range(len(temp[x])):
                num,test=bfs(x,y,test)
                # print(num)
                cnt+=num
    print(cnt,test)

    answer = 0


    return answer


m= [4,6]
n = [5,6]
board = [["CCBDE", "AAADE", "AAABF", "CCBBF"],["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]


for i in range(2):
    print(solution(m[i],n[i],board[i]))