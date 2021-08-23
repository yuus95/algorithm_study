nx = 1
ny = 1
size =4

dx = [0,0,-1,1]
dy = [1,-1,0,0]
myboard = [[0]*4 for _ in range(4)]
myboard[3][3] = 1

while True:
    if 0 <= nx + dx[0] < size  and 0 <= ny + dy[0] < size :
        nx += dx[0]
        ny += dy[0]
        if myboard[nx][ny] != 0:
            break
    else:
        break

print(nx,ny)