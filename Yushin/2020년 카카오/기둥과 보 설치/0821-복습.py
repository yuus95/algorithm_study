# 실패


# 보를 설치하는 경우, 기둥을 설치하는 경우
# 보는 양쪽끝이 보와 연결되거나 한쪽 끝 부분이 기둥 위에 있어야 한다
# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.

# a --> 0 :기둥 , 1 : 보
# b --> 0:삭제 , 1 : 추가

# 조건을 모두 만족할 경우 pass ?
def impossible(x,y,a,result):
    if a == 0 :
        if y !=  0 and   (not (x-1,y,1) in result and not (x,y,1) in result) and not (x,y-1,0) in result :
            return  False
    else :
        # if not ((x,y+1,1) in result and (x,y-1,1) in result) and (not (x,y-1,0) in  result and not (x+1,y-1,0) in result) :
        if not( (x+1,y,1) in result and (x-1,y,1) in result) and (not (x,y-1,0) in result and not (x+1,y-1,0) in result) :
            return False
    return True


def solution(n, build_frame):
    result = set()
    for i in range(len(build_frame)):
        x,y,a ,b = build_frame[i][0],build_frame[i][1],build_frame[i][2],build_frame[i][3]
        if b == 1 :
            if impossible(x,y,a,result):
                result.add((x,y,a))
        else :
            temp = list(result)
            ok = True
            temp.remove((x,y,a))
            for a,b,c in temp:
                if  not impossible(a,b,c,result) :
                    ok = False
                    break
            if ok and (x,y,a) in result:
                result.remove((x,y,a))
    answer= []
    for x,y,a in result:
        answer.append([x,y,a])

    answer = sorted(list(answer),key=lambda x:(x[0],x[1],x[2]))
    return answer


n=[5,5]
build_frame=[[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]]


for i in range(2):
    print(solution(n[i],build_frame[i]))
# 	[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
