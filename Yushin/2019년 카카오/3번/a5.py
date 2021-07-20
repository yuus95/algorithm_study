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

    for x in range(2,(temp_len+1)):
        text = list(combinations(temp,x))
        for x1 in text:
                text_box = []
                res_1 = ""
                for y1 in range(n):
                    for i in x1:
                        res_1+=relation[y1][i]

                    text_box.append(res_1)




    # 카운터
    return answer



print(solution(relation))