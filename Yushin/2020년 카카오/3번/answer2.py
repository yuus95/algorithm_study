# 유튜브영상 참고  다시풀어보기

import copy

def rotate(key,m):
    rst = [[0]* m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            rst[j][m-1-i]=key[i][j]
    return rst


def test(key,lock,i,j,m,n):
    dump= copy.deepcopy(lock)
    for p in range(i,i+m):
        if 0<= p < n :
            for q in range(j,j+m):
                if 0<= q < n :
                    dump[p][q] += key[p-i][q-j]

    for line in dump :
        for item in line:
            if item != 1:
                return False

    return True


# m = 3 ,n = 3

def solution(key,lock):
    m,n = len(key),len(lock)
    for _ in range(4):
        # key[2][2]로 lock[0][0]도 검색할 수 있어야함

        for i in range(-m+1,n):
            for j in range(-m+1,n):
                if test(key,lock,i,j,m,n):
                    return True
        key = rotate(key,m)
    return False
key =[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock =[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))