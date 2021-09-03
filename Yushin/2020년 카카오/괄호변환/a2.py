# 츨처 https://jiwon-lee-it.tistory.com/44

from collections import deque
x = ["(()())()",")(","()))((()"]


def pair(p):
    count = 0

    # "("와 ")"의 짝수가 맞는지 검정
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= -1

    return True


def balance(p):
    count = 0

    # u와 v로 나누어야 될 구간 리턴하도록
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def solution(p):
    answer = ''

    if p == '':
        return answer

    index = balance(p)

    # u와 v로 분해
    u = p[:index + 1]
    v = p[index + 1:]

    # 재귀함수 사용 # 문제 지시사항 그대로 command
    if pair(u):
        answer = u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"

        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)

    return answer




for p in x :
    print(solution(p))