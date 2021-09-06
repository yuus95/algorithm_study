# 시간초과
from bisect import bisect_left, bisect_right
def solution(n, k, cmd):
    answer = []
    graph = [i for i in range(n)]
    temp = [i for i in range(n)]
    queue = []
    for i in cmd:
        i = i.split()
        if i[0] == 'U':
            k -= int(i[1])
        elif i[0] == 'D':
            k += int(i[1])
        elif i[0] == 'C':
            queue.append(graph[k])
            graph.remove(graph[k])
            if k > len(graph)-1: # k는 인덱스 위치, 인덱스 위치가 길이를 벗어날경우 맞춰줌
                k = len(graph)-1
        elif i[0] == 'Z':
            re = queue.pop() # re는 유일한 값 (0,1,2 ...)
            bi = bisect_left(graph, re) # re가 들어갈 위치
            print(bi, re)
            graph.insert(bi, re)
            if k >= bi: # bi(들어갈 위치)가 인덱스 보다 작을 경우 인덱스 밀려야함 선택된 값이 안바뀌기 위해
                k += 1 
        
    graph = set(graph)
    temp = set(temp)
    demo = temp - graph
    for i in range(n):
        if i in demo:
            answer.append('X')
        else:
            answer.append('O')
    
    return ''.join(answer)