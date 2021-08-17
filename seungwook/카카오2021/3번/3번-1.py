# 시간초과
def solution(info, query):
    answer = []
    info_split_list = []
    query_split_list = []
    for i in info:
        info_split_list.append(i.split())
    for i in query:
        demo = i.split() # 공백 제거 
        demo.insert(7, 'and') # and로 구분하기 위해 특정 장소에 and 추가
        query_split_list.append(''.join(demo).split('and')) # 문자열로 바꾼후 and로 다시 split
    
    for i in query_split_list:
        count = 0
        speak = i[0]
        job = i[1]
        year = i[2]
        food = i[3]
        test = i[4]
        for j in info_split_list:
            if speak == j[0] or speak == '-':
                if job == j[1] or job == '-':
                    if year == j[2] or year == '-':
                        if food == j[3] or food == '-':
                            if int(test) <= int(j[4]):
                                count += 1
        answer.append(count)
    return answer