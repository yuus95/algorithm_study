def rotation(key):
    ret = [[0] * len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            ret[j][len(key) -1 -i] = key[i][j]
    return ret
        
    
def check(arr, key, lock):
    count = 0
    #print(arr)
    for i in range(len(key)-1, len(key) + len(lock)-1):
        for j in range(len(key)-1, len(key) + len(lock)-1):
            if arr[i][j] != 1:
                return False
    return True
    

def reset(key, lock):
    arr = [[0] * (len(key) * 2 + len(lock) - 2) for _ in range(len(key) * 2 + len(lock) - 2)]
    for a in range(len(lock)):
        for b in range(len(lock)):
            arr[a + len(key) -1][b + len(key) -1] = lock[a][b]
    
    return arr

def solution(key, lock):
    answer = True
    key_len = len(key)
    lock_len = len(lock)
    leng = len(key) * 2 + len(lock) - 2
    
            
    for i in range(key_len + lock_len -1):
        for j in range(key_len + lock_len -1):
            for k in range(4):
                arr = reset(key, lock)
                
                key = rotation(key)
                print(key)
                for x in range(key_len):
                    for y in range(key_len):
                        #print(i,j,x,y)
                        arr[x+i][y+j] += key[x][y]
                #print(arr)
                chk = check(arr, key, lock)
                if chk:
                    return True
    return False
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))