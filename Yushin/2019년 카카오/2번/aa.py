from collections import Counter

# 실패율 확률로 내림차순 만들기
def solution(N, stages):
    answer = []
    result=[]
    temp = [[0,0]  for _ in range(N+1)]
    people = len(stages)
    a = Counter(stages)
    for i in range(1,len(temp)):
        count = a[i]
        if people == 0:
            answer.append([i, 0])
            continue
        answer.append([i,count/ people])
        people -= count


    answer.sort(key=lambda x: (-x[1],x))
    for i in range(len(answer)):
        result.append(answer[i][0])

    return result







n = [5,4]
stages=[[2, 1, 2, 6, 2, 4, 3, 3],[4,4,4,4,4]]


for i in range(2):
    solution(n[i],stages[i])