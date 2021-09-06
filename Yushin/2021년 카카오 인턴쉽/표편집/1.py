# U X  현재 행에서  X칸 위에있느행
# D X 현재 행에서 X칸 밑에있는행
# C 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# Z 마지막에 삭제한 행 복구 단, 현재 선택된 행은 바뀌지 않습니다.

# "OOXOXOOO"


# 효율성 0점

def solution(n, k, cmd):

    # 체크배열
    check = ['O'] * n
    # k는 현재위치

    lcmd = len(cmd)
    stack = []
    for i in range(lcmd):
        # print(stack)
        if len(cmd[i]) == 1 :
            x = cmd[i]
            # 삭제
            if x == 'C':
                check[k] = 'X'
                stack.append(k)
                ok = False
                if k+1 < len(check):
                    for i in range(k+1,len(check)):
                        if check[i] == 'O':
                            k = i
                            ok = True
                            break
                if not ok :
                    for i in range(k-1,-1,-1):
                        if check[i] =='O':
                            k = i
                            break
            else:
                num = stack.pop()
                check[num] = 'O'


        else:
            # x : 명령어, y: 숫자
            x,y = cmd[i].split()
            y = int(y)
            if x == 'U':
                for i in range(k-1,-1,-1):
                    if check[i] == 'O':
                        y -=1
                    if y == 0 :
                        k = i
                        break
            else :
                for i in range(k+1,len(check)):
                    if check[i] == 'O':
                        y -= 1

                    if y == 0:
                        k = i
                        break


    return "".join(check)


n = [8,8]
k = [2,2]
cmd = [["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]]

for i in range(2):
    print(solution(n[i],k[i],cmd[i]))