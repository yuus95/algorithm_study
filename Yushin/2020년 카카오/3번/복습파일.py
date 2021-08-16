
import copy
from collections import deque

dx =[0,0,1,-1]
dy = [1,-1,0,0]
def rotate(key):
    m =len(key)
    temp1 = [[0]* m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            temp1[j][m-i-1] = key[i][j]

    return temp1

def check(key,lock,i,j,m,n):
    temp = copy.deepcopy(lock)
    # (2,2)-> (0,0)    (2,2)--> (1,1)  x y  - >
    for x in range(i,i+m):
        if 0<= x < n :
            for y in range(j,j+m):
                if 0<= y < n :
                    temp[x][y] += key[x-i][y-j]


    for row in temp:
        for col in row:
            if col != 1 :
                return False
    return True







def solution(key, lock):
    answer = True

    # 키부분
    m = len(key)
    n = len(lock)

    for _ in range(4):
        # -m+1 맨마지막칸도 확인하기 위해 (2,2)  --> (0,0) (2,1) --> (0,0)
        for i in range(-m+1,n):
            for j in range(-m+1,n):
                ans=check(key,lock,i,j,m,n)
                if ans == True:
                    return True
        key = rotate(key)


    return False



key =[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock =[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))