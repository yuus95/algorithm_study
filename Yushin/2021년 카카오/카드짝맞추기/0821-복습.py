# 카드 순서를 순열로 받아놓기
# 시작점에서부터 카드까지 거리 더하기
#
from itertools import permutations
from collections import deque
import copy
dx = [0,0,-1,1]
dy = [1,-1,0,0]





def bfs(ex,ey,sx,sy,deep_board):
    print(sx,sy)
    d = [[-1] * 4 for _ in range(4)]
    q= deque()
    d[sx][sy] = 0
    q.append((sx,sy))

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<= nx < 4 and 0<= ny< 4 :
                if d[nx][ny] == - 1 :
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))
            ok = True
            while 0<= nx+dx[k] < 4 and 0 <= ny+dy[k] < 4 :
                nx += dx[k]
                ny += dy[k]
                if deep_board[nx][ny] != 0 and d[nx][ny] == -1 :
                    d[nx][ny] = d[x][y] + 1
                    ok = False
                    q.append((nx,ny))
                    break
            nx -=dx[k]
            ny -= dy[k]
            if ok and d[nx][ny] == -1 :
                d[nx][ny] = d[x][y] +1
                q.append((nx,ny))

    distance = d[ex][ey]+1
    return [ex,ey,distance]

def dfs(sx,sy,card_order_idx,card_box_idx,card_order,card_box,deep_board):
    if len(card_box) == card_box_idx:
        return





    sx,sy,temp = bfs(card_box[card_order[card_order_idx][card_box_idx]][0][0], card_box[card_order[card_order_idx][card_box_idx]][0][1], sx, sy, deep_board)
    sx,sy,temp = bfs(card_box[card_order[card_order_idx][card_box_idx]][1][0], card_box[card_order[card_order_idx][card_box_idx]][1][1], sx, sy, deep_board)
    dfs(sx,sy,card_order_idx,card_box_idx+1,card_order,card_box,board)



    bfs(card_box[card_box_idx][1][0], card_box[card_box_idx][1][1], sx, sy, deep_board)
    bfs(card_box[card_box_idx][0][0], card_box[card_box_idx][0][1], sx, sy, deep_board)

    # card_b
    #

    #



def solution(board, r, c):
    n = 4
    card_box = []
    temp = dict()
    answer = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0 :
                if not board[i][j] in temp :
                    temp[board[i][j]]= [(i,j)]
                else :
                    temp[board[i][j]].append((i,j))
    card_box = [[] for _ in range(max(temp))]
    for x in temp.keys():
        card_box[x-1]=temp[x]

    card_order = list(range(max(temp)))
    card_order=list(permutations(card_order))

    for i in range(len(card_order)):
        dfs(r,c,i,0,card_order,card_box,board)

        #
        # i_len=0
        # sx=r
        # sy=c
        # for card in card_order[i]:
        #
        #     # start card_box[card][0]  card박스에서 card의 첫번쨰 좌표 부터시작
        #     bfs(card_box[0][0],card_box[0][1],sx,sy,deep_board)
        #
        #     bfs(card_box[1][0],card_box[1][1],sx,sy,deep_board)


    return answer


board=[[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]]
r=[1,0]
c=[0,1]


for i in range(2):
    print(solution(board[i],r[i],c[i]))