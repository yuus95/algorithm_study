def solution(p):
    def divide(p):
        count = 0
        for i in range(len(p)):
            if p[i] == '(':
                count += 1
            elif p[i] == ')':
                count -= 1
            if count == 0:
                return p[:i+1],p[i+1:]
    def right(p):
        for i in p:
            count = 0
            if i == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
            return True
    if p == '':
        return ''
    u,v = divide(p)
    if right(u):
        return u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        del_u = u[1:-1]
        for i in range(len(del_u)):
            if del_u[i] == '(':
                answer += ')'
            else:
                answer += '('
        return answer
    return answer