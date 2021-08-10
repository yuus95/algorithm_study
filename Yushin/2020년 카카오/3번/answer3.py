def solution(key,lock):
    answer = False

    def rotate(key,m):
        temp = [[0] * m  for _ in range(m)]
        for i in range(m):
            for j in range(m):
                temp[j][m-i-1] = key[i][j]

        return temp

    def check(x,y,board,m,key):
        for i in range(m):
            for j in range(m):
                board[x+i][y+j] +=key[i][j]

        for col in board:
            for row in col:
                if row != 1 :
                    return False
        return True

    m = len(key)
    n = len(lock)
    length=2*m +n

    board= [[0]* length for _ in range(length)]

    for i in range(m,m+n):
        for j in range(m,m+n):
            board[i][j] = lock[i-m][j-m]

    for i in range(4):
        key = rotate(key,n)
        for x in range(1,m+n):
            for y in range(1,m+n):
                if(check(x,y,board,m,key)):
                    return True

    return False
