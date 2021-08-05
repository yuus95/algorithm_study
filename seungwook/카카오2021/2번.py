from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        for j in orders:
            list_j = list(j)
            list_j.sort() # orders 안에 내용도 정렬이 필요하므로 정렬시켜준다.
            answer.extend(list(combinations(list_j, i))) # 모든 조합 경우의 수를 answer에 넣어준다.
    
    maxx = 0
    total = []
    counter_answer = Counter(answer) # 모든 경우에 수에 대해서 counter함수로 세어준다.
    for co in course: # course안에 몇자리 수가 필요한지 co로 체크한다.
        result = []
        for i,j in counter_answer.most_common(): # 가장 counter가 많은 수대로 출력해준다.
            if co == len(i): # 원하는 자리수랑 같다면
                if len(result) >= 1: # 만약 이미 자릿수가 result안에 있다면 가장 큰값이랑 같은값만 넣어준다.
                    if max(result) == j and j >= 2:
                        total.append(i)
                        result.append(j)
                elif j >= 2: # 현재 자릿수가 result에 없다면 2보다 크다면 넣어준다.
                    total.append(i)
                    result.append(j)
    total.sort() # 전체 리스트에 대해서 정렬도 필요하므로 해준다.
    demo = []
    for i in total:
        demo.append(''.join(i)) # 문자열로 바꿔 demo에 넣어준다.
    return demo