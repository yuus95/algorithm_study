Pillar = [[]]
Bar = [[]]

def checkPillar(x,y): # 기둥이 설치가능 하지 체크
    if y == 0 or Pillar[x][y-1]: # 바닥면, 바로아래에 기둥있는 경우 설치가능
        return True
    if (x > 0 and Bar[x-1][y]) or Bar[x][y]: # 현재 위치에 보가 있는경우, 왼쪽에 보가 있는경우 기둥 설치가능
        return True
    return False

def checkBar(x,y):
    if Pillar[x][y-1] or Pillar[x+1][y-1]: # 아래에 기둥이 있는 경우, 오른쪽 아래에 기둥이 있는경우 보 설치 가능
        return True
    if x > 0 and Bar[x-1][y] == 1 and Bar[x+1][y] == 1:
        return True 
    return False

def canDelete(x,y): # 구조물 삭제후 check 했을때 주변 건축물이 False라면 삭제불가능
    for i in range(x-1, x+2): # 열은 양옆 두부분만 확인하면됨
        for j in range(y, y+2): # 행은 밑에부분은 안봐도 되고 위에만 보면된다. (모든 건축물이 위와 오른쪽으로 진행되기 때문)
            if Pillar[i][j] and checkPillar(i,j) == False:
                return False
            if Bar[i][j] and checkBar(i,j) == False:
                return False
    return True
            
def solution(n, build_frame):
    global Pillar, Bar
    Pillar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    Bar = [[0 for _ in range(n+2)] for _ in range(n+2)]

    for x, y, kind, cmd in build_frame: # 이 문제에서는 x가 열 y가 행으로 주지만 행열이 n으로 같으므로 주어진 대로 하는게 편하다.
        if kind == 0: # 기둥
            if cmd == 1: # 설치
                if checkPillar(x,y):
                    Pillar[x][y] = 1
            else: # 삭제
                Pillar[x][y] = 0
                if not canDelete(x,y):
                    Pillar[x][y] = 1
        else: # 보
            if cmd == 1: # 설치
                if checkBar(x,y):
                    Bar[x][y] = 1
            else: # 삭제
                Bar[x][y] = 0
                if not canDelete(x,y):
                    Bar[x][y] = 1


    answer = []
    for x in range(n+1):
        for y in range(n+1):
            if Pillar[x][y]:
                answer.append([x,y,0])
            if Bar[x][y]:
                answer.append([x,y,1])
    return answer


