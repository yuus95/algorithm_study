from collections import Counter
from itertools import combinations

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]



# 후보키 찾고 제외하고


def solution(relation):
    answer = 0
    col_len= len(relation[0])
    row_len = len(relation)

    cKey= set()

    for i in range(col_len):
        temp=set()
        for j in range(row_len):
            temp.add(relation[j][i])
        if len(temp) == row_len:
            cKey.add(i)
            answer+=1

    for i in range(col_len-1):
        if not i in cKey:
            text = list(range(i+1,col_len))
            for j in range(1,len(text)):
                temp = list(combinations(text,j))
                for combi_num in temp:
                    for c_num in combi_num:
                            for c in range(row_len):
                                print()

    return answer



print(solution(relation))