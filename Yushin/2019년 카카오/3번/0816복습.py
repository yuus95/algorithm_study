from collections import  deque
from itertools import combinations


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]



def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])
    candidates = []
    for i in range(1,n_col+1):
        candidates.extend(combinations(range(n_col),i))

    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)


    # intersection() 교집합
    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            # final[i] 와 final[j]의 교집합의 길이가 final[i] 와 같다면 최소성 실패 discard
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)
print(solution(relation))