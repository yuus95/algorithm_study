# U X  현재 행에서  X칸 위에있느행
# D X 현재 행에서 X칸 밑에있는행
# C 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# Z 마지막에 삭제한 행 복구 단, 현재 선택된 행은 바뀌지 않습니다.

# "OOXOXOOO"


# 효율성 0점

def solution(n, k, cmd):

    # 표상태
    check=['O'] * n


    # 스택 - 삭제한 행 복구하기
    stack = []

    for cm in cmd:
        if len(cm) > 1 :
            x,y = cm.split()
            y = int(y)
            if x =='U':
                for i in range(k-1,-1,-1):
                    if check[i] =='O':
                        y -= 1
                        if y == 0 :
                            k = i
                            break

            else :
              for i in range(k+1,n):
                  if check[i] == 'O':
                      y -=1
                      if  y == 0 :
                          k = i
                          break

        else:
            if cm == 'C':
                check[k] = 'X'
                stack.append(k)
                for i in range(k+1,n):
                    if check[i] == 'O':
                        k = i
                        break
                else  :
                     for i in range(k-1,-1,-1):
                         if check[i] =='O':
                            k = i
                            break
            else:
                pop = stack.pop()
                check[pop] = 'O'

    # print(check)

    return  "".join(check)


n = [8,8]
k = [2,2]
cmd = [["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]]

for i in range(2):
    print(solution(n[i],k[i],cmd[i]))