def solution(key, lock):
    answer = False
    key_result = []
    lock_result = []
    lock_long = len(lock)
    key_long = len(key)
    
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    zx, zy = [1, -1, 0, 0], [0, 0, -1, 1]
    
    def rotate(arr):
        demo = [[0] * len(arr) for _ in range(key_long)]
        for x in range(key_long):
            for y in range(key_long):
                demo[y][key_long - 1 - x] = arr[x][y]
        return demo
    
    for x in range(key_long):
        for y in range(key_long):
            if key[x][y] == 1:
                key_result.append((x,y))

    for x in range(lock_long):
        for y in range(lock_long):
            if lock[x][y] == 0:
                lock_result.append((x,y))
                
    for t in range(4): # 90 ~ 360 회전
        key = rotate(key)
        for a in range(1, key_long):
            count  = 0
            for i in range(4): # 상하좌우 이동
                zx[i] = dx[i] * a
                zy[i] = dy[i] * a            
                for x,y in key_result:
                    nx = x + zx[i]
                    ny = y + zy[i]
                    if (nx,ny) in lock_result:
                        count += 1
                    if count == len(lock_result):
                        answer = True    
    return answer