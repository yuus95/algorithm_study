def solution(row,col):
    temp = [[0] * col for _ in range(row)]
    count = row * col - 1
    temp[0][0] = 1

    # 보안상 삭제
    return temp

row =[3,3]
col = [3,4]

for i in range(3):
    print(solution(row[i],col[i]))