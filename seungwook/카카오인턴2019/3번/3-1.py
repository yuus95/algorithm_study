from itertools import combinations
def solution(user_id, banned_id):
    answer = 0
    result = []
    demo = []
    for i in banned_id:
        cnt = 0
        demo = []
        for j in user_id:
            if len(i) == len(j):
                for a,b in zip(i,j):
                    if a != b:
                        if a != '*':
                            break
                else:
                    demo.append(j)
            else:
                continue
        result.append(demo)
    print(result)
    # result = set(result)
    # result = list(result)
    # print(result)
    # com = list(combinations(result, len(banned_id)))
    # print(com)
    
    return answer