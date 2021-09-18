from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    per = list(permutations(user_id, len(banned_id)))
    result = []
    demo = []
    def check(a,b):
        for x,y in zip(a,b):
            if len(x) == len(y):
                for i,j in zip(x,y):
                    if i != j:
                        if j != '*':
                            return False
            else:
                return False
        return True
        
    
    for i in per:
        if check(i, banned_id):
            if set(i) not in result:
                result.append(set(i))
    

    
    return len(result)