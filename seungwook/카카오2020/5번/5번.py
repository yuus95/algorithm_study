def solution(n, build_frame):
    # build_frame = [x,y,a,b] => [좌표,좌표,(기둥:0,보:1),(삭제:0,설치:1)]
    answer = [[]]
    pi_graph = [[-1]*(n+1) for _ in range(n+1)] # 기둥, 0이면 기둥 설치된거
    bo_graph = [[-1]*(n+1) for _ in range(n+1)] # 보, 1이면 보 설치된거
    build = tuple(build_frame)
    result = []
    for x,y,a,b in build: # x가 열 y가 행
        if b == 1:
            if a == 1:
                if pi_graph[y-1][x] == 0 or pi_graph[y-1][x+1] == 0 or (bo_graph[y][x+1] == 1 and bo_graph[y][x-1] == 1): # 보를 설치할때는 밑에좌표가 기둥이거나 양옆좌표가 보거나 밑에 오른쪽 좌표가 기둥인 경우.
                    
                    bo_graph[y][x] = 1
            elif a == 0:
                if y == 0 or bo_graph[y][x-1] == 1 or pi_graph[y-1][x] == 0 or bo_graph[y][x] == 1: # 기둥을 설치할때 밑에 좌표가 기둥이거나 바닥이거나 옆에좌표가 보거나 현재 좌표가 보인 경우.
                    pi_graph[y][x] = 0
                    
        elif b == 0:
            if a == 1: # 보를 삭제하는 경우
                if (bo_graph[y][x+1] == -1 or pi_graph[y-1][x+1] == 0) and pi_graph[y][x+1] == -1: # 보를 삭제할 수 있을 경우에만 삭제
                    pi_graph[y][x] = -1
            elif a == 0: # 기둥을 삭제하는 경우
                if bo_graph[y+1][x-1] == 1 and bo_graph[y+1][x] == 1: # 기둥을 삭제할 수 있을 경우에만 삭제
                    pi_graph[y][x] = -1
    
    for x in range(n+1):
        for y in range(n+1):
            if pi_graph[y][x] != -1:
                result.append([x,y,pi_graph[y][x]])
                
    for x in range(n+1):
        for y in range(n+1):
            if bo_graph[y][x] != -1:
                result.append([x,y,bo_graph[y][x]])
        
    result.sort()
    return result