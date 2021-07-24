#다른사람 문제풀이
from itertools import combinations


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]


# x = [a,b,c] , y = 'ping' , z = [test,test1]

# list.append(y)는 리스트 끝에 x 1개를 그대로 넣습니다.
# x.append(y) == > [a,b,c,ping]
# x.append(z) == > [a,b,c,[test,test1]

# list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣습니다.
# x.append(y)== > [a,b,c,p,i,n, g]
# x.append(z) ==> [a,b,c,test,test1]

def solution(relation):
    n_row = len(relation) #  로우 길이(튜플갯수)
    n_col = len(relation[0]) # 열 길이(속성)

    candidates = []
    candidates2= []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))  #
        # [(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]


        candidates2.append(list(combinations(range(n_col), i)))
    # candidates2 [[(0,), (1,), (2,), (3,)], [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)], [(0, 1, 2, 3)]]

    final = []  #유일성 만족하는 경우 속성 번호 넣기
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)

    answer = set(final[:])

    
    print("answer",answer)
    print("final",final)

    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            # final에 들어있는 수를 앞에서부터 차례대로 비교하여 중복된 값을 삭제한다.
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))): # x.intersection(y) y와 교집합을 리턴
                answer.discard(final[j]) # discard(값) - 전달받은 값을 삭제 (없을 때 그냥 무시)
    print(answer)


    return len(answer)




print(solution(relation))