from copy import copy
from itertools import permutations

def solution(expression):
    answer = 0
    temp = []
        # "100-200*300-500+20"
    text =""
    for x in expression:
        if x.isdigit():
            text+=x
        else :
            temp.append(int(text))
            temp.append(x)
            text = ""
    if text :
        temp.append((int(text)))

    ans_box = ["+","-","*"]
    result = list(permutations(ans_box,3))

    for res in result:
        num = 0

        # 수식어
        ex = len(temp)//2

        copy_temp = temp[:]

        for x in res :
            for i in range(0,ex):
                # 연산자 인덱스
                idx = i * 2 + 1

                if x == temp[idx]:
                    if x == '+':
                        copy_temp[idx-1] = copy_temp[idx-1] + copy_temp[idx+1]
                        copy_temp[idx+1] = 0
                    elif x == '-':
                        copy_temp[idx-1] = copy_temp[idx-1] - copy_temp[idx+1]
                        copy_temp[idx+1] = 0

                    else :
                        if copy_temp[idx-1] == 0 :
                            for j in range(idx-1,-1,-2):
                                if copy_temp[j] != 0 :
                                    copy_temp[j] = copy_temp[j] * copy_temp[idx+1]
                                    break
                        else:
                            copy_temp[idx-1] = copy_temp[idx-1] * copy_temp[idx+1]
                        copy_temp[idx+1]= 0
                print(copy_temp)

                for i in range(0,len(copy_temp),+2):
                    num +=copy_temp[i]
                if answer < abs(num):
                    answer = abs(num)

    return answer

# [100,-,200,-,400,-,500,-,600,-,600]
# 60420  300 9 // 2 1,3,5,7
expression = ["100-200*300-500+20","50*6-3*2"]

for i in range(2):
    print(solution(expression[i]))