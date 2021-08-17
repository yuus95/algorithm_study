def solution(n, build_frame):
    # 보를 설치하는 경우, 기둥을 설치하는 경우
    # 보는 양쪽끝이 보와 연결되거나 한쪽 끝 부분이 기둥 위에 있어야 한다
    # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.

    # build_frame = [x,y,a,b] - (x,y)설치또는 삭제할 교차점의 좌표, a - 설치 또는 삭제할 구조물의 종류 0: 기둥  , 1: 보
    #  b: 구조물을 설치할지 혹은 삭제할 지를 나타낸다 0 : 삭제 1: 설치

    board = [[-1] * n for _ in range(n)]

    # board[i][j] -> -1: 아무것도 없는 상태, 0 : 기둥만 있는 상태 , 1: 보만 있는 경우 2 : 보와 기둥이 연결되어 있는 경우?

    d_pillar=[[0]* n for _ in range(n)] # 0: 빈 공간 1: 시작점 , 2 : 끝점, 3: 시작점과 끝점

    d_bo = [[0] * n for _ in range(n)] # 0 :빈 공간 1: 시작점,  2 : 끝점 , 3 : 시작점과 끝점
    for i in range(len(build_frame)):
        x,y,a,b = build_frame[i]
        if b == 1 :
            if a == 0 :
                if x-1  == 0:
                    d_pillar[x][y] = 2
                elif x-1 >= 0 and (d_pillar[x-1][y] == 1 ):
                    d_pillar[x-1][y] = 2
                    d_pillar[x][y] =


            elif a == 1 :
                if x > 0 :
                    if y < n-1 and  d_bo[x][y] ==2 and d_bo[x][y+1] == 1 :
                        d_bo[x][y] = 3
                        d_bo[x][y+1] = 3
                    elif d_pillar[x][y] >= 1 or (y < n -1 and  d_pillar[x][y+1] >= 1):
                        d_bo[x][y+1] = 2
                        d_bo[x][y] = 1

    print(d_bo)

    #삭제할 경우  기둥 -> 기둥과 연결된 보와 기둥 위치를 봐야 한다.
    # 보를 삭제할 경우 양쪽 끝이 보와 연결되어 있는지 확인,


    answer = [[]]




    # [x,y,a] 형식으로 리턴  기둥, 보는 교차점 좌표를 기준으로 오른쪽 또는 위쪽 방향으로 설치되어 있음을 나타낸다
    # a는 구조물의 종류를 나타내며 0은 기둥 1은 보를 나타낸다.
    # x,y순으로 오름차순 정렬하기
    # x,y좌표가 모두 같은 경우 기둥이 보보다 앞에오면 된다.

    return answer


n=[5,5]
build_frame=[[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]]


for i in range(2):
    print(solution(n[i],build_frame[i]))


