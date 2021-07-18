recode = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

# id nickname

def solution(record):
    answer = []
    
    # 딕을 이용해 아이디 변경될 떄마다 id에 관한 닉네임값 변경해주기 
    id = {}

    result=[]

    for x in record:
        arr = x.split()
        # 들어올 떄 아이디를 변경한 경우도 처리해주기
        if arr[0] == 'Enter':
            answer.append([arr[1],"님이 들어왔습니다."])
            id[arr[1]] = arr[2]
        elif arr[0] == 'Leave':
            answer.append([arr[1],"님이 나갔습니다."])
        # change될 때 아이디에 대한 닉네임 변경 처리해주기
        elif arr[0] == 'Change':
            id[arr[1]] = arr[2]

    for i in range(len(answer)):
        answer[i][0] = id[answer[i][0]]

    for i in range(len(answer)):
        result.append(answer[i][0]+answer[i][1])

    return result




print(solution(recode))
