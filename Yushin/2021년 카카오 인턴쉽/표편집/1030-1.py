# U X  현재 행에서  X칸 위에있느행
# D X 현재 행에서 X칸 밑에있는행
# C 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# Z 마지막에 삭제한 행 복구 단, 현재 선택된 행은 바뀌지 않습니다.

# "OOXOXOOO"


# 효율성 0점
import copy


class linked:

    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None


def solution(n, k, cmd):
    ans = linked(0)
    temp = linked(0)
    stack = []
    result = "O" * n

    # 초기설정
    for i in range(1, n):
        t = linked(i)
        t.left = temp
        temp.right = t
        temp = t
        if i == 1:
            ans.right = temp
    # 커서 위치
    for i in range(k):
        test_reset = ans.right
        ans = test_reset
    # 명령어 처리
    for c in cmd:
        if len(c) >= 2:
            # x 명령어  y:숫자
            x, y = c.split()
            y = int(y)
            if x == "D":
                for _ in range(y):
                    if ans.right == None:
                        break
                    test_reset = ans.right
                    ans = test_reset

            else:
                for _ in range(y):
                    if ans.left == None:
                        break
                    test_reset = ans.left
                    ans = test_reset

        # C
        elif c == "C":
            deleteIdx = ans
            if ans.right == None:
                ans = ans.left
                ans.right = None
            elif ans.left == None:
                ans = ans.right
                ans.left = None
            else:
                ans.left.right = ans.right
                ans.right.left = ans.left
                ans = ans.right
            stack.append(deleteIdx)

        else:  # Z
            value = stack.pop()
            if value.left != None:
                value.left.right = value

            if value.right != None:
                value.right.left = value
    result = list(result)
    for x in stack:
        result[x.num] = 'X'
    result = "".join(result)


    return result


n = [8, 8]
k = [2, 2]
cmd = [["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"],
       ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]]

for i in range(2):
    print(solution(n[i], k[i], cmd[i]))
