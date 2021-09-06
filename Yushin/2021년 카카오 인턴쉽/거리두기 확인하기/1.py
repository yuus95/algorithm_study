# P는 응시자가 앉아있는 자리를 의미합니다.
# O는 빈 테이블을 의미합니다.
# X는 파티션을 의미합니다.
# |r1 - r2| + |c1 - c2|
def check(pbox,place):

    for i in range(len(pbox)-1):
        x1 ,y1 = pbox[i][0],pbox[i][1]
        for j in range(i+1,len(pbox)):
            x2,y2 = pbox[j][0],pbox[j][1]
            if x1 == x2 :
                n = abs(y1-y2)
                if  n <= 2 :
                    if n == 1 :
                         if y1 < y2 :
                             if place[x1][y1+1] != 'X':
                                 return False
                         elif y2< y1 :
                             if place[x1][y2+1] != 'X':
                                 return False
                    if n == 2:
                        if y1 < y2:
                            if not(place[x1][y1 + 1] == 'X' or place[x1][y1+2] == 'X'):
                                return False
                        elif y2 < y1:
                            if not(place[x1][y2 + 1] == 'X' or place[x1][y2+2] == 'X'):
                                return False
            elif y1==y2 :
                n = abs(x1-x2)
                if n <= 2 :
                    if n == 1 :
                        if x1 < x2 :
                            if place[x1+1][y1] != 'X':
                                return False
                        if x2 < x1 :
                            if place[x2 + 1][y1] != 'X':
                                return False
                    if n == 2 :
                        if x1 < x2 :
                            if not(place[x1+1][y1] =='X' or place[x1+2][y1] =='X'):
                                return False
                        elif x2< x1  :
                            if not(place[x2+1][y1] =='X' or place[x2+2][y1]=='X'):
                                return False
            else :
                n = abs(x1-x2) + abs(y1-y2)
                if n <= 2 :
                    if x1 < x2:
                        if y1 < y2 :
                            if not(place[x1][y1+1] == 'X' and place[x2][y2-1] =='X'):
                                return False
                        else :
                            if not(place[x1][y1-1] == 'X' and place[x2][y2+1] =='X'):
                                return False
                    elif x2< x1 :
                        if y1 < y2 :
                            if not(place[x2][y2-1] =='X' and place[x1][y1+1]=='X'):
                                return False
                        else :
                            if not (place[x2][y2 + 1] == 'X' and place[x1][y1 -1] == 'X'):
                                return False

    return True

def solution(places):
    answer = []

    for place in places:
        pbox = []
        for x in range(len(place)):
            for y in range(len(place[x])):
                if place[x][y] == 'P':
                    pbox.append((x,y))

        if len(pbox) == 0 :
            answer.append(1)
        else :
            if (check(pbox,place)):
                answer.append(1)
            else :
                answer.append(0)


    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


print(solution(places))