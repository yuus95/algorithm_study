# x 가 3이상  y 가 3이상이면 안에 사각형이 생김
import  copy
from collections import  deque

def solution(rows, columns, queries):
    answer = []
    box = [[0]* columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            box[i][j] = i * rows + j % columns +1

    for query in queries:
        x1 = query[0] -1
        y1= query[1] -1
        x2= query[2] -1
        y2 = query[3] -1

        temp = copy.deepcopy(box)
        arr1 = box[x1][y1:y2+1]
        for k in range(y1,y2+1):
            if k == y1:
                temp[x1][k] = box[x1+1][y1]
            else:
                temp[x1][k] = box[x1][k-1]

        for k in range(x1+1,x2+1):
            if k == x1+1 :
                temp[k][y2] = box[x1][y2]
            else:
                temp[k][y2]  = box[k-1][y2]

            arr1.append(temp[k][y2])

        for k in range(y2-1,y1-1,-1):
            if k == y2-1:
                temp[x2][k] = box[x2][y2]
            else:
                temp[x2][k] = box[x2][k+1]
            arr1.append(temp[x2][k])

        for k in range(x2-1,x1,-1):
            if k == x2-1:
                temp[k][y1]   =box[x2][y1]
            else:
                temp[k][y1] = box[k+1][y1]
            arr1.append(temp[k][y1])
        answer.append(min(arr1))
        box = copy.deepcopy(temp)


    return answer

rows=[6,3,100]
columns=[6,3,97]
queries=[	[[2,2,5,4],[3,3,6,6],[5,1,6,3]],[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]],[[1,1,100,97]]]

for i in range(2):
    print(solution(rows[i],columns[i],queries[i]))