# 몰겠다.
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
        set_i = set(i)
        for j in info_split_list:
            set_j = set(j)
            set_ij = set_i - set_j
            if int(i[-1]) <= int(j[-1]):
                if '-' not in set_ij:
                    if len(set_ij) <= 1:
                        count += 1
                elif '-':
                    print(123)
        answer.append(count)
            
    return answer