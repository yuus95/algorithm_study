from collections import Counter
from itertools import combinations




def solution(relation):
    answer = 0
    #배열 길이
    n = len(relation)

    #속성길이
    n_tuple = len(relation[0])

    for i in range(n_tuple):
        temp = []
        for j in range(n):
            temp.append(relation[j][i])
        counter = Counter(temp)
        if max(counter.values()) == 1:
            answer+=1

        else :
            for recur in range(1,n-i+1):
                ok = False
                temp2 = []
                for x in range(i+1,n_tuple):
                    for y in range(n):
                        text= relation[y][i]
                        text2 = ''.join(relation[y][x:x+recur])
                        text+= text2
                    temp2.append(text)
                    counter2=Counter(temp2)
                    print(counter2)
                    if max(counter2.values()) == 1:
                        answer+=1
                        ok = True
                        break
                if ok :
                    break





    return answer






relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]



print(solution(relation))