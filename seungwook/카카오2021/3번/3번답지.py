import copy
from itertools import combinations

def solution(info, query):
    answer = []
    #딕셔너리를 이용하기 key : 조건 value :list(조건에 맞는 점수들)
    db = {}
    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        for n in range(5):
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = copy.copy(conditions)
                for v in c:
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                
                if changed_t_c in db:
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]
    
    for value in db.values():
        value.sort()
                    
    for q in query:
        test = q.split()
        qry = [i for i in test if i != 'and'] # 새로운 리스트에 and뺴고 넣어준다.
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])

        if qry_cnd in db:
            data = db[qry_cnd]
            
            start, end = 0, len(data) -1
            while start <= end:
                mid = (start + end) // 2
                if data[mid] >= qry_score:
                    end = mid - 1
                else:
                    start = mid + 1
            answer.append(len(data) - start)
        else:
            answer.append(0)
    return answer


