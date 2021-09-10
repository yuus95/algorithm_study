from itertools import permutations
def solution(expression):
    answer = []
    exp = []
    op = ['-', '+', '*']
    demo = ''
    per = list(permutations(op, 3))
    for i in expression:
        if i.isdigit():
            demo += i
        else:
            exp.append(demo)
            exp.append(i)
            demo = ''
    exp.append(demo)
    
    print(exp)
    for i1, i2, i3 in per:
        temp = []
        for j in range(len(exp)):
            if temp:
                if temp[-1] == i1:
                    temp.pop()
                    if i1 == '-':
                        temp[-1] = int(temp[-1]) - int(exp[j])
                    elif i1 == '+':
                        temp[-1] = int(temp[-1]) + int(exp[j])
                    else:
                        temp[-1] = int(temp[-1]) * int(exp[j])
                else:
                    temp.append(exp[j])
            else:
                temp.append(exp[j])
        temp2 = []
        for k in range(len(temp)):
            if temp2:
                if temp2[-1] == i2:
                    temp2.pop()
                    if i2 == '-':
                        temp2[-1] = int(temp2[-1]) - int(temp[k])
                    elif i2 == '+':
                        temp2[-1] = int(temp2[-1]) + int(temp[k])
                    else:
                        temp2[-1] = int(temp2[-1]) * int(temp[k])
                else:
                    temp2.append(temp[k])
            else:
                temp2.append(temp[k])
        temp3 = []
        for m in range(len(temp2)):
            if temp3:
                if temp3[-1] == i3:
                    temp3.pop()
                    if i3 == '-':
                        temp3[-1] = int(temp3[-1]) - int(temp2[m])
                    elif i3 == '+':
                        temp3[-1] = int(temp3[-1]) + int(temp2[m])
                    else:
                        temp3[-1] = int(temp3[-1]) * int(temp2[m])
                else:
                    temp3.append(temp2[m])
            else:
                temp3.append(temp2[m])

        answer.append(abs(temp3[0]))
                    
    return max(answer)