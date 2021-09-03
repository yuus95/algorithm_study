from collections import deque
x = ["(()())()",")(","()))((()"]

def reverse():
    return


def check_p(p):
    test = deque(p)
    u,v ="",""
    stack =[]
    while test :
        x = test.popleft()
        if x == ')':
            stack.append(x)
            u+=x
        else :
            u+= x
            if stack:
                stack.pop()
            else:
                test.appendleft(x)
                v = test
                break


    return "".join(u),"".join(v)




# 첫번 쨰 문제풀이 실패 다시풀어보기
def solution(p):
    answer = ""
    if p == "":
        return

    u,v = check_p(p)
    print("u",u)
    print("v",v)


    return answer




for p in x :
    print(solution(p))

