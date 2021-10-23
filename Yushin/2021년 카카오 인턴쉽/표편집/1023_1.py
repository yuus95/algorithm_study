# U X  현재 행에서  X칸 위에있느행
# D X 현재 행에서 X칸 밑에있는행
# C 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# Z 마지막에 삭제한 행 복구 단, 현재 선택된 행은 바뀌지 않습니다.

# "OOXOXOOO"


# 효율성 0점
import copy


def solution(n, k, cmd):
    # 이중 연결 노드
    ans = {i: [i-1,i+1] for i in range(1,n+1)}
    cur = k+1
    stack = []
    for c in cmd:
        if len(c) >= 2:
            x,y = c.split()
            y = int(y)
            # print(x,y)
            if x == 'U':
                for _ in range(y):
                    if ans[cur][0] == 0 :
                        break
                    cur = ans[cur][0]
            else :
                for _ in range(y):
                    if ans[cur][1] == n+1:
                        break
                    cur = ans[cur][1]
        elif c == 'C':
            temp =cur
            stack.append(temp)
            if ans[cur][1] == n+1 :
                ans[ans[cur][0]][1] = n+1
                cur = ans[cur][0]
            elif ans[cur][0] == 0:
                ans[ans[cur][1]][0] = 0
                cur = ans[cur][1]

            else:
                if ans[cur][1] != n+1:
                    ans[ans[cur][1]][0] = ans[cur][0]
                    ans[ans[cur][0]][1] = ans[cur][1]
                    cur = ans[cur][1]
                else:
                    ans[ans[cur][0]][1] = n+1
                    cur = ans[cur][0]
        else:
            lifo = stack.pop()
            if ans[lifo][1] != n+1:
                ans[ans[lifo][1]][0] = lifo
            if ans[lifo][0] != 0:
                ans[ans[lifo][0]][1] = lifo

    result = 'O' * n
    result = list(result)
    for i in stack:
        result[i-1] = 'X'
    result = "".join(result)
    return result


n = [8,8]
k = [2,2]
cmd = [["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]]

for i in range(2):
    print(solution(n[i],k[i],cmd[i]))