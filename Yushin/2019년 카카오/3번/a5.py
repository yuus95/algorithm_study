from collections import Counter
from itertools import combinations

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]




def solution(relation):
    answer = 0

    #배열 길이
    n = len(relation)

    #속성길이
    n_tuple = len(relation[0])
    tuple_box =[False] * n_tuple
    temp=[]
    
    
    #유일성 찾기
    for x in range(n_tuple):
        ok = False
        for i in range(n-1):
            for j in range(i+1,n):
                if relation[i][x] == relation[j][x]:
                    ok = True
        if ok == False:
            tuple_box[x] = True
            answer+=1
        else:
            temp.append(x)

    temp_len = len(temp)


    if temp_len < 2:
        return answer


    else:
        for x in range(2,temp_len+1):

            # 유일성만족하지 못하는 데이터들중 2개부터 조합 시작해보기
            test_arr=[]
            ok = False
            combi_num = list(combinations(temp,x))
            for combi in combi_num  :
                text_box= []
                for y in range(n):
                    text=""
                    for k in combi:
                        text+=relation[y][k]
                    text_box.append(text)
                counter = Counter(text_box)
                if max(counter.values()) == 1:
                    answer+=1
                    for kk in combi:
                        temp.remove(k)
                    if len(temp) < 2 :
                        break








    # 카운터
    return answer



print(solution(relation))