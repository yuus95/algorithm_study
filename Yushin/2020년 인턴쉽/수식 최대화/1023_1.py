from copy import copy
from itertools import permutations

# 연산 구하기
# 순열
# 우선순위대로 계산하기

def next_permutation(x):
    i = len(x)-1
    j = len(x)-1

    while  i > 0  and x[i-1]>= x[i]:
        i-=1
    if i == 0 :
        return False
    while x[i-1] >= x[j]:
        j-=1
    x[i-1],x[j] = x[j],x[i-1]
    k = len(x)-1
    while i < k:
        x[i],x[k] = x[k],x[i]
        i+=1
        k-=1
    return x
# 1+3 +4 [1,3,5,7]

def cal(box,problem,su):
    res = 0
    temp = copy(problem)
    for i in box:
        # 수식길이
        k =  len(problem) // 2
        for j in range(k):
            jj = j *2 +1
            if temp[jj] == su[i]:

                if temp[jj] == '+':
                    temp[jj-1] = temp[jj-1] + temp[jj+1]
                    temp[jj+1] = 0
                elif temp[jj] =='-':
                    temp[jj-1] = temp[jj-1] - temp[jj+1]
                    temp[jj+1] = 0

    print(temp)



    return 1

def solution(expression):
    answer = 0
    temp = set()
    num =""
    problem = []
    for x in expression:
        if x.isdigit():
            num+=x

        if not x.isdigit():
            temp.add(x)
            problem.append(int(num))
            problem.append(x)
            num = ""
    problem.append(int(num))
    su =list(temp)

    print(problem)
    # 연산자 순열을 위한 box
    box = [i for i in range(len(temp))]
    ans = cal(box,problem,su)
    while True:
        if next_permutation(box):
            cal(box,problem,su)
        else :
            break


    return answer

# [100,-,200,-,400,-,500,-,600,-,600]
# 60420  300 9 // 2 1,3,5,7
expression = ["100-200*300-500+20","50*6-3*2"]

for i in range(2):
    print(solution(expression[i]))