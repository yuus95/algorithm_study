

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
import copy
from itertools import combinations



def solution(info, query):
    answer = []
    #딕셔너리를 이용하기 key : 조건 value :list(조건에 맞는 점수들)
    res = {}

    query_arr=[]

    for inf in info :
        # 문자열 짜르기 조건과 점수 나누기
        temp = inf.split()
        temp_condi = temp[:-1]
        temp_score = int(temp[-1])
        #[0,1,2,3]1~4
        # '-' 는 문제에서 상관없음을 의미
        # 4가지의 조건에 대하여 '-' 들어갈 수 있는 경우 조합 만들기
        for i in range(5):
            stick_arr = list(combinations(range(4),i))
            for stick in stick_arr:
                temp_condi_stick = copy.deepcopy(temp_condi)
                for k in stick:
                    temp_condi_stick[k] = '-'
                temp_condi_stick='/'.join(temp_condi_stick)
                if temp_condi_stick in res:
                    res[temp_condi_stick].append(temp_score)
                else:
                    res[temp_condi_stick]=[temp_score]
    # 조건에 해당하는 value 정렬하기
    for k in res.keys():
        res[k].sort()

    # 답찾기
    for q in query:

        # 쿼리문도 조건과 점수 나누기
        test = q.split()
        q_text = [x for x in test  if x != "and"]
        q_query="/".join(q_text[:-1])
        q_score=int(q_text[-1])

        # 해당하는 조건이 res안에 있을 경우 이분탐색
        if q_query in res:
            score_arr = res[q_query]
            n =len(score_arr)
            rt = n-1
            lt = 0
            mid = (lt+rt)//2
            while lt<=rt:
                mid = (lt+rt)//2
                if score_arr[mid] < q_score:
                    lt = mid +1
                elif score_arr[mid] >= q_score:
                    rt = mid - 1
            answer.append(n-lt)
        # 해당하는 조건이 없을 경우
        else:
            answer.append(0)

    return answer




print(solution(info,query))