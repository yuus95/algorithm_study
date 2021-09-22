from collections import deque

dx = [0,1,1]
dy = [1,0,1]




def solution(m, n, board):

    answer = 0
    b = list(map(list,board))


    while True:
        cnt_box=[]
        for i in range(1,m):
            for j in range(1,n):
                if b[i][j] != '-' and b[i][j] == b[i-1][j] == b[i-1][j-1] == b[i][j-1]:
                    cnt_box.append((i,j))
                    cnt_box.append((i,j-1))
                    cnt_box.append((i-1,j-1))
                    cnt_box.append((i-1,j))

        if len(cnt_box) == 0 :
            break

        cnt_box = set(cnt_box)
        answer += len(cnt_box)

        for x,y in cnt_box:
            b[x][y] = '-'
        for i in range(n):
            q = deque()
            q.append((m-1))
            temp = []
            while q:
                k =  q.popleft()
                if b[k][i] != '-':
                    temp.append(b[k][i])
                if k-1 >= 0 :
                    q.append(k-1)
            if len(temp) != m:
                num = m - len(temp)
                temp += ['-'] * num
            temp = temp[::-1]
            for j in range(m-1,-1,-1):
                b[j][i] = temp[j]


    return answer


m= [4,6]
n = [5,6]
board = [["CCBDE", "AAADE", "AAABF", "CCBBF"],["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]


for i in range(2):
    print(solution(m[i],n[i],board[i]))