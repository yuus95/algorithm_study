
def solution(n, build_frame):
    answer = []
    pi = [[0 for _ in range(n+1)] for _ in range(n+1)]
    bo = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    def piCheck(x,y):
        if y == 0 or pi[x][y-1] == 1:
            return True
        if (x > 0 and bo[x-1][y] == 1) or bo[x][y] == 1:
            return True
        return False
    
    def boCheck(x,y):
        if pi[x][y-1] == 1 or pi[x+1][y-1] == 1:
            return True
        if x > 0 and bo[x-1][y] == 1 and bo[x+1][y] == 1:
            return True
        return False
    
    def canDelete(x,y):
        for i in range(x-1, x+2):
            for j in range(y, y+2):
                if pi[i][j] and piCheck(i,j) == False:
                    return False
                if bo[i][j] and boCheck(i,j) == False:
                    return False
        return True
            
    for x,y,a,b in build_frame: # x열, y행
        if a == 0: # 기둥
            if b == 1: # 설치
                if piCheck(x,y):
                    pi[x][y] = 1
            else:
                pi[x][y] = 0
                if not canDelete(x,y):
                    pi[x][y] = 1
        else: # 보
            if b == 1: # 설치
                if boCheck(x,y):
                    bo[x][y] = 1
            else:
                bo[x][y] = 0
                if not canDelete(x,y):
                    bo[x][y] = 1
    
    for i in range(n+1):
        for j in range(n+1):
            if pi[i][j] == 1:
                answer.append([i,j,0])
            if bo[i][j] == 1:
                answer.append([i,j,1])
            
    return answer