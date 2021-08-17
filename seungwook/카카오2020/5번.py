def solution(n, build_frame):
    # build_frame = [x,y,a,b] => [좌표,좌표,(기둥:0,보:1),(삭제:0,설치:1)]
    answer = [[]]
    graph = [[-1]*(n+1) for _ in range(n+1)]
    build = tuple(build_frame)
    result = []
    for x,y,a,b in build: # x가 열 y가 행
        if b == 1:
            if a == 1:
                print(y,x)
                print(graph)
                if graph[y-1][x] == 0 or (graph[y][x+1] == 1 and graph[y][x-1] == 1): # 보를 설치할때는 밑에좌표가 기둥이거나 양옆좌표가 보여야한다.
                    
                    graph[y][x] = 1
            elif a == 0:
                if graph[y][x] == -1 or graph[y][x-1] == 1 or graph[y-1][x] == 0: # 기둥을 설치할때 밑에 좌표가 기둥이거나 바닥이거나 옆에좌표가 보여야한다.
                    graph[y][x] = 0
        elif b == 0:
            if a == 1:
                if graph[y][x+1] != 1 and graph[y][x-1] != 1:
                    graph[y][x] = -1
            elif a == 0:
                if graph[y+1][x-1] == 1 and graph[y+1][x+1] == 1: # 기둥을 삭제할 수 있을 경우에만 삭제
                    graph[y][x] = -1
    print(graph)
    for x in range(n+1):
        for y in range(n+1):
            if graph[y][x] != -1:
                result.append([x,y,graph[y][x]])
        
    
    return result