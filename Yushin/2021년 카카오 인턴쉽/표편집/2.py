# U X  현재 행에서  X칸 위에있느행
# D X 현재 행에서 X칸 밑에있는행
# C 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# Z 마지막에 삭제한 행 복구 단, 현재 선택된 행은 바뀌지 않습니다.

# "OOXOXOOO"

def solution(n, k, cmd):

    check = [1] * n
    stack = []
    for i in range(len(cmd)):
        if len(cmd[i]) == 1 :
            x = cmd[i]
            if x == 'C':
                check[k] = 0
                stack.append(k)
                if sum(check[k+1:]) == 0 :
                    for i in range(k-1,-1,-1):
                        if check[i] == 1 :
                            k = i
                            break
                else :
                    for i in range(k+1,len(check)):
                        if check[i] ==  1 :
                            k = i
                            break
            else :
                num = stack.pop()
                check[num] = 1


        else :
            x,y = cmd[i].split()
            y= int(y)
            if x == 'U':
                if sum(check[:k]) == 0 :
                    break
                else :
                    for i in range(k-1,-1,-1):
                        if check[i] == 1:
                            y -=1
                        if y == 0 :
                            k = i

            else :
                if sum(check[k+1:]) == 0 :
                    break
                else:
                    for i in range(k+1,len(check)):
                        if check[i] == 1:
                            y -= 1
                        if y == 0 :
                            k = i
    answer = ""
    for i in range(len(check)):
        if check[i] == 0 :
            answer += 'X'
        else :
            answer +='O'

    return answer

n = [8,8]
k = [2,2]
cmd = [["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]]

for i in range(2):
    print(solution(n[i],k[i],cmd[i]))