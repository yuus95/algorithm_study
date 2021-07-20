from collections import Counter


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]




def solution(relation):
    answer = 0

    #배열 길이
    n = len(relation)

    #속성길이
    n_tuple = len(relation[0])


    for i in range(n_tuple):
        ok = False
        for j in range(n-1):
            for k in range(j+1,n):
                if relation[j][i] == relation[k][i]:
                    ok = True
                    break
            if ok == True:
                break

        if ok == False:
            answer+=1
            continue

        for recur in range(1,n-i+1):
            ok2 = False
            for x in range(n-1):
                temp = relation[x][i:i+recur+1]
                temp = ''.join(temp)
                for y in range(x+1,n):
                    compare = relation[y][i:i+recur+1]
                    compare = ''.join(compare)
                    print(temp,compare)
                    if temp == compare:
                        ok2 = True

            if ok2 == False:
                answer +=1
                break




    # 카운터
    return answer



print(solution(relation))