
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:30:16 2021

@author: 82103
"""
def rotate90(key):
    # 사실, list(map(list, zip(*key[::-1]))) 반환하면 끝
    M = len(key)
    rotate_key = [[0]*M for _ in range(M)] # 회전을 저장할 리스트
    
    for i in range(M):
        for j in range(M):
              rotate_key[j][M-1-i] = key[i][j]
    return rotate_key

def insert_key(x, y, table, key):
    M = len(key)
    for i in range(M): # key 길이
        for j in range(M):
            table[i+x][j+y] += key[i][j]
            
    return table
            
def remove_key(x, y, table, key):
    M = len(key)

    for i in range(M): # key 길이
        for j in range(M):
            table[i+x][j+y] -= key[i][j]    
    return table

def check(table, lock, key):
    N = len(lock)
    M = len(key)
    for i in range(N):
        for j in range(N):
            if table[M+i][M+j] != 1:
                return False
    return True
    

def solution(key, lock):
    M, N = len(key), len(lock)
    table = [[2]*(2*M + N) for _ in range (2*M + N)]
    
    for i in range(N):
        for j in range(N):
            table[M+i][M+j] = lock[i][j]
    
    for i in range(4):
        key = rotate90(key)
        for i in range(1, M+N): # 1부터 M+N-1 까지
            for j in range(1, M+N):
                table = insert_key(i, j, table, key)
                if check(table, lock, key) == True:
                    return True
                table = remove_key(i, j, table, key)
    
    return False


solution([[0,0,0], [1,0,0], [0,1,1]], [[1,1,1], [1,1,0], [1,0,1]])