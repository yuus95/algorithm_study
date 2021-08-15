
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:30:16 2021

@author: 82103
"""
import copy

def rotate90(key):
    return list(map(list, zip(*key[::-1]))) 

def test(key, lock, i, j, M, N):
    dump = copy.deepcopy(lock)
    
    for p in range(i, i+M): # dump에 key값 추가
        if 0<= p < N:
            for q in range(j, j+M):
                if 0 <= q < N:
                    dump[p][q] += key[p-i][q-j]
                    
    for line in dump:
        for item in line:
            if item != 1:
                return False
    return True

def solution(key, lock):
    M, N = len(key), len(lock)
    
    for _ in range(4):
        for i in range(-M+1, N): # key의 이동
            for j in range(-M+1, N):
                if test(key, lock, i, j, M, N):
                    return True
    
        key = rotate90(key)
    return False


solution([[0,0,0], [1,0,0], [0,1,1]], [[1,1,1], [1,1,0], [1,0,1]])