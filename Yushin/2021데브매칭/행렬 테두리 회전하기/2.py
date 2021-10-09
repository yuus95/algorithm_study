# x 가 3이상  y 가 3이상이면 안에 사각형이 생김
import  copy
from collections import  deque

def solution(rows, columns, queries):
    answer = []
    box=[]
    box = [[0]* columns for _ in range(rows)]
    num = 0
    for i in range(rows):
        for j in range(columns):
            num+=1
            box[i][j] = num
    # for r in range(rows):
    #     box.append([a for a in range(r * columns + 1, (r + 1) * columns + 1)])


    for query in queries:
        x1 = query[0] -1
        y1 = query[1] -1
        x2 = query[2] -1
        y2 = query[3] -1
        minNum = 2147000


        # 현재 바뀌기전 값
        # 이전값
        lastValue = box[x1+1][y1]
        for k in range(y1,y2+1):
            if lastValue < minNum :
                minNum = lastValue
            tmp = box[x1][k]
            box[x1][k] = lastValue
            lastValue = tmp


        for k in range(x1+1,x2+1):
            if lastValue < minNum :
                minNum = lastValue
            tmp = box[k][y2]
            box[k][y2] = lastValue
            lastValue = tmp

        for k in range(y2-1,y1-1,-1):
            if lastValue < minNum :
                minNum = lastValue
            tmp = box[x2][k]
            box[x2][k] = lastValue
            lastValue = tmp


        for k in range(x2-1,x1,-1):
            if lastValue < minNum :
                minNum = lastValue
            tmp = box[k][y1]
            box[k][y1] = lastValue
            lastValue=  tmp


        answer.append(minNum)
    return answer

rows=[6,3,100]
columns=[6,3,97]
queries=[	[[2,2,5,4],[3,3,6,6],[5,1,6,3]],[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]],[[1,1,100,97]]]

for i in range(2):
    print(solution(rows[i],columns[i],queries[i]))