# 틀린 풀이
from itertools import permutations
def solution(expression):
    answer = 0
    op = ['-','+','*']
    
    per = list(permutations(op, 3))
    result = []
    for i1, i2, i3 in per:
        
        exp = expression.split(i1)
        #print(exp)
        for i in exp:
            
            i = i.split(i2)
            str_i = ''.join(i)
            for o in str_i:
                if o in op:
                    break
            else:
                print(o)
                #result.append(int(o))
                if i2 == '-':
                    result.append('-')
                elif i2 == '*':
                    result.append('*')
                else:
                    result.append('+')
            # if len(i) >= 2:
            #     if i2 == '-':
            #         answer = int(i[0]) - int(i[1])
            #     elif i2 == '+':
            #         answer = int(i[0]) + int(i[1])
            #     else:
            #         answer = int(i[0]) * int(i[1])
            for j in i:
                j = j.split(i3)
                
                if len(j) >= 2:
                    if i3 == '-':
                        answer = int(j[0]) - int(j[1])
                    elif i3 == '+':
                        answer = int(j[0]) + int(j[1])
                    else:
                        answer = int(j[0]) * int(j[1])
    return answer