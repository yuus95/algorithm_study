

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
import copy
from itertools import combinations



def solution(info, query):
    answer = []
    result= {}

    for i in range(len(info)):
        text = info[i].split()
        qus = text[:-1]
        score = int(text[-1])
        n = len(qus)

        # 질문 갯수만큼 조합사이즈 증가 시키기 질문 5개면  - - - - - 도 될 수 잇고 - 2,3,4,5 도 될 수잇음
        for j in range(n+1):
            combi = list(combinations(list(range(n)),j))

            for c in combi:
                copy_qus = copy.deepcopy(qus)

                for x in c :
                    copy_qus[x] = '-'
                copy_qus = '/'.join(copy_qus)
                if copy_qus in result.keys():
                    result[copy_qus].append(score)
                else :
                     result[copy_qus]= [score]

    for x in result.keys():
        result[x].sort()

    for i in range(len(query)):
        text = query[i].split()
        query_qus = [x for x in text if not x == 'and']
        query_score= int(query_qus[-1])
        query_qus = "/".join(query_qus[:-1])

        if query_qus in result.keys():
            score = result[query_qus]
            scoreSize = len(score)
            lt = 0
            rt = scoreSize-1
            while lt<=rt:
                ans = (rt+lt)//2
                if score[ans] < query_score:
                    lt = ans +1
                elif score[ans]>= query_score:
                    rt = ans- 1
            answer.append(scoreSize-lt)

        else:
            answer.append(0)



    return answer




print(solution(info,query))