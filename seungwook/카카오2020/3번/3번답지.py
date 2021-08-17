# 90도 회전
def rotation(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            ret[y][n-1-x] = arr[x][y]
    return ret

# 자물쇠가 열리는지 체크
# key_start_x, key_start_y는 key가 들어가기 시작할 인덱스
def check(key_start_x, key_start_y, key, lock, expendSize, lock_start, lock_end):
    expendList = [[0] * expendSize for _ in range(expendSize)]

    # expendList에 key 추가
    for i in range(len(key)):
        for j in range(len(key)):
            expendList[key_start_x + i][key_start_y + j] += key[i][j]
    
    # expendList에 lock 추가하면서 기존 값이랑 더하기
    for i in range(lock_start, lock_end):
        for j in range(lock_start, lock_end):
            expendList[i][j] += lock[i - lock_start][j - lock_start] # lock배열에 값을 더해준다. i, j는 lock_start만큼 이동했기 때문에 다시 빼준다.
            if expendList[i][j] != 1:
                return False
    return True

def solution(key, lock):
    start = len(key) - 1 # expendList에서 lock의 시작 지점
    end = start + len(lock) # expendList에서 lock이 끝나는 지점
    expendSize = len(lock) + start * 2 # expendList 배열의 크기

    # lock은 고정이고 key가 움직이는거
    for a in range(0,4):
        for i in range(end): # end까지만 돌아줘도 되는 이유는 end 위치부터 key값이 들어가기 때문이다.
            for j in range(end):   
                if check(i, j, key, lock, expendSize, start, end):
                    return True
        key = rotation(key)
    return False
    