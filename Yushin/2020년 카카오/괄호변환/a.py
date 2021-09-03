from collections import deque
x = ["(()())()",")(","()))((()"]



# 첫번 쨰 문제풀이 실패 다시풀어보기
def solution(p):
    answer = ''
    u=""
    v=""
    temp = []
    if p == "":
        return answer
    v = p
    while True:
        lt = 0
        rt = 0
        # 처음 U가져오기
        for k in v :
            u+=k

            if k == '(':
                lt +=1
            else :
                rt +=1

            if lt == rt:
                 break




    print("u",u)



    return answer



#
# for p in x :
#     print(solution(p))
#

qq = [1,2,3,4]

print(not qq)