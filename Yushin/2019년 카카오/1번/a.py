recode = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

# id nickname
# 문제풀이 실패 테스트케이스 3개성공
def solution(record):
    answer = []

    change = []

    id = {}

    result=[]

    for x in record:
        arr = x.split()
        if arr[0] == 'Enter':
            answer.append([arr[1],arr[1],"님이 들어왔습니다."])
            id[arr[1]] = arr[2]
        elif arr[0] == 'Leave':
            answer.append([arr[0],arr[1],"님이 나갔습니다."])

        elif arr[0] == 'Change':
            change.append((arr[1],arr[2]))
            
    for i in range(len(answer)):
        answer[i][1] = id[answer[i][1]]

    for x,y  in change:
        for i in range(len(answer)):
            if answer[i][0] == x:
                answer[i][1]= y

    for i in range(len(answer)):
        result.append(answer[i][1]+answer[i][2])

    return result




print(solution(recode))