from collections import deque

def solution(s):
    answer = []
    s = s[1:len(s)]
    s = deque(s)
    s_list = []
    temp = ""
    st = ""
    while s:
        ch = s.popleft()
        if ch == "{":
            continue

        if ch == "}":
            if temp =="" :
                continue

            s_list.append(list(temp.split(",")))
            temp = ""
            continue
        if ch== "," and len(temp) == 0  or len(s) == 0 and ch ==",":
            continue
        temp += ch

    s_list=sorted(s_list,key =lambda x:(len(x)))
    answer.extend(s_list[0])
    if len(s_list) > 1:
        for i in range(1,len(s_list)):
            a = set(s_list[i-1])
            test = set(s_list[i])
            c = list(test-a)
            answer.append(c[0])
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    return answer




s = ["{{2},{2,1},{2,1,3},{2,1,3,4}}","{{1,2,3},{2,1},{1,2,4,3},{2}}","{{20,111},{111}}","{{123}}","{{4,2,3},{3},{2,3,4,1},{2,3}}"]

for i in range(len(s)):
    print(solution(s[i]))