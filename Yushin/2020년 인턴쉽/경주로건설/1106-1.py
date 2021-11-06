import sys
sys.setrecursionlimit(10**6)

#  0 빈칸 1 벽
# 0 ~ n- 1
# 직선도로 100원 코너 500원

# DFS

nx = [0,0,1,-1]
ny = [1,-1,0,0]
result = 2147000


def dfs(board,n,x,y,box,check):
    global result

    if x == n-1 and y == n-1 :
        print(box)
        # 0일때는 가로, 1일 때는 세로
        ch = 0
        r,c = box[1]
        num = 0
        if r == 1:
            ch = 1
        for i in range(2,len(box)):
            x,y = box[i]
            r,c = box[i-1]
            if ch == 1 and r == x :
                num +=500
                ch = 0
            if ch == 0 and c == y:
                num += 500
                ch = 1
        num = num + (100 * (len(box)-1))
        if num < result:
            result = num



    for i in range(4):
        dx,dy = x +nx[i],y+ny[i]
        if 0<= dx < n and 0<= dy < n and board[dx][dy] != 1 :
            if check[dx][dy] == False:
                check[dx][dy] = True
                dfs(board,n,dx,dy,box+[(dx,dy)],check)
                check[dx][dy] = False



def solution(board):
    answer = 0
    n = len(board[0])
    check  =[[False] * n for _ in range(n)]
    # box = [(0,0)]
    # box += [(1,0)]
    # print(box)
    check[0][0] = True
    dfs(board,len(board[0]),0,0,[(0,0)],check)
    print(result)
    return answer




board = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
         ,[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],[[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]]

print(solution(board[0]))
# for i in range(len(board)):
#     print(solution(board[i]))